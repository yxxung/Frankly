<template>
  <ul class="like-post-list">
    <li
      class="like-post-list__container"
      v-for="like in likeBoards"
      :key="like.likeID"
      @click="goToBoardDetail(like.boardID)"
    >
      <div class="like-post-list__title">
        <h3>{{ like.title }}</h3>
      </div>
    </li>
  </ul>
</template>

<script>
export default {
  name: "LikeBoard",
  props: {
    likeBoards: Object,
  },
  data() {
    return {};
  },
  methods: {
    goToBoardDetail(boardID) {
      this.$router.push({
        name: "BoardDetail",
        params: {
          boardID: boardID,
        },
      });
    },
  },
};
</script>

<style>
@import '@/assets/scss/style.scss';
/* 게시글 목록 */
.like-post-list {
    padding: 14px 0;
}
/* 게시글 박스 */
.like-post-list__container {
    position: relative;
    padding: 6px 8px 6px;
    border-bottom: 1px solid #e7e7e7;
    -webkit-transition: all 0.08s ease-in-out;
    -o-transition: all 0.08s ease-in-out;
    transition: all 0.08s ease-in-out;
}
.like-post-list__container:hover {
    background-color: #f8f8f8;
    cursor: pointer;
}
/* 게시글 제목 */
.like-post-list__title {
    display: flex;
    align-items: center;
}
.like-post-list__title > h3 {
    font-size: 16px;
}
</style>
