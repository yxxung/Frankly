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
        <div class="email-login">
            <img src="" />
            <h2>카카오로 시작하기</h2>
        </div>
        <div class="email-login">
            <img src="" />
            <h2>구글로 시작하기</h2>
        </div>
        <div class="email-login" @click.prevent="$router.push('/Login')">
            <img src="" />
            <h2>휴대전화로 시작하기</h2>
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
}

.background-image {
  background-image: url("@/assets/icon/franlogo_background.svg");
  transform: rotate(-135deg);
  position: absolute;
  width: 330px;
  height: 330px;
  margin: auto;
}
</style>