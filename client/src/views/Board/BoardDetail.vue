<template>
  <div class="wrap">
    <!--헤더-->
    <header class="header header--back">
      <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
        <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
      </a>
      <div class="header-right-icon">
        <!--<a class="icon-button-56">
          <img src="@/assets/icon/Share.svg" alt="공유하기" />
        </a>
        <a class="icon-button-56" @click="edit_show = true">
          <img src="@/assets/icon/Other2.svg" alt="더보기" />
        </a>-->
        <a class="icon-button-56">
          <b-dropdown
            size="xs"
            variant="link"
            toggle-class="text-decoration-none"
            no-caret
          ><template #button-content>
            <img src="@/assets/icon/Other2.svg" alt="더보기" />
            <span class="visually-hidden"></span>
          </template>
            <b-dropdown-item @click="updateBoard(DetailData.boardID)">수정</b-dropdown-item>
            <b-dropdown-item @click="deleteBoard">삭제</b-dropdown-item>
          </b-dropdown></a>
      </div>
    </header>

    <!--타이틀-->
    <div class="post-header">
      <div class="post-header__kategorie">
        커뮤니티 > {{ DetailData.region }}
      </div>
      <h3 class="post-header__title">{{ DetailData.title }}</h3>
      <div class="post-header__info">
        <div class="post-header__writer">익명</div>
        <div class="post-header__reg-date">
          {{ elapsedText(DetailData.boardRegDate) }}
        </div>
      </div>
    </div>

    <!--내용-->
    <article class="post-content">
      <p>{{ DetailData.content }}</p>
    </article>

    <!--좋아요-->
    <div class="post-like">
      <button @click="(marked = !marked), changeLike(DetailData.boardID)">
        <img src="@/assets/icon/Like.svg" v-if="marked === false" />
        <img src="@/assets/icon/Like_active.svg" v-if="marked === true" />
      </button>
      <span>{{ DetailData.marked }}</span>
    </div>

    <!--댓글-->
    <div class="comments">
      <ul>
        <li
          class="comments__box"
          v-for="reply in replys"
          v-bind:key="reply.replyID"
        >
          <div class="comments__info">
            <div class="comments__info-left">
              <img src="@/assets/icon/Anonymous_user.svg" alt="익명유저" />
              <h6>익명{{ reply.replyID }}</h6>
              <span class="comments__info__date">{{
                elapsedText(reply.replyRegDate)
              }}</span>
            </div>

            <div class="comments__info-right">
              <button class="icon-button-24">
                <img src="@/assets/icon/Other1.svg" alt="더보기" />
              </button>
            </div>
          </div>
          <div class="comments__text">{{ reply.reply }}</div>
        </li>
      </ul>
    </div>

    <!--댓글 입력창-->
    <div class="enter-comment">
      <textarea
        placeholder="댓글 입력..."
        class="enter-comment__textarea"
        v-model="replyInput"
      ></textarea>
      <button
        class="enter-comment__submit"
        @click.prevent="
          createReply(DetailData.boardID), countReply(this.cntReply)
        "
      >
        <img src="@/assets/icon/Comment.svg" alt="댓글 전송 버튼" />
      </button>
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
        boardRegDate: "",
        region: "",
        userID: "",
        marked: "", //board db의 좋아요
      },
      replys: [], //댓글 axios get
      replyInput: "", //댓글 입력
      marked: false, //좋아요
      cntMarked: null, //좋아요 개수
      edit_show: false,
    };
  },
  created() {
    const boardID = this.$route.params.boardID;
    axios.get(`/api/boards/${boardID}`).then((response) => {
      this.DetailData.boardID = response.data.boardID;
      this.DetailData.title = response.data.title;
      this.DetailData.content = response.data.content;
      this.DetailData.boardRegDate = response.data.boardRegDate;
      this.DetailData.region = response.data.region;
      this.DetailData.userID = response.data.userID;
      this.DetailData.marked = response.data.marked;
    });
    axios.get(`/api/replys/${boardID}/replyList`).then((response) => {
      this.replys = response.data;
      console.log(response.data);
    });
    this.cntMarked = this.DetailData.marked; //좋아요 개수 저장
  },
  methods: {
    //date format 변환
    elapsedText(date) {
      return dateformat.elapsedText(new Date(date));
    },
    // 게시글 삭제
    deleteBoard() {
      const boardID = this.$route.params.boardID;
      axios.delete(`api/boards/delete/${boardID}`)
        .then((response) => {
          if(response.status === 200){
            alert("게시글이 삭제되었습니다.");
          }
          this.$router.go(-1);
        })
        .catch(() =>{
          console.log("삭제 요청 실패")
        })
    },
    // 게시글 수정
    updateBoard(boardID) {
      this.$router.push({
        name: "WriteBoard",
        params: {
          boardID: boardID
        },
      });
    },
    //댓글 생성
    createReply(boardID) {
      if (this.replyInput.trim()) {
        //앞 뒤 공백제거
        axios
          .post("/api/replys/create", {
            boardID: boardID,
            reply: this.replyInput,
          })
          .then((response) => {
            console.log(response);
            this.$router.go();
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    async changeLike(boardID) {
      //좋아요가 안눌러진 상태에서 좋아요를 누를 때
      if (this.marked) {
        // 해당 게시글의 좋아요 개수 1 증가시킨 걸로 수정 (put)
        this.DetailData.marked += 1;
        this.cntMarked = this.DetailData.marked;
        axios
          .put(`/api/boards/update/${boardID}`, {
            title: this.DetailData.title,
            content: this.DetailData.content,
            marked: this.cntMarked,
          })
          .then((response) => {
            console.log(response);
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";
/*
게시글 페이지
*/
.post-header {
  padding: 0px 16px;
}
.post-header__kategorie {
  padding: 4px 0;
  font-size: 13px;
  color: #696969;
}
.post-header__title {
  font-size: 20px;
  color: #2b2b2b;
}
.post-header__info {
  margin: 12px 0;
  display: flex;
  justify-content: space-between;
}
.post-header__writer {
  font-size: 13px;
  color: #696969;
}
.post-header__reg-date {
  font-size: 13px;
  color: #696969;
}
.post-content {
  padding: 0px 16px;
}
/*게시글 좋아요*/
.post-like {
  padding: 24px 16px;
}
.post-like button {
  margin-right: 8px;
  background-color: #ffffff;
  width: 28px;
  height: 28px;
}
.post-like button img {
  background-color: #fff;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.post-like span {
  font-family: "Roboto";
  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  text-align: right;
  letter-spacing: -0.024em;
  color: #646464;
}
/*댓글*/
.comments ul {
  padding-left: 0;
}
.comments__box {
  padding: 8px 16px;
  border-bottom: 1px solid #f6f6f6;
}
.comments__box--reply {
  padding-left: 32px;
  position: relative;
}
.comments__box--reply:before {
  position: absolute;
  top: 12px;
  left: 16px;
  content: "";
  display: block;
  width: 14px;
  height: 14px;
  background-image: url("@/assets/icon/Reply.svg");
  background-repeat: no-repeat;
}
.comments__info {
  margin-bottom: 4px;
  display: flex;
  justify-content: space-between;
}
.comments__info h6 {
  padding: 0 12px 0 8px;
  font-size: 14px;
  color: #696969;
}
.comments__info-left {
  display: flex;
  align-items: center;
}
.comments__info__date {
  font-size: 12px;
  color: #696969;
}
.comments__plus {
  padding: 16px;
}
.comments__plus-button {
  padding: 14px 0;
  width: 100%;
  border-radius: 12px;
  color: #424242;
  background-color: #f1f1f1;
}
.comments__plus-button:hover {
  background-color: #e7e7e7;
}
/*댓글 입력창*/
.enter-comment {
  position: fixed;
  bottom: 0;
  width: 100%;
  max-width: 540px;
  height: 64px;
  display: flex;
  justify-content: center;
  background-color: rgb(255, 255, 255);
}
.enter-comment__textarea {
  height: 30px;
  padding-left: 20px;
  padding-top: 8px;
  border-radius: 24px;
  font-family: "Noto Sans KR", sans-serif;
  font-size: 16px;
  color: #2b2b2b;
  background-color: #f8f8f8;
  outline: none;
  border: none;
  resize: none;
  box-sizing: unset;
}
.enter-comment__textarea:focus-visible {
  outline: none;
  /*box-shadow: 0 0 0 2px #000 inset;*/
}
.enter-comment__submit {
  position: absolute;
  right: 0px;
  width: 42px;
  height: 40px;
  border-radius: 40px;
}
.enter-comment__submit:hover {
  background-color: #cccccc;
}
.dropdown-menu {
  min-width: 1rem !important;
}
</style>
