<template>
  <div class="wrap">
    <!--헤더-->
    <header class="header header--back">
      <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
        <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
      </a>
      <h2>검색 결과</h2>
    </header>

    <div class="politician-search-view">
      <div class="politician-search">
        <form class="politician-search-form">
          <input
            class="politician-search-form__text-input"
            type="search"
            placeholder="국회의원 검색"
            v-model="politicianInput"
          />
          <button
            class="search-button"
            @click.prevent="searchresultshow(politicianInput)"
          >
            <!--버튼 클릭시 searchresultshow 실행-->
            <img src="@/assets/icon/button.svg" />
          </button>
        </form>
      </div>

      <!--<div class="line"></div> -->
      <div class="search-politician-list-wrap">
        <ul class="search-all-politician-list">
          <li
            class="search-politician"
            v-for="politician in searchPoliticians"
            v-bind:key="politician.politicianID"
            @click="goToPoliticianDetail(politician.politicianID)"
          >
            <!-- 정치인 리스트 출력 이미지, 이름-->
            <div
              class="search-politician-image"
              v-bind:style="{ border: getPoliticianColor(politician) }"
            >
              <img
                :src="
                  'http://teamfrankly.kr/images/' +
                  politician.politicianID +
                  '.png'
                "
              />
            </div>
            <div class="search-politician-name">
              {{ politician.politicianName }}
            </div>
          </li>
        </ul>
      </div>
    </div>
    <Navigation />
  </div>
</template>
<script>
import axios from "axios";
import Navigation from "@/components/Navigation";

export default {
  name: "Search",
  components: {
    Navigation: Navigation
  },
  data() {
    return {
      politicianInput: "",
      searchPoliticians: {},
    };
  },
  methods: {
    searchresultshow(politicianInput) {
      console.log(politicianInput);
      if (politicianInput !== "") {
        //검색어를 입력한 경우
        axios
          .get(`/api/politician/search?searchName=${politicianInput}`)
          .then((response) => {
            this.searchPoliticians = response.data;
          })
          .catch((error) => {
            console.log(error);
          });
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
    getPoliticianColor(politician) {
      if (politician.partyName === "국민의힘") {
        return "3px solid #aa0000";
      } else if (politician.partyName === "더불어민주당") {
        return "3px solid #0d6efd";
      } else if (politician.partyName === "시대전환") {
        return "3px solid #8B00FF";
      } else if (politician.partyName === "정의당") {
        return "3px solid #FFD400";
      } else if (politician.partyName === "기본소득당") {
        return "3px solid #000000";
      }
    },
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";

.politician-search-view {
  padding: 8px 24px;
  margin: 100px auto;
  justify-content: center;
  justify-items: center;
  width: 100%;
  max-width: 540px; /*max-width*/
  height: 100%;
  background-color: #ffffff;
}

.line {
  margin-top: 30px;
  width: 100%;
  max-width: 540px;
  height: 1px;
  box-shadow: #404040 2px;
  background-color: #e4e4e4;
}

/*전체 국회의원*/
.search-all-politician-list {
  margin: 0 auto 0 auto;
  max-width: 540px;
  width: 100%;
  height: 100%;
  display: table;
  text-align: center;
  padding: 0;
  box-shadow: rgba(17, 17, 26, 0.05) 0px 1px 0px,
    rgba(17, 17, 26, 0.1) 0px 0px 8px;
  border-radius: 15px;
}

.search-politician {
  display: inline-table;
  margin: 20px 0;
  padding: 0 24px;
  align-items: center;
}

.search-politician-image {
  width: 75px;
  height: 75px;
  box-sizing: border-box;
  border: 3px solid #00b5ff;
  border-radius: 100%;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.search-politician-image img {
  width: 100%;
  height: 100%;
  border-radius: 100%;
  object-fit: cover;
}

.search-politician-name {
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

.search-politician-list-wrap {
  display: flex;
  margin: 30px auto;
  justify-content: space-evenly;
  align-items: center;
}
</style>
