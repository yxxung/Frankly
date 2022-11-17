<template>
  <div class="wrap">
    <div class="bookmark-politician-list-wrap">
      <ul class="bookmark-politician-list">
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
          <div class="bookmark-politician-name">{{ politician.politicianName }}</div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "BookmarkPolitician",
  data() {
    return {
      politicians: []
    };
  },
  mounted() {
    this.getPoliticianList();
  },
  methods: {
    getPoliticianList() {
      axios
        .get("/api/likeBookmark/all", {
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
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";

/*전체 국회의원*/
.bookmark-politician-list {
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

.bookmark-politician-list-wrap {
  display: flex;
  margin: auto;
  justify-content: space-evenly;
  align-items: center;
}
</style>
