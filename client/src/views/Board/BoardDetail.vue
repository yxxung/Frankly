<template>
  <div>
    <div class="wrap">
      <!--헤더-->
      <header class="header header--back">
        <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
          <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
        </a>
        <div class="header-right-icon">
          <a class="icon-button-56">
            <img src="@/assets/icon/Share.svg" alt="공유하기" />
          </a>
          <a class="icon-button-56">
            <img src="@/assets/icon/Other2.svg" alt="더보기" />
          </a>
        </div>
      </header>

      <!--타이틀-->
      <div class="post-header">
        <div class="post-header__kategorie">커뮤니티 > {{ DetailData.region }}</div>
        <h3 class="post-header__title">{{ DetailDatatitle }}</h3>
        <div class="post-header__info">
          <div class="post-header__writer">{{ DetailData.userID }}</div>
          <div class="post-header__reg-date">{{ elapsedText(DetailData.regDate) }}</div>
        </div>
      </div>

      <!--내용-->
      <article class="post-content">
        <p>{{ DetailData.content }}</p>
      </article>

      <!--좋아요, 싫어요-->
      <div class="post-like">
        <button><img src="@/assets/icon/Like.svg"></button>
        <button><img src="@/assets/icon/Unlike.svg"></button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import dateformat from "@/commons/dateformat.js";

export default {
  name: "BoardDetail",
  data() {
    return {
      DetailData: {
        boardID: "",
        title: "",
        content: "",
        regDate: "",
        region: "",
        userID: "",
        marked: "",
      },
    };
  },
  created() {
    const boardID = this.$route.params.boardID;
    axios.get(`/api/boards/${boardID}`).then((response) => {
      this.DetailData.boardID = response.data.boardID;
      this.DetailData.title = response.data.title;
      this.DetailData.content = response.data.content;
      this.DetailData.regDate = response.data.regDate;
      this.DetailData.region = response.data.region;
      this.DetailData.userID = response.data.userID;
      this.DetailData.marked = response.data.marked;
      console.log(boardID);
    });
  },
  methods: {
    //date format 변환
    elapsedText(date) {
      return dateformat.elapsedText(new Date(date));
    },
    // 특정인덱스인 값을 삭제할 때 사용함
    deleteData() {
      data.splice(this.index, 1);
      this.$router.push({
        path: "/",
      });
    },
    // 특정인덱스인 값을 수정할 때 사용함
    updateData() {
      this.$router.push({
        name: "Create",
        params: {
          boardID: this.index,
        },
      });
    },
    //댓글 작성
    createReply(reply) {
      axios
        .post(
          `${BACK_URL}/boards/replys`,
          {
            boardId: this.detailData.boardId,
            commentContent: comment,
          },
          {
            headers: { "jwt-auth-token": this.$cookies.get("token") },
          }
        )
        .then((response) => {
          // console.log(response);
          if (response.status === 200) {
            alert("댓글이 작성되었습니다!");
            axios
              .get(`${BACK_URL}/boards/${this.detailData.boardId}`)
              .then((response) => {
                this.detailData.comments = response.data.board.comments;
              });
          }
        })
        .catch((error) => {
          alert(error);
        });
    },
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";
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