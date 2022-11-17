<template>
  <div class="wrap">
    <SearchBar />

    <div class="political-party-list">
      <h2>대한민국 원내 정당</h2>
      <Slider />
    </div>

    <div class="politician-title">
      <h2>전체 국회의원</h2>
      <h3
        v-if="politicianOrder === 1"
        v-on:click="politicianOrdering"
        style="cursor: pointer"
      >
        가나다 순
      </h3>
      <h3
        v-if="politicianOrder === 2"
        v-on:click="politicianOrdering"
        style="cursor: pointer"
      >
        정당 순
      </h3>
      <h3
        v-if="politicianOrder === 3"
        v-on:click="politicianOrdering"
        style="cursor: pointer"
      >
        지역구 순
      </h3>
    </div>

    <div class="politician-list-wrap">
      <ul class="all-politician-list">
        <li
          class="politician"
          v-for="politician in politicians"
          v-bind:key="politician.politicianID"
          @click="
            goToPoliticianDetail(politician.politicianID),
              countPoliticianClick(politician.politicianID)
          "
        >
          <!-- 정치인 리스트 출력 이미지, 이름-->
          <div
            class="politician-image"
            v-bind:style="{ border: getPoliticianColor(politician) }"
          >
            <img
              :src="
                'https://teamfrankly.kr/images/' +
                politician.politicianID +
                '.png'
              "
            />
          </div>
          <div class="politician-name">{{ politician.politicianName }}</div>
          <div class="politician-region" v-if="politicianOrder === 3">
            {{ politician.regionName }}
          </div>
          <div class="politician-region" v-if="politicianOrder === 2">
            {{ politician.partyName }}
          </div>
        </li>
      </ul>
    </div>

    <Navigation />
  </div>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import Slider from "@/components/Slider.vue";
import SearchBar from "@/components/SearchBar.vue";
import axios from "axios";
export default {
  name: "Politician",
  components: {
    Navigation: Navigation,
    Slider: Slider,
    SearchBar: SearchBar,
  },
  data() {
    return {
      searchKeyword: "",
      politicians: [],
      border: "3px solid #0d6efd",
      politicianOrder: 1,
      clickCount: 0
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
          this.politicians = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    goToPoliticianDetail(politicianID) {
      this.$router.push({
        name: "PoliticianDetail",
        params: {
          politicianID: politicianID,
        },
      });
    },
    countPoliticianClick(politicianID) {
      clickCount += 1;
      axios
        .post(`/api/politician/${politicianID}`, {
          viewCount: clickCount,
        })
        .then((response) => {})
        .catch((error) => {
          console.log(error);
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
    politicianOrdering() {
      this.politicianOrder++;
      if (this.politicianOrder === 4) this.politicianOrder = 1;

      if (this.politicianOrder === 1) {
        this.politicians.sort((a, b) => {
          if (a.politicianName > b.politicianName) return 1;
          else return -1;
        });
      } else if (this.politicianOrder === 2) {
        this.politicians.sort((a, b) => {
          if (a.partyName > b.partyName) return 1;
          else return -1;
        });
      } else if (this.politicianOrder === 3) {
        // let resultArray = this.politicians;
        let politicianJson;
        for (politicianJson of this.politicians) {
          let index = -1;
          index = politicianJson.regionName.indexOf("시");
          if (index === -1) index = politicianJson.regionName.indexOf("군");
          if (index === -1) index = politicianJson.regionName.indexOf("구");

          if (politicianJson.regionName.length > 11) {
            politicianJson.regionName =
              politicianJson.regionName.substr(0, index + 1) + " 등";
          } else if (politicianJson.regionName.length > 9) {
            politicianJson.regionName = politicianJson.regionName.substr(
              0,
              index + 1
            );
          }
        }
        this.politicians.sort((a, b) => {
          if (a.regionName > b.regionName) return 1;
          else return -1;
        });
      }
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
  margin: 0 auto 0 auto;
  width: 100%;
  max-width: 540px;
  display: table;
  text-align: center;
  padding: 0;
}
.politician {
  display: inline-table;
  /*align-items: center;*/
  margin-bottom: 20px;
  padding: 0 5%;
}
.politician-image {
  width: 75px;
  height: 75px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  box-sizing: border-box;
  border: 3px solid #0d6efd;
  border-radius: 100%;
}

.politician-image img {
  border-radius: 100%;
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
.politician-region {
  margin: 5px auto;
  font-size: 10px;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 500;
  color: #000000;
  display: flex;
  justify-content: center;
  align-items: center;
}

.politician-list-wrap {
  display: flex;
  margin: auto;
  justify-content: space-evenly;
  align-items: center;
}
</style>
