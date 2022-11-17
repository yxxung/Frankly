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

      <b-modal
        style="font-family: Noto Sans KR; margin: 0 auto"
        v-model="modifyFlag"
        hide-footer
        title="개인정보 수정"
      >
        <b-container fluid style="margin: 0 auto">
          <b-row>
            <b-col sm="2">
              <label
                style="font-size: 15px"
                class="mt-2"
                for="textarea-auto-height"
                >이름</label
              >
            </b-col>
            <b-col sm="10">
              <b-form-textarea
                id="textarea-auto-height"
                class="mt-2"
                disabled
                v-model="user.name"
                size="sm"
                rows="1"
                max-rows="3"
              ></b-form-textarea>
            </b-col>
          </b-row>
          <b-row>
            <b-col sm="2">
              <label
                style="font-size: 15px"
                class="mt-2"
                for="textarea-auto-height"
                >이메일</label
              >
            </b-col>
            <b-col sm="10">
              <b-form-textarea
                id="textarea-auto-height"
                class="mt-2"
                disabled
                v-model="user.email"
                size="sm"
                rows="1"
                max-rows="3"
              ></b-form-textarea>
            </b-col>
          </b-row>
          <!--<b-row>
            <b-col sm="2">
              <label for="textarea-auto-height">비밀번호</label>
            </b-col>
            <b-col sm="10">
              <b-form-textarea
                id="textarea-auto-height"
                class="mt-3"
                v-model="user.password"
                size="sm"
                rows="3"
                max-rows="8"
              ></b-form-textarea>
            </b-col>
          </b-row>-->
          <b-row>
            <b-col sm="2">
              <label
                style="font-size: 15px"
                class="mt-2"
                for="textarea-auto-height"
                >전화번호</label
              >
            </b-col>
            <b-col sm="10">
              <b-form-textarea
                id="textarea-auto-height"
                class="mt-2"
                v-model="user.contact"
                size="sm"
                rows="1"
                max-rows="3"
              ></b-form-textarea>
            </b-col>
          </b-row>
          <b-row>
            <b-col sm="2">
              <label
                style="font-size: 15px"
                class="mt-2"
                for="textarea-auto-height"
                >지역</label
              >
            </b-col>
            <b-col sm="10">
              <b-form-textarea
                class="mt-2"
                v-model="user.district"
                size="sm"
                rows="1"
                max-rows="3"
              ></b-form-textarea>
            </b-col>
          </b-row>
        </b-container>
        <b-button
          align="center"
          class="mt-5"
          variant="Light"
          @click="CancelModifyBtn"
          >취소</b-button
        >
        <b-button align="center" class="mt-5" variant="dark" @click="updateUser"
          >수정</b-button
        >
      </b-modal>
      <div class="mypage">
        <div class="mypage-info">
          <div class="mypage-image">
            <img src="@/assets/icon/Anonymous_user.svg" />
          </div>
          <div class="mypage-user-detail">
            <h2 class="mypage-user-name">{{ user.name }}</h2>
            <h4 class="mypage-user-region">{{ user.district }}</h4>
          </div>
        </div>

        <div class="mypage-detail">
          <div v-if="adminFlag === true" class="mypage-detail-list">
            <h2>관리자 페이지</h2>
            <div class="admin-wrap">
              <div class="admin-container">
                <div class="admin-statistics" @click="goToEditUser()">
                  회원 관리
                </div>
                <div class="admin-statistics" @click="goToEditBoard()">
                  게시글 관리
                </div>
              </div>
            </div>
          </div>

          <div class="mypage-detail-list">
            <h2>북마크 국회의원</h2>
            <BookmarkPolitician
              v-bind:bookmarkPoliticians="bookmarkPoliticians"
            />
          </div>

          <div class="mypage-detail-list">
            <h2>좋아요한 글</h2>
            <LikeBoard
            v-bind:likeBoards="likeBoards"/>
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
import { mapState } from "vuex";
import BookmarkPolitician from "@/views/User/BookmarkPolitician.vue"
import LikeBoard from "@/views/User/LikeBoard.vue"

export default {
  name: "Mypage",
  components: {
    Navigation: Navigation,
    BookmarkPolitician: BookmarkPolitician,
    LikeBoard: LikeBoard
  },
  data() {
    return {
      modifyFlag: false,
      adminFlag: false,
      user: {},
      bookmarkPoliticians: [],
      likeBoards: []
    };
  },
  computed: {
    ...mapState({ userStore: "userStore" }),
    //...mapState([ 'userInfo', 'isLogin' ])
  },
  mounted() {
    this.setAdminpage();
  },
  created() {
    axios
      .get(`/api/users/${this.userStore.userInfo.userID}`)
      .then((response) => {
        console.log("users", response.data);
        this.user = response.data;
      })
      .catch((error) => {
        console.log(error);
      });

    axios
      .get(`/api/likeBookmark/bookmark/${this.userStore.userID}`, {
        headers: {},
      })
      .then((response) => {
        this.bookmarkPoliticians = response.data;
      })
      .catch((error) => {
        console.log(error);
      });

      axios
      .get(`/api/likeBookmark/like/${this.userStore.userID}`, {
        headers: {},
      })
      .then((response) => {
        this.likeBoards = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    setAdminpage() {
      //관리자 페이지 isShow
      let authorities = this.userStore.userInfo.authorities;

      for (let i = 0; i < authorities.length; i++) {
        if (authorities[i].authority === "ROLE_ADMIN") {
          this.adminFlag = true;
        }
        /*else if(authorities[i].authority === "ROLE_USER") {
        this.adminFlag = false;
      }*/
      }
    },
    //수정 버튼 클릭 시
    clickModifyBtn() {
      this.modifyFlag = true;
    },
    // 취소 버튼 클릭 시
    CancelModifyBtn() {
      this.modifyFlag = false;
    },
    //회원 정보 수정
    updateUser() {
      axios
        .put(`/api/users/${this.userStore.userInfo.userID}/update`, {
          userID: this.user.userID,
          name: this.user.name,
          email: this.user.email,
          password: this.user.password,
          contact: this.user.contact,
          district: this.user.district,
          userAuth: this.userStore.userInfo.userAuth,
        })
        .then((response) => {
          this.modifyFlag = false;
          if (response.status === 200) {
            alert("회원 정보 수정이 완료됐습니다.");
          }
        })
        .catch(() => {
          console.log("수정 요청 실패");
        });
    },
    confirmDelete() {
      if (confirm("정말 탈퇴하시겠습니까?") == true) {
        //확인
        document.form.submit();
      } else {
        //취소
        return;
      }
    },
    //회원탈퇴
    deleteUser() {
      if (confirm("정말 탈퇴하시겠습니까?") == true) {
        axios
          .delete(`/api/users/${this.userStore.userID}/delete`)
          .then((response) => {
            if (response.status === 200) {
              alert("회원 탈퇴가 완료됐습니다.");

              this.$store.commit("userStore/SET_IS_LOGIN", false);
              this.$store.commit("userStore/SET_USER_INFO", null);
              this.$store.commit("userStore/SET_USER_ID", null);

              sessionStorage.removeItem("token");
              sessionStorage.removeItem("userID");

              if (this.$route.path != "/") {
                this.$router.push({ name: "AuthPage", component: "AuthPage" });
              }
            }
          })
          .catch((error) => {
            console.log("탈퇴 요청 실패", error);
          });
      } else {
        return;
      }
    },
    //로그아웃
    logoutUser() {
      this.$store.commit("userStore/SET_IS_LOGIN", false);
      this.$store.commit("userStore/SET_USER_INFO", null);
      this.$store.commit("userStore/SET_USER_ID", null);

      sessionStorage.removeItem("token");
      sessionStorage.removeItem("userID");

      if (this.$route.path != "/") {
        this.$router.push({ name: "Login" });
      }
    },
    goToEditUser() {
      this.$router.push("/EditUser");
    },
    goToEditBoard() {
      this.$router.push("/EditBoard");
    },
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
  vertical-align: middle;
}

.mypage-user-name {
  font-size: 19px;
  margin: 3px 0;
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

.admin-wrap {
  width: 100%;
  display: flex;
  justify-content: center;
  justify-items: center;
}

.admin-container {
  display: flex;
  justify-content: flex-start;
  margin: 5px auto;
  width: 100%;
  max-width: 540px;
  background: #ffffff;
}

.admin-statistics {
  padding: 8px 16px;
  color: #3c3c3c;
  border-radius: 8px;
  border: 1px solid #ebe8e2;
  margin-right: 8px;
}

.admin-statistics:hover {
  cursor: pointer;
  background-color: #f2eee8;
}
</style>
