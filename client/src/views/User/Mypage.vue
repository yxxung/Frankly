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
        v-model="modifyFlag"
        hide-footer
        title="개인정보 수정"
      >
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

      <div class="mypage-info">
        <div class="mypage-user">
          <h2 class="mypage-user-name">
            <img src="@/assets/icon/Anonymous_user.svg" alt="" />{{
              user.userName
            }}
          </h2>
          <h4 class="mypage-user-email">{{ user.userEmail }}</h4>
          <h4 class="mypage-user-region">{{ user.district }}</h4>
        </div>

        <div class="mypage-bookmark">
          <a href="#"
            ><img src="@/assets/icon/Bookmark.svg" alt="" />북마크 국회의원</a
          >
          <div class="mypage-bookmark-politician">
            <!--<div class="politician-detail-image">
                  <img :src="'http://teamfrankly.kr/images/' + PoliticianDetailData.politicianID + '.png'" />
                </div>
                <div class="politician-detail-name">
                  {{ PoliticianDetailData.politicianName }}-->
          </div>
        </div>

        <div class="mypage-board">
          <li>
            <a href="/posted"
              ><img src="@/assets/icon/Document.svg" alt="" />내가 쓴 글</a
            >
          </li>
          <li>
            <a href="/replied"
              ><img src="@/assets/icon/Comment.svg" alt="" />내가 쓴 댓글</a
            >
          </li>
          <li>
            <a href="/liked"
              ><img src="@/assets/icon/Like_active.svg" alt="" />내가 좋아한
              글</a
            >
          </li>
        </div>
      </div>
      <Navigation />
    </div>
  </body>
</template>

<script>
import axios from "axios";
import Navigation from "@/components/Navigation.vue";

const userStore = "userStore";

export default {
  name: "Mypage",
  components: {
    Navigation: Navigation,
  },
  data() {
    return {
      modifyFlag: false,
      user: {
        userName: "",
        userEmail: "",
        district: "",
      },
    };
  },
  created() {
    const userID = 2;
    axios
      .get(`/api/users/${userID}`)
      .then((response) => {
        console.log("users", response.data);
        this.user.userName = response.data.name;
        this.user.userEmail = response.data.email;
        this.user.district = response.data.district;
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
      const userID = 2;
      axios
        .put(`/api/users/${userID}/update`)
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
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";

.wrap {
  font-family: "Noto Sans KR";
}
.mypage-user {
  padding: 8px 24px;
}
.mypage-user > h2 {
  padding: 8px 12px;
  color: #2b2b2b;
  font-size: 16px;
}
.mypage-user-name {
  margin: 0;
}
.mypage-user-name img {
  padding: 0px 10px 0px 0px;
  width: 30px;
  height: 30px;
}
.mypage-user > h4 {
  padding: 0px 12px;
  color: #818181;
  font-size: 12px;
}
.mypage-bookmark {
  padding: 8px 24px;
}
.mypage-bookmark a {
  padding: 8px;
  color: #2b2b2b;
  font-size: 16px;
  text-decoration: none;
}
.mypage-board {
  padding: 8px 24px;
}
.mypage-board a {
  color: #2b2b2b;
  font-size: 16px;
  text-decoration: none;
}
.mypage-board li {
  padding: 8px;
}
</style>
