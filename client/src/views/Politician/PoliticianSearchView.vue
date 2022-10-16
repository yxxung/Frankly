<template>
  <div class="politician-search-view">
    <div class="politician-search">
      <form class="politician-search-form">
        <input
          class="politician-search-form__text-input"
          type="search"
          placeholder="국회의원 검색"
          v-model="politicianInput"
        />
        <button class="search-button" @click.prevent="searchresultshow(politicianInput)">
          <!--버튼 클릭시 searchresultshow 실행-->
          <img src="@/assets/icon/button.svg" />
        </button>
      </form>
    </div>

    <h2>검색 결과</h2>

    <ul class="search-all-politician-list">
      <li
        class="search-politician"
        v-for="politician in searchPoliticians"
        v-bind:key="politician.politicianID"
        @click="goToPoliticianDetail(politician.politicianID)"
      >
        <!-- 정치인 리스트 출력 이미지, 이름-->
        <div class="search-politician-image">
          <img src="@/assets/politician/정진석.png" />
        </div>
        <div class="search-politician-name">{{ politician.politicianName }}</div>
      </li>
    </ul>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  name: "Search",
  data() {
    return {
      politicianInput: "",
      searchPoliticians: {}
    };
  },
  methods: {
    searchresultshow(politicianInput) {
      console.log(politicianInput);
      if (politicianInput !== "") { //검색어를 입력한 경우
      axios.get(`/api/politician/search?searchName=${politicianInput}`)
      .then((response) => {
        console.log("searchPoliticians", response.data);
        this.searchPoliticians = response.data;
      }).catch((error) => {
        console.log(error);
      })

      } else {
        alert('검색어를 입력해주세요 !')
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
  },
};
</script>

<style>
.politician-search-view {
  padding: 8px 24px;
  margin: 54px auto 0 auto;
  max-width: 540px;  /*max-width*/
  height: 100%;
  background-color: #ffffff;
}

.politician-search-view > h2 {
  padding: 10px;
  margin-top: 20px;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 700;
  font-size: 24px;
  line-height: 26px;
  letter-spacing: -0.024em;

  color: #2b2b2b;
}

/*전체 국회의원*/
.search-all-politician-list {
  margin: 10px auto;
  max-width: 540px;
  display: table;
  padding: 0;
}

.search-politician {
  display: inline-table;
  margin-bottom: 20px;
  padding: 0 24px;
}

.search-politician-image {
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

.search-politician-image img {
  width: 100%;
  height: 100%;
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
</style>