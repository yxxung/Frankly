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
        <div class="post-header__kategorie">커뮤니티 > {{ regionName }}</div>
        <h3 class="post-header__title">{{ title }}</h3>
        <div class="post-header__info">
          <div class="post-header__writer">{{ author }}</div>
          <div class="post-header__reg-date">{{ regDate }}</div>
        </div>
      </div>

      <!--내용-->
      <article class="post-content">
        <p>{{ content }}</p>
      </article>

      <!--좋아요, 싫어요-->
      <div class="post-like">
        <button>좋아요</button>
        <button>싫어요</button>
      </div>

      <!--댓글-->
      <div class="comments">
        <ul>
          <li class="comments__box">
            <div class="comments__info">
              <div class="comments__info-left">
                <img src="@/assets/icon/Anonymous_user.svg" alt="익명유저" />
                <h6>익명</h6>
                <span class="comments__info__date">36분전</span>
              </div>

              <div class="comments__info-right">
                <button class="icon-button-24">
                  <img src="@/assets/icon/Other1.svg" alt="더보기" />
                </button>
              </div>
            </div>
            <div class="comments__text">
              나는
              ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
            </div>
          </li>

          <li class="comments__box">
            <div class="comments__info">
              <div class="comments__info-left">
                <img src="@/assets/icon/Anonymous_user.svg" alt="익명유저" />
                <h6>익명</h6>
                <span class="comments__info__date">36분전</span>
              </div>

              <div class="comments__info-right">
                <button class="icon-button-24">
                  <img src="@/assets/icon/Other1.svg" alt="더보기" />
                </button>
              </div>
            </div>
            <div class="comments__text">ㅋㅋㅋㅋㅋ웃기</div>
          </li>

          <!--대댓글 class에 comments__box--reply 추가-->
          <li class="comments__box comments__box--reply">
            <div class="comments__info">
              <div class="comments__info-left">
                <img src="@/assets/icon/Anonymous_user.svg" alt="익명유저" />
                <h6>익명</h6>
                <span class="comments__info__date">36분전</span>
              </div>

              <div class="comments__info-right">
                <button class="icon-button-24">
                  <img src="@/assets/icon/Other1.svg" alt="더보기" />
                </button>
              </div>
            </div>
            <div class="comments__text">
              엌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
            </div>
          </li>
        </ul>

        <div class="comments__plus">
          <button class="comments__plus-button">댓글 32개 더보기...</button>
        </div>
      </div>
    </div>

    <!--댓글 입력창-->
    <div class="enter-comment">
      <textarea
        name="comment"
        id="comment"
        cols="30"
        rows="10"
        placeholder="댓글 입력..."
        class="enter-comment__textarea"
      ></textarea>
      <button class="enter-comment__submit">
        <img src="@/assets/icon/Comment.svg" alt="댓글 전송 버튼" />
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

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
        author: "",
      },
    };
  },
  created() {
    let boardID = this.$route.params.boardID;
    axios.get(`/api/boards/${boardID}`).then((response) => {
      this.DetailData.boardID = response.data.boardID;
      this.DetailData.boardID = response.data.boardID;
      this.DetailData.boardID = response.data.boardID;
      this.DetailData.boardID = response.data.boardID;
      this.DetailData.boardID = response.data.boardID;
      this.DetailData.boardID = response.data.boardID;
    });
  },
  methods: {
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
  height: 64px;
  display: flex;
  justify-content: center;
  background-color: rgb(255, 255, 255);
}

.enter-comment__textarea {
  margin: 8px 16px 0;
  padding: 8px 40px 0 24px;
  height: 32px;
  border-radius: 24px;
  font-family: "Noto Sans KR", sans-serif;
  font-size: 16px;
  color: #2b2b2b;
  background-color: #f8f8f8;
  outline: 0;
  border: 0;
}

.enter-comment__textarea:focus-visible {
  outline: 0;
  /*box-shadow: 0 0 0 2px #000 inset;*/
}

.enter-comment__submit {
  position: absolute;
  top: 8px;
  right: 16px;
  width: 40px;
  height: 40px;
  border-radius: 40px;
}

.enter-comment__submit:hover {
  background-color: #cccccc;
}
</style>