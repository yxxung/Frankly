<template>
  <div class="politician-search">
    <form class="politician-search-form">
      <input
        class="politician-search-form__text-input"
        type="search"
        placeholder="국회의원 검색"
        @click.prevent="checkClick"
      />
      <button class="search-button" type="submit">
        <img src="@/assets/icon/button.svg" />
      </button>
    </form>
  </div>
</template>

<script>
import Search from "@/views/Politician/PoliticianSearchView.vue";
import axios from "axios";
export default {
  components: {
    Search,
  },
  methods: {
    checkClick() {
      this.$router.push({
        path: "/Search",
      });
    },
  }
};
</script>

<style>
/*국회의원 검색*/
.politician-search {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  margin-top: -30px;
}
.politician-search-form__text-input {
  align-items: center;
  width: 440px;
  height: 38px;
  left: 16px;
  top: 297px;
  padding: 4px 0 4px 18px;
  border: none;
  outline: none;
  background: #f5f5f5;
  border-radius: 55px;
}
.politician-search-form__text-input::placeholder {
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  letter-spacing: -0.024em;
  color: #a9a9a9;
}
.search-button img {
  width: 25px;
  height: 25px;
  margin-left: 14px;
  vertical-align: middle;
}
.politician-search-view {
  padding: 8px 24px;
  max-width: 540px;
  height: 100%;
  top: 100px;
}
.politician-search-view > h2 {
  padding-top: 10px;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 700;
  font-size: 24px;
  line-height: 26px;
  letter-spacing: -0.024em;
  color: #2b2b2b;
}
</style>
