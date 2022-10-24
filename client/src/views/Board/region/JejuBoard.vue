<template>
  <div class="wrap">
    <!--헤더-->
    <header class="header header--back">
      <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
        <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
      </a>
      <h2>제주특별자치도</h2>
    </header>

    <ul class="post-list">
      <li
        class="post-list__container"
        v-for="board in boards"
        :key="board.boardID"
        @click="goToBoardDetail(board.boardID)"
      >
        <div class="post-list__title">
          <img src="@/assets/icon/Image.svg" alt="이미지 있음" />
          <h3>{{ board.title }}<span>[110]</span></h3>
        </div>
        <p>{{ board.content }}</p>
        <div class="post-list__info">
          <span>{{ elapsedText(board.boardRegDate) }}</span>
          <img src="@/assets/icon/Like.svg" alt="좋아요" />
          <span>{{ board.marked }}</span>
        </div>
      </li>
    </ul>
    <FloatingButton />
    <Navigation />
  </div>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import FloatingButton from "@/components/FloatingButton.vue";

import axios from "axios";
import dateformat from "@/commons/dateformat.js";

export default {
  components: {
    Navigation: Navigation,
    FloatingButton: FloatingButton,
  },
  data() {
    return {
      boards: [],
    };
  },
  mounted() {
    this.getBoardList();
  },
  methods: {
    getBoardList() {
      console.log(this.$axios);
      axios
        .get(`/api/boards/boardlist/제주특별자치도`)
        .then((response) => {
          console.log("boards", response.data);
          this.boards = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    goToBoardDetail(boardID) {
      this.$router.push({
        name: "BoardDetail",
        params: {
          boardID: boardID,
        },
      });
    },
    //date format 변환
    elapsedText(date) {
      return dateformat.elapsedText(new Date(date));
    },

    // 무한 스크롤 정의
    handleNotificationListScroll(e) {
      const { scrollHeight, scrollTop, clientHeight } = e.target;
      const isAtTheBottom = scrollHeight === scrollTop + clientHeight;
      // 일정 한도 밑으로 내려오면 함수 실행
      if (isAtTheBottom) this.handleLoadMore();
    },

    // 내려오면 api 호출하여 아래에 더 추가, total값 최대이면 호출 안함
    handleLoadMore() {
      if (this.notifications.length < this.total) {
        const params = {
          limit: this.params.limit,
          page: this.params.page + 1,
        };
        this.$store.commit(
          "notification/SET_PARAMS",
          this.filterValue ? { ...params, type: this.filterValue } : params
        );
        this.dispatchGetNotifications(false);
      }
    },

    // 스크롤을 맨위로 올리고 싶을 때
    handleClickTitle() {
      this.$refs["notification-list"].scroll({ top: 0, behavior: "smooth" });
    },

    // 새로고침
    handleClickRefresh() {
      this.$refs["notification-list"].scroll({ top: 0 });
      this.dispatchGetNotifications(true);
    },

    // 처음 렌더링시 이전 알림 불러오기 or reset=true시 새로고침, false시 이전 목록에 추가
    dispatchGetNotifications(reset) {
      this.$store.dispatch("notification/getNotifications", reset);
    },
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";
</style>