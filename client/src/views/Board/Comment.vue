<template>
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
    <button class="enter-comment__submit" @click="onClickCommentSubmit()">
      <img src="@/assets/icon/Comment.svg" alt="댓글 전송 버튼" />
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {

    }
  },
  methods: {
    //댓글 입력
    onClickCommentSubmit() {
      
    }
  },
};
</script>

<style>
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