<template>
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

    <ul class="all-politician-list">
      <li
        class="politician"
        v-for="politician in politicians"
        v-bind:key="politician.politicianID"
        @click="goToPoliticianDetail(politician.politicianID)"
      >
        <!-- 정치인 리스트 출력 이미지, 이름-->
        <div class="politician-image">
          <img src="@/assets/politician/정진석.png" />
        </div>
        <div class="politician-name">{{ politician.politicianName }}</div>
      </li>
    </ul>

    <PoliticianSearchView
      v-if="isResultShow"
      v-bind:searchKeyword="searchKeyword"
    ></PoliticianSearchView>

    <Navigation />
  </div>
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
    SearchBar: SearchBar,
  },
  data() {
    return {
      searchKeyword: "",
      politicians: [],
    };
  },
  mounted() {
    this.getPoliticianList();
  },
  methods: {
    getPoliticianList() {
      axios
        .get("/api/politician/all", {
          headers: {},
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
      console.log('"', keyword, '"' + " 검색");
      if (searchKeyword !== "") {
        this.$router
          .push({
            name: "Politician",
            params: {
              searchKeyword: this.searchKeyword,
            },
          })
          .catch(() => {});
      } else {
        alert("검색어를 입력해주세요 !");
      }
    },
    goToPoliticianDetail(politicianID) {
      this.$router.push({
        name: "PoliticianDetail",
        params: {
          politicianID: politicianID,
        },
      });
    },
    searchKeywordChange() {
      this.isResultShow = false;
    },
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";

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

/*전체 국회의원*/
.all-politician-list {
  margin: 10px auto;
  width: 100%;
  max-width: 520px;
  display: table;
}

.politician {
  display: inline-table;
  margin-bottom: 20px;
  padding: 0 20px;
}

.politician-image {
  width: 75px;
  height: 75px;
  box-sizing: border-box;
  border: 3px solid #00B5FF;
  border-radius: 100%;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.politician-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.politician-name {
  margin: 5px auto;
  font-size: 16px;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 500;
  color: #000000;
  display: flex;
        justify-content: center;
        align-items: center;
}
</style>