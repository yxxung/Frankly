<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      show: false,
      id: ''
    }
  },
  computed: {
    isLogin() {
      if (sessionStorage.length != 0) {
        return JSON.parse(sessionStorage.getItem("vuex")).userStore.isLogin;
      }
      return false;
    },
  },
  created() {
    if (this.isLogin) {
      this.show = true;
      this.id = JSON.parse(
        sessionStorage.getItem("vuex")
      ).userStore.userID;
    }
  },
  watch: {
    $route(to) {
      if (
        !(
          to.name == "Login" ||
          to.name == "SignUp" ||
          to.name == "findPass"
        )
      ) {
        this.show = true;
      } else {
        this.show = false;
      }
    },
  },
}
</script>

<style>
@import '@/assets/scss/reset.scss';
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

#app {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>