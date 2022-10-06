<template>
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
          나는 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        </div>
      </li>

      <!--대댓글 class에 comments__box--reply 추가-->
      <!--
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
    </ul>-

    <div class="comments__plus">
      <button class="comments__plus-button">댓글 32개 더보기...</button>
    </div>
  </div> -->
</template>

<script>
export default {
    data() {
        return {
            
        }
    },
};
</script>

<style>
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
</style>