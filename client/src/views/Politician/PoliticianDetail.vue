<template>
  <div class="wrap">
    <div class="content">
      <!--헤더-->
      <header class="politician-header header--back">
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
          ><div class="assembly-detail">
            <h4>> 통계<br />더보기</h4>
          </div></router-link
        >
      </div>

      <div class="link-statistics-container">
        <div class="link-statistics" @click="goToPropertyDetail(this.PoliticianDetailData.politicianID)">재산정보</div>
        <div class="link-statistics" @click="goToNewsKeyword(this.PoliticianDetailData.politicianID)">뉴스 키워드</div>
      </div>

      <div class="assembly-law-info">
        <div>
          <b-nav pills align="center">
            <b-nav-item>대표발의법률안</b-nav-item>
            <b-nav-item>공동발의법률안</b-nav-item>
            <b-nav-item>표결현황</b-nav-item>
          </b-nav>
        </div>
      </div>
    </div>
    <Navigation />
  </div>

</template>

<script>
import axios from "axios";
import Navigation from "@/components/Navigation.vue";

export default {
  name: "PoliticianDetail",
  components:{
    Navigation
  }
  ,
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
  methods:{
    goToPropertyDetail(politicianID) {
      this.$router.push({
        name: "PoliticianPropertyDetail",
        params: {
          politicianInfo: JSON.stringify({
            politicianID: politicianID,
            PoliticianDetailData: this.PoliticianDetailData
          })
        },
      });
    },
    goToNewsKeyword(politicianID) {
      this.$router.push({
        name: "PoliticianNewsKeyword",
        params: {
          politicianID: politicianID,
          politicianInfo: this.PoliticianDetailData
        },
      });
    }

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
};
</script>

<style>
@import "@/assets/scss/style.scss";

.politician-header {
  top: 0;
  position: fixed;
  width: 100%;
  max-width: 540px; /*max-width*/
  height: 56px;
  z-index: 999;
  background-color: #f9f3e9;
}

.content {
  background: #f9f3e9;
}

/*국회의원 프로필*/
.politician-detail-info {
  margin: 54px auto 0 auto;
  position: relative;
  width: 500px;
  height: 254px;
  background: #ffffff;
  /* red_lawmaker */
  border-radius: 24px;
  text-align: center;
}

.assembly-image {
  z-index: 10;
  margin: 10px 0 0 247px;
  position: absolute;
  width: 49px;
  height: 48px;
  background-image: url("@/assets/icon/assembly.svg");
}

.assembly-text {
  margin: -90px 0 0 30px;
  position: absolute;
  width: 98.54px;
  height: 99.7px;
  z-index: 12;
  width: 160px;
  height: 80px;
  background-image: url("@/assets/icon/assembly_text.svg");
  background-size: cover;
}

.politician-detail-region {
  display: inline-block;
  margin: 20px auto 20px auto;
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
  margin: 30px auto;
  width: 500px;
  height: 89px;
  background: #ffffff;
  border-radius: 24px;
  display: table;
}

.assembly-detail {
  margin-top: 20px;
  width: 25%;
  display: inline-block;
}

.assembly-detail h2 {
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 19px;
  /* identical to box height */

  text-align: center;
  letter-spacing: -0.024em;

  color: #000000;
}

.assembly-detail h3 {
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 19px;
  /* identical to box height */

  text-align: center;
  letter-spacing: -0.024em;
  color: #000000;
}
.assembly-detail h4 {
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  line-height: 19px;
  text-align: center;
  letter-spacing: -0.024em;

  color: #6e6e6e;
}

/*법률안*/
.assembly-law-info {
  margin: 30px auto 0 auto;
  width: 500px;
  height: 300px;
  background: #ffffff;
  border-radius: 24px;
}

.link-statistics-container {
  display: flex;
  justify-content: flex-start;
  border-radius: 24px;
  margin: 30px auto;
  width: 500px;
  padding: 24px 16px;
  background: #ffffff;
}

.link-statistics {
  padding: 8px 16px;
  color: #3c3c3c;
  border-radius: 8px;
  border: 1px solid #ebe8e2;
  margin-right: 8px;
}

.link-statistics:hover {
  cursor: pointer;
  background-color: #f2eee8;
}

</style>
