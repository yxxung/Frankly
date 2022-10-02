<template>
  <div class="wrap">
    <div class="auth-page">
      <div class="background-image"></div>
      <div class="fran-logo-wrap">
        <img src="@/assets/icon/franlogo_black.svg" />
        <h2 class="auth-title">Frankly</h2>
        <h2 class="auth-title-2">대한민국 정치 플랫폼 프랭클리</h2>
      </div>

      <div class="auth-login-wrap">
        <div class="loginbox">
          <img src="@/assets/icon/kakao_talk.svg" />
          <h2>카카오로 시작하기</h2>
        </div>
        <div class="loginbox">
          <img src="@/assets/icon/google.svg" />
          <h2>구글로 시작하기</h2>
        </div>
        <div class="loginbox" @click.prevent="$router.push('/Login')">
          <img src="@/assets/icon/Mobile-phone.svg" />
          <h2>이메일로 시작하기</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
@import "@/assets/scss/style.scss";

.auth-content {
  padding: 8px 24px;
  position: relative;
  margin: 0 auto;
  max-width: 540px;

}

.background-image {
  background-image: url("@/assets/icon/franlogo_background.svg");
  background-size: cover;
  transform: rotate(-135deg);
  position: absolute;
  width: 330px;
  height: 330px;
  margin: auto;
}

.fran-logo-wrap {
  padding: 8px 24px;
  position: relative;
  text-align: center;
}

.fran-logo-wrap img {
  position: absolute;
  width: 77px;
  height: 77px;
}

.auth-title {
  position: absolute;
  width: 85px;
  height: 30px;
  left: 145px;
  top: 235px;

  font-family: "Roboto";
  font-style: normal;
  font-weight: 700;
  font-size: 26px;
  line-height: 30px;
  letter-spacing: -0.005em;

  color: #393939;
}

.auth-title-2 {
  position: absolute;
  width: 127px;
  height: 14px;
  left: 125px;
  top: 269px;

  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 10px;
  line-height: 14px;
  text-align: center;

  color: #000000;
}

.auth-login-wrap {
  padding: 8px 24px;
  margin-top: 400px;
  align-items: center;
}

.loginbox {
  box-sizing: border-box;
  border: 2px solid #000000;
  width: 380px;
  height: 46px;
  margin: 0 auto 20px auto;
  position: relative;
}

.loginbox img {
    position: absolute;
    width: 30px;
    height: 30px;
}

.loginbox h2 {
  left: 60px;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  text-align: center;
  letter-spacing: -0.024em;
  vertical-align: middle;

  color: #000000;
}
</style>