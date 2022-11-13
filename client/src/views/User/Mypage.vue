<template>
  <body>
    <div class="wrap">
      <!--헤더-->
      <header class="header header--back">
        <a class="icon-button-56 header__back-button" href="/">
          <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
        </a>
        <h2>마이페이지</h2>

        <a class="icon-button-56 header-right-icon">
          <b-dropdown
            size="xs"
            variant="link"
            toggle-class="text-decoration-none"
            no-caret
            ><template #button-content>
              <img src="@/assets/icon/Settings.svg" alt="설정" />
              <span class="visually-hidden"></span>
            </template>
            <b-dropdown-item @click="clickModifyBtn"
              >개인정보 수정</b-dropdown-item
            >
            <b-dropdown-item @click="logoutUser">로그아웃</b-dropdown-item>
            <b-dropdown-item @click="deleteUser">회원탈퇴</b-dropdown-item>
          </b-dropdown></a
        >
      </header>

      <b-modal v-model="modifyFlag" hide-footer title="개인정보 수정">
        <b-form-group
          label="Street:"
          label-for="nested-street"
          label-cols-sm="3"
          label-align-sm="end"
        >
          <b-form-input id="nested-street"></b-form-input>
        </b-form-group>
        <b-form-group
          label="City:"
          label-for="nested-city"
          label-cols-sm="3"
          label-align-sm="end"
        >
          <b-form-input id="nested-city"></b-form-input>
        </b-form-group>
        <b-form-group
          label="State:"
          label-for="nested-state"
          label-cols-sm="3"
          label-align-sm="end"
        >
          <b-form-input id="nested-state"></b-form-input>
        </b-form-group>
        <b-form-group
          label="Country:"
          label-for="nested-country"
          label-cols-sm="3"
          label-align-sm="end"
        >
        </b-form-group>
        <b-button
          class="mt-3"
          variant="outline-danger"
          block
          @click="CancelModifyBtn"
          >취소</b-button
        >
        <b-button
          class="mt-2"
          variant="outline-warning"
          block
          @click="updateUser"
          >수정</b-button
        >
      </b-modal>
      <div class="mypage">
        <div class="mypage-info">
          <div class="mypage-image">
            <img src="@/assets/icon/Anonymous_user.svg" />
          </div>
          <div class="mypage-user-detail">
            <h2 class="mypage-user-name">{{ userInfo.name }}</h2>
            <h4 class="mypage-user-region">{{ userInfo.district }}</h4>
          </div>
        </div>

        <div class="mypage-detail">
          <div class="mypage-detail-list">
            <h2>북마크 국회의원</h2>
            <BookmarkPolitician />
          </div>

          <div class="mypage-detail-list">
            <h2>좋아요한 글</h2>
            <LikeBoard />
          </div>
        </div>
      </div>
      <Navigation />
    </div>
  </body>
</template>

<script>
import axios from "axios";
import Navigation from "@/components/Navigation.vue";
import { mapMutations, mapState } from "vuex";

export default {
  name: "Mypage",
  components: {
    Navigation: Navigation,
  },
  data() {
    return {
      modifyFlag: false,
      userInfo: {},
    };
  },
  computed: {
    ...mapState({ userStore: "userStore" }),
    ...mapMutations(["userStore/SET_IS_LOGIN", "userStore/SET_USER_INFO"])
  },
  created() {
    axios
      .get(`/api/users/${this.userStore.userID}`)
      .then((response) => {
        console.log("users", response.data);
        this.userInfo = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    //수정 버튼 클릭 시
    clickModifyBtn() {
      this.modifyFlag = true;
    },
    // 취소 버튼 클릭 시
    CancelModifyBtn() {
      this.modifyFlag = false;
      location.href = "/Mypage";
    },
    //회원 정보 수정
    updateUser() {
      axios
        .put(`/api/users/${this.userStore.userID}/update`)
        .then((response) => {
          if (response.status === 200) {
            alert("회원 정보 수정이 완료됐습니다.");
          }
          this.$router.go();
        })
        .catch(() => {
          console.log("수정 요청 실패");
        });
    },

    //회원탈퇴
    deleteUser() {
      const userID = 2;
      axios
        .delete(`/api/users/${userID}/delete`)
        .then((response) => {
          if (response.status === 200) {
            alert("회원 탈퇴가 완료됐습니다.");
          }
          this.$router.go();
        })
        .catch(() => {
          console.log("탈퇴 요청 실패");
        });
    },
    logoutUser() {
      this.userStore/SET_IS_LOGIN(false);
      this.userStore/SET_USER_INFO(null);

      sessionStorage.removeItem("token");

      if (this.$route.path != "/") {
        this.$router.push({ name: "Login" });
      }
    }
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";

.wrap {
  font-family: "Noto Sans KR";
}
.mypage {
  padding: 8px 24px;
}
.mypage-info {
  display: flex;
}

.mypage-image {
  flex: 1;
  width: 50%;
  max-width: 50px;
  max-height: 50px;
}

.mypage-image > img {
  width: 50px;
  height: 50px;
  vertical-align: middle;
}

.mypage-user-detail {
  margin: auto 0 auto 10px;
  flex: 1;
  width: 50%;
  vertical-align:middle;
}

.mypage-user-name {
  font-size: 19px;
  margin: 0;
}

.mypage-user-region {
  font-size: 14px;
  color: #7e7e7e;
  margin: 6px 0;
}

.mypage-detail {
  width: 100%;
  max-width: 540px;
  height: 100%;
  margin: 30px auto;
}

.mypage-detail-list > h2 {
  margin: 20px auto;
  font-style: normal;
  font-weight: 600;
  font-size: 22px;
  line-height: 23px;
  letter-spacing: -0.024em;

  color: #383838;
}
</style>
