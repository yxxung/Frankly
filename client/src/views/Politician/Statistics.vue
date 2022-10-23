<template>
<div class="wrap">
  <!--헤더-->
    <header class="header header--back">
      <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
        <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
      </a>
      <h2>통계</h2>
    </header>


</div>
</template>
<script>
import axios from 'axios';

export default {
  name: "Statistics",
  data() {
    return {

    };
  },

};
</script>

<style>
@import "@/assets/scss/style.scss";

</style>