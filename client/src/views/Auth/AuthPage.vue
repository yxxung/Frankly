<template>
  <div class="auth-wrap">

  <div class="auth-page">
    <div class="background-image"></div>
    <div class="fran-logo-wrap">
      <img src="@/assets/icon/franlogo_black.svg" />
      <h2 class="auth-title">Frankly</h2>
      <h2 class="auth-title-2">대한민국 정치 플랫폼 프랭클리</h2>
    </div>

    <div class="auth-login-wrap">
      <div class="loginbox" @click.prevent="$router.push('/signup')">
        <h2>이메일로 회원가입</h2>
      </div>
      <div class="loginbox" @click.prevent="$router.push('/login')">
        <h2>이메일로 로그인</h2>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'AuthPage'
};
</script>

<style>
@import "@/assets/scss/style.scss";

.auth-wrap{
  display: flex;
  width: 100%;
  max-width: 540px;
  justify-items: center;
  justify-content: center;
  margin: 0 auto;
}

.auth-page {
  width: 100%;
  height: 100%;
  margin: 0 auto;
  max-width: 540px;
}

.background-image {
  background-image: url("@/assets/icon/franlogo_background.svg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: absolute;
  width: 100%;
}

.fran-logo-wrap {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  margin-top: 100px;
}

.fran-logo-wrap img {
  position: absolute;
  width: 100px;
  height: 100px;
}

.auth-title {
  position: absolute;
  width: 95px;
  height: 30px;
  top: 210px;

  font-family: "Roboto";
  font-style: normal;
  font-weight: 800;
  font-size: 30px;
  line-height: 30px;

  color: #393939;
}

.auth-title-2 {
  position: absolute;
  width: 170px;
  height: 14px;
  top: 250px;

  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 13px;
  line-height: 14px;
  text-align: center;

  color: #000000;
}

.auth-login-wrap {
  padding: 8px 24px;
  margin-top: 420px;
  align-items: center;
}

.loginbox {
  box-sizing: border-box;
  background-color: #000000;
  width: 100%;
  height: 50px;
  margin: 0 auto 20px auto;
  position: relative;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -1px rgba(0, 0, 0, 0.06);
  cursor: pointer;
}

.loginbox:hover {
  background: #2e2e2e;
}

.loginbox h2 {
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  text-align: center;
  line-height: 46px;
  letter-spacing: -0.024em;
  align-items: center;

  color: #fff;
}
</style>
