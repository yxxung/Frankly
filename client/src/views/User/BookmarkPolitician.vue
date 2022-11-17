<template>
    <div class="bookmark-politician-list-wrap">
      <ul class="bookmark-politician-list">
        <li
          class="bookmark-politician"
          v-for="bookmark in bookmarkPoliticians"
          v-bind:key="bookmark.bookmarkID"
          @click="
            goToPoliticianDetail(bookmark.politicianID)
          "
        >
          <!-- 정치인 리스트 출력 이미지, 이름-->
          <div
            class="bookmark-politician-image"
            v-bind:style="{ border: getPoliticianColor(bookmark) }"
          >
            <img
              :src="
                'https://teamfrankly.kr/images/' +
                bookmark.politicianID +
                '.png'
              "
            />
          </div>
          <div class="bookmark-politician-name">{{ bookmark.politicianName }}</div>
        </li>
      </ul>
    </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";

export default {
  name: "BookmarkPolitician",
  props: {
    bookmarkPoliticians: Object
  },
  data() {
    return {
    };
  },
  computed: {
    ...mapState({ userStore: "userStore" }),
  },
  methods: {
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

/*전체 국회의원*/
.bookmark-politician-list-wrap {
  display: flex;
  margin: auto;
  justify-content: space-between;
  align-items: center;
  align-content: flex-start;
}

.bookmark-politician-list {
  margin: 0 auto 0 auto;
  width: 100%;
  max-width: 540px;
  display: table;
  text-align: center;
  padding: 0;
}
.bookmark-politician {
  display: inline-table;
  /*align-items: center;*/
  margin-bottom: 20px;
  padding: 0 5%;
}
.bookmark-politician-image {
  width: 70px;
  height: 70px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  box-sizing: border-box;
  border: 3px solid #0d6efd;
  border-radius: 100%;
}

.bookmark-politician-image img {
  border-radius: 100%;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.bookmark-politician-name {
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
