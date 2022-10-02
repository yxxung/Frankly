<template>
  <body>
    <div class="wrap">
      <SearchBar />

      <div class="political-party-list">
        <h2>대한민국 정당</h2>
        <Slider />
      </div>

      <div class="politician-title">
        <h2>전체 국회의원</h2>
        <h3>가나다 순</h3>
      </div>

      <div class="all-politician-list">
        <div
          class="politician"
          v-for="politician in politicians"
          v-bind:key="politician.politicianID"
        >
        <!-- 정치인 리스트 출력 -->
          <img
            :src="require(`@/assets/politician/${politician.politicianImage}`)"
          />
          <h2>{{ politician.politicianName }}</h2>
        </div>
      </div>

      <PoliticianSearchView v-if="isResultShow" v-bind:searchKeyword="searchKeyword"></PoliticianSearchView>

      <Navigation />
    </div>
  </body>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import Slider from "@/components/Slider.vue";
import PoliticianSearchView from "@/views/Politician/PoliticianSearchView.vue";
import SearchBar from "@/components/SearchBar.vue";
import axios from "axios";

export default {
  name: "Politician",
  components: {
    Navigation: Navigation,
    Slider: Slider,
    PoliticianSearchView: PoliticianSearchView,
    SearchBar: SearchBar
  },
  data() {
    return {
      searchKeyword: '',
      politicians: []
    };
  },
  mounted() {
    this.getPoliticianList()
  },
  methods: {
    getPoliticianList() {
      axios
      .get("/api/infos/all", {
        headers: {}
      })
      .then((response) => {
        console.log("politicians", response.data);
        this.politicians = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
    },
    searchResultShow(searchKeyword) {
      console.log('"',keyword,'"' + ' 검색')
      if (searchKeyword !== '') {
        this.$router.push({
          name: "Politician",
          params: {
            searchKeyword: this.searchKeyword
          },
        }).catch(()=>{});
      } else {
        alert('검색어를 입력해주세요 !')
      }
    },
    searchKeywordChange() {
      this.isResultShow = false
    }
  }
};
</script>

<style>
@import '@/assets/scss/style.scss';

/*국회의원 검색*/
.politician-search {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  top: 0px;
  padding: 8px 24px;
}

.politician-search-form__text-input {
  align-items: center;
  width: 448px;
  height: 38px;
  left: 16px;
  top: 297px;
  padding: 4px 0 4px 14px;

  background: #f5f5f5;
  border-radius: 55px;
}

.politician-search-form__text-input::placeholder {
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 300;
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

/*대한민국 정당*/
.political-party-list {
  padding: 8px 24px;
}

.political-party-list > h2 {
  padding-top: 10px;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 700;
  font-size: 24px;
  line-height: 26px;
  letter-spacing: -0.024em;

  color: #2b2b2b;
}

.politician-title {
  display: flex;
  padding: 8px 24px;
  justify-content: space-between;
}

.politician-title > h2 {
  padding-top: 10px;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 700;
  font-size: 24px;
  line-height: 26px;
  letter-spacing: -0.024em;

  color: #2b2b2b;
}

.politician-title > h3 {
  padding-top: 18px;
  font-family: "Noto Sans KR";
  font-style: normal;
  display: flex;
  font-size: 14px;
  line-height: 26px;
  letter-spacing: -0.024em;
  font-weight: 300;

  color: #818181;
}

.all-politician-list {
  padding: 8px 24px;
}
</style>