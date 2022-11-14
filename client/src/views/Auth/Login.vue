<template>
  <div class="wrap">
    <!--헤더-->
    <header class="header header--back">
      <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
        <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
      </a>
    </header>

    <div class="sign-up-title">
      <h3>로그인</h3>
    </div>

    <form class="sign-up-form">
      <!--        이메일-->
      <label>
        <p class="sign-up-form__input-info">이메일</p>
        <input
          class="sign-up-form__text-input"
          type="email"
          placeholder="example@gmail.com"
          v-model="userEmail"
        />
        <p class="sign-up-form__error-message">
          올바른 이메일 형식을 입력해주세요.
        </p>
      </label>

      <!--        비밀번호-->
      <label>
        <p class="sign-up-form__input-info">비밀번호</p>
        <input
          class="sign-up-form__text-input"
          type="password"
          placeholder="대소문자, 숫자, 특수문자 포함 8~16자리"
          maxlength="16"
          v-model="userPassword"
        />
        <p class="sign-up-form__error-message">
          대소문자, 숫자, 특수문자 포함 8~16자리
        </p>
      </label>

      <!--        이메일 저장, 비밀번호 찾기-->
      <div class="log-in__check">
        <div class="remember-email">
          <input type="checkbox" id="remember-email" class="input-checkbox" />
          <label for="remember-email"></label>
          이메일 저장
        </div>
        <a href="#">비밀번호 찾기</a>
      </div>

      <button class="sign-up-form__button" @click.prevent="confirm()">
        로그인
      </button>
    </form>
  </div>
</template>

<script>
import { login, findById } from "@/js/user.js";
import { validateEmail, validatePassword } from "@/commons/validation.js"

export default {
  name: "Login",
  data() {
    return {
      userEmail: "",
      userPassword: "",
    };
  },
  methods: {
    async confirm() {
      const user = {
        email: this.userEmail,
        password: this.userPassword,
      };
      login(user, (response) => {
        console.log("userConfirm", response);
        if (response.status === 200) {
          let token = response.data.token;
          let userID = response.data.userID;
          this.$store.commit("userStore/SET_IS_LOGIN", true);
          this.$store.commit("userStore/SET_IS_LOGIN_ERROR", false);
          this.$store.commit("userStore/SET_USER_ID", userID);

          sessionStorage.setItem("token", token);
          sessionStorage.setItem("userID", userID);

          this.$store.dispatch("userStore/getUserInfo", userID);
          this.$router.push({ name: "Home"});
        } else {
          alert('아이디 또는 비밀번호가 일치하지 않습니다.')
          this.$store.commit("userStore/SET_IS_LOGIN", false);
          this.$store.commit("userStore/SET_IS_LOGIN_ERROR", true);
        }
      },
      (error) => {
        console.error(error);
        alert('아이디 또는 비밀번호가 일치하지 않습니다.')
      });
    },
  },
};
</script>

<style>
.sign-up-title {
  padding: 0 24px;
  height: 48px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.sign-up-title > h3 {
  font-size: 24px;
}
.sign-up-title > h3 > span {
  font-size: 16px;
}
.sign-up-title p {
  font-family: "Roboto", sans-serif;
  font-size: 16px;
  font-weight: bold;
}
.sign-up-form {
  margin-top: 24px;
  padding: 0 24px;
}
.sign-up-form > label {
  margin-top: 16px;
  display: block;
}
/*
이메일, 비밀번호 입력 input / button
*/
.sign-up-form__text-input[type="email"],
.sign-up-form__text-input[type="password"] {
  box-sizing: border-box;
  padding-left: 8px;
  width: 100%;
  height: 48px;
  cursor: text;
  background-color: #fafafa;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
}
.sign-up-form__text-input[type="email"]:focus-visible,
.sign-up-form__text-input[type="password"]:focus-visible {
  outline: 0;
  box-shadow: inset 0 -2px 0 #000000;
}
.sign-up-form__input-info {
  margin: 2px 0;
  font-size: 14px;
  color: #a9a9a9;
}
.sign-up-form__error-message {
  display: none;
}
.sign-up-form--error > .sign-up-form__error-message {
  margin-top: 4px;
  display: block;
  font-size: 14px;
  color: #da8282;
}
.sign-up-form--error > input {
  outline: 0;
  box-shadow: inset 0 -2px 0 #ff3030;
}
.sign-up-form__button {
  margin-top: 24px;
  width: 100%;
  height: 48px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  color: white;
  background-color: black;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
}
.sign-up-form__button:hover {
  background-color: #343434;
}
.sign-up-form__button:disabled {
  background-color: #c5c5c5;
}
/*
회원가입 지역 선택 dropdown
*/
.dropdown-container {
  width: 100%;
  display: flex;
  justify-content: space-between;
}
.sign-up-form__dropdown {
  box-sizing: border-box;
  padding-left: 8px;
  height: 48px;
  background-color: #fafafa;
}
.dropdown-container > .sign-up-form__dropdown:nth-child(2) {
  width: 100%;
}
.dropdown-container > .sign-up-form__dropdown:nth-child(1) {
  margin-right: 16px;
}
.sign-up-form__dropdown:focus-visible {
  outline: 0;
  box-shadow: inset 0 -2px 0 #000000;
}
.form__check {
  margin-top: 24px;
}
.form__check > ul > li {
  padding: 8px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.check-box-line {
  border-bottom: 1px solid #bfbfbf;
}
.log-in__check {
  margin: 16px 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 14px;
}
.remember-email {
  display: flex;
  align-items: center;
}
.remember-email label {
  margin-right: 8px;
}
</style>
