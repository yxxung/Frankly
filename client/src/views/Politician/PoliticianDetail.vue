<template>
  <div class="wrap">
    <!--헤더-->
    <header class="header header--back">
      <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
        <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
      </a>
      <div class="header-right-icon">
        <a class="icon-button-56">
          <img src="@/assets/icon/Bookmark.svg" alt="북마크" />
        </a>
        <a class="icon-button-56">
          <img src="@/assets/icon/Other2.svg" alt="더보기" />
        </a>
      </div>
    </header>

    <div class="yellow-background" />

    <div class="assembly-image" />

    <div class="politician-detail-info">
      <div class="politician-detail-region">충북 공주시 부여군 청양군</div>
      <div class="politician-detail-image">
        <img src="@/assets/politician/정진석.png" />
      </div>
      <div class="politician-detail-name">
        {{ PoliticianDetailData.politicianName }}
      </div>
      <div class="politician-detail-party">
        {{ PoliticianDetailData.partyName }}
      </div>
    </div>
    <div class="assembly-text" />

    <div class="assembly-infos">
      <div class="assembly-detail">
        <h2>국회 출석률</h2>
        <h3>86%</h3>
      </div>
      <div class="assembly-detail">
        <h2>표결건수</h2>
        <h3>3147건</h3>
      </div>
      <div class="assembly-detail">
        <h2>당선 횟수</h2>
        <h3>4선</h3>
      </div>
      <router-link to="/statistics"
        ><div class="link-statistics">통계 더보기</div></router-link
      >
      <router-link to ="/property">
        <div class="link-statistics" v-bind:politicianInfo = "PoliticianDetailData">재산정보 보기</div>

      </router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PoliticianDetail",
  data() {
    return {
      PoliticianDetailData: {
        politicianID: "",
        politicianName: "",
        partyName: "",
        selectNumber: "",
        selectInfo: "",
      },
    };
  },
  created() {
    const politicianID = this.$route.params.politicianID;
    axios.get(`/api/politician/${politicianID}`).then((response) => {
      this.PoliticianDetailData.politicianID = response.data.politicianID;
      this.PoliticianDetailData.politicianName = response.data.politicianName;
      this.PoliticianDetailData.partyName = response.data.partyName;
      this.PoliticianDetailData.selectNumber = response.data.selectNumber;
      this.PoliticianDetailData.selectInfo = response.data.selectInfo;
      console.log(response);
    });
  },
  methods:{
    goToPropertyDetail(politicianID) {
      this.$router.push({
        name: "PoliticianDetail",
        params: {
          politicianID: politicianID,
        },
      });
    }

  }

};
</script>

<style>
@import "@/assets/scss/style.scss";

.yellow-background {
  width: 516px;
  height: 228px;
  margin: 0 auto;
  background: rgba(246, 238, 225, 0.5);
  position: relative;
}

/*국회의원 프로필*/
.politician-detail-info {
  z-index: 5;
  position: absolute;
  width: 374px;
  height: 254px;
  margin: -200px 0 0 81px;
  background: #ffffff;
  /* red_lawmaker */

  box-shadow: 0px 4px 16px rgba(255, 0, 0, 0.23);
  border-radius: 24px;
}

.assembly-image {
  z-index: 10;
  position: absolute;
  width: 49px;
  height: 48px;
}

.assembly-text {
  position: absolute;
  width: 98.54px;
  height: 99.7px;
  z-index: 12;
  width: 49px;
  height: 48px;
}

.politician-detail-region {
  margin: 20px auto;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 23px;
  text-align: center;
  letter-spacing: -0.024em;

  color: #2e2e2e;
}

.politician-detail-image {
  width: 82px;
  height: 113px;
  box-sizing: border-box;
  border: 1px solid #f6eee1;
  overflow: hidden;
  margin: 0 auto;
}

.politician-detail-image img {
  width: 81px;
  height: 107px;
  object-fit: cover;
}

.politician-detail-name {
  margin: 5px auto;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 600;
  font-size: 22px;
  line-height: 32px;
  /* identical to box height */

  text-align: center;
  letter-spacing: -0.024em;

  color: #000000;
}

.politician-detail-party {
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 13px;
  line-height: 19px;
  /* identical to box height */

  text-align: center;
  letter-spacing: -0.024em;

  color: #000000;
}

/*국회 정보*/
.assembly-infos {
  width: 375px;
  height: 89px;
  background: #ffffff;
  border-radius: 24px;
  display: table;
}

.assembly-detail {
  width: 33%;
}
</style>
