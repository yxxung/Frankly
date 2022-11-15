<template>
  <div class="wrap">
    <!--헤더-->
    <header class="header header--back">
      <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
        <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
      </a>
      <h2>내가 쓴 글</h2>
    </header>

    <ul class="post-list">
      <li
        class="post-list__container"
        v-for="board in boards"
        :key="board.boardID"
        @click="goToBoardDetail(board.boardID)"
      >
        <div class="post-list__title">
          <!--<img src="@/assets/icon/Image.svg" alt="이미지 있음" />--->
          <h3>
            {{ board.title }}<span>[{{ board.replyCount }}]</span>
          </h3>
        </div>
        <p>{{ board.content }}</p>
        <div class="post-list__info">
          <span>{{ elapsedText(board.boardRegDate) }}</span>
          <img src="@/assets/icon/Like.svg" alt="좋아요" />
          <span>{{ board.marked }}</span>
        </div>
      </li>
    </ul>
    <Navigation />
  </div>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import axios from "axios";
import dateformat from "@/commons/dateformat.js";
import { mapState } from "vuex";

export default {
  components: {
    Navigation: Navigation,
  },
  data() {
    return {
      boards: [],
      marked: "",
    };
  },
  mounted() {
    this.getBoardList();
  },
  computed: {
    ...mapState({ userStore: "userStore" }),
  },
  methods: {
    getBoardList() {
      axios
        .get(`/api/boards/user/${this.userStore.userID}`)
        .then((response) => {
          this.boards = response.data;
          this.marked = response.data.marked;
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
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";
</style>
