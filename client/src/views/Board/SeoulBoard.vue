<template>
  <div class="wrap">
    <!--헤더-->
    <header class="header header--back">
      <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
        <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
      </a>
      <h2>서울특별시</h2>
    </header>

    <ul class="post-list">
      <li
        class="post-list__container"
        v-for="board in boardList"
        :key="boardID"
        @click="DetailView(idx)"
      >
        <div class="post-list__title">
          <img src="@/assets/icon/Image.svg" alt="이미지 있음" />
          <h3 @click="$router.push('BoardDetail/'+$route.params.boardID)">{{ board.title }}<span>[110]</span></h3>
        </div>
        <p>{{ board.content }}</p>
        <div class="post-list__info">
          <span>{{ board.regDate }}</span>
          <img src="@/assets/icon/Like.svg" alt="좋아요" />
          <span>13</span>
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
  methods: {
    //게시글 리스트 불러오기
    getBoardList() {
      console.log(this.$axios);
      axios
        .get(`/api/boards/${region}`)
        .then((response) => {
          console.log("boards", response.data);
          this.freeboards = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    //게시글 상세보기
    DetailView(idx) {
      this.$router.push({
        //params를 넘겨줄때에는 push할때 path보단 name을 사용
        name: "BoardDetail",
        params: {
          boardId: idx
        },
      });
    },
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";

/*
게시판 목록
*/

.community-list {
  padding: 8px 24px;
}

.community-list > h4 {
  margin-bottom: 8px;
  font-size: 14px;
  font-weight: normal;
  color: #818181;
}

.community-list a {
  padding: 8px;
  display: flex;
  align-items: center;
  color: #2b2b2b;
  font-size: 16px;
}
.community-list a:hover {
  background-color: #f8f8f8;
}
.community-list img {
  margin-right: 8px;
}

/*
게시글 목록
*/

.post-list {
  padding-top: 14px;
}

/* 게시글 박스 */
.post-list__container {
  position: relative;
  padding: 16px 24px 30px;
  border-bottom: 1px solid #e7e7e7;
  -webkit-transition: all 0.08s ease-in-out;
  -o-transition: all 0.08s ease-in-out;
  transition: all 0.08s ease-in-out;
}
.post-list__container:hover {
  background-color: #f8f8f8;
  cursor: pointer;
}

/* 게시글 제목 */
.post-list__title {
  margin-bottom: 4px;
  display: flex;
  align-items: center;
}
.post-list__title > img {
  margin-right: 8px;
}
.post-list__title > h3 {
  font-size: 16px;
}
.post-list__title > h3 > span {
  font-family: "Roboto", serif;
  font-size: 14px;
  font-weight: bold;
  color: #ff3a3a;
}

/* 게시글 내용 */
.post-list__container > p {
  font-size: 14px;
  color: #7b7b7b;
}

/* 게시글 등록시간, 좋아요 수 */
.post-list__info {
  position: absolute;
  right: 24px;
  bottom: 8px;
  display: flex;
  align-items: center;
  color: #7b7b7b;
}
.post-list__info > span {
  font-size: 12px;
}

/*
게시글 페이지
*/

.post-header {
  padding: 0 16px;
}

.post-header__kategorie {
  padding: 4px 0;
  font-size: 12px;
  color: #696969;
}

.post-header__title {
  font-size: 20px;
  color: #2b2b2b;
}

.post-header__info {
  margin: 8px 0;
  display: flex;
  justify-content: space-between;
}

.post-header__writer {
  font-size: 12px;
  color: #696969;
}

.post-header__reg-date {
  font-size: 12px;
  color: #696969;
}

.post-content {
  padding: 0 16px;
}

/*게시글 좋아요, 싫어요*/
.post-like {
  padding: 24px 16px;
}
.post-like button {
  margin-right: 8px;
  background-color: #f3f3f3;
}
</style>