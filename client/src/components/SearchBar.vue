<template>
  <div>
    <div class="politician-search">
      <form class="politician-search-form">
        <input
          class="politician-search-form__text-input"
          type="search"
          placeholder="국회의원 검색"
          v-model="politicianInput"
        />
        <button class="search-button" type="submit" @click="searchResultShow">
          <!--버튼 클릭시 searchresultshow 실행-->
          <img src="@/assets/icon/button.svg" />
        </button>
      </form>
    </div>
    <Search v-bind:propPoliticianInput="politicianInput"></Search>
  </div>
</template>

<script>
import Search from "@/views/Politician/PoliticianSearchView.vue";
import axios from "axios";

export default {
  components: {
    Search,
  },
  data() {
    return {
      politicianInput: "",
      searchPoliticians: []
    };
  },
  methods: {
    searchResultShow() {
      this.searchPoliticians = []
      if (politicianInput !== "") { //검색어를 입력한 경우
      axios.get(`/api/politician/` + this.politicianInput)
        .then(response => {
          if(response.data instanceof Array) {
            this.searchPoliticians = response.data
          }else{
            this.searchPoliticians.push(response.data)
          }
          console.log(this.searchPoliticians)
        })
      } else {
        alert('검색어를 입력해주세요 !')
      }
    },
    doMouseOver() {
      this.$router.push({
        path: "/search",
      });
    },
  },
};
</script>

<style>
/*국회의원 검색*/
.politician-search {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  padding: 8px 24px;
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