<template>
    <body>
        <div class="wrap">
            <!--헤더-->
            <header class="header header--back">
                <a class="icon-button-56 header__back-button" href="/Home">
                    <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기">
                </a>
                <a class="icon-button-56 header-right-icon" href="index.html">
                    <img src="@/assets/icon/Settings.svg" alt="설정">
                </a>
            </header>

            <div class="mypage-info">
                <div class="mypage-info-image">
                  <img src="" alt="">
                </div>
                <h2 class="mypage-info-name">익명1</h2>
                <h4 class="mypage-info-region">충남 아산시을1</h4>
            </div>

            <div class="mypage-bookmark">
              <h2>북마크 국회의원</h2>
              <div class="mypage-bookmark-politician"></div>
            </div>

            

            <Navigation />
        </div>
    </body>
</template>

<script>
import Navigation from '@/components/Navigation.vue'
export default {
  name: 'Mypage',
  components: {
    'Navigation': Navigation
  }
}
</script>

<style lang="style.scss">
@import "../assets/scss/style.scss";

</style>