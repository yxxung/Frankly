<template>
  <div class="wrap">
    <!--헤더-->
    <header class="header header--back">
      <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
        <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
      </a>
      <div class="header-right-icon">
        <a class="icon-button-56">
          <img src="@/assets/icon/Bookmark.svg" alt="북마크" />
        </a>
        <a class="icon-button-56">
          <img src="@/assets/icon/Other2.svg" alt="더보기" />
        </a>
      </div>
    </header>

    <div class="politician-info">
      
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
@import "@/assets/scss/style.scss";
</style>