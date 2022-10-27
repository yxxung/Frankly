<template>
  <div class="politician-detail-wrap">
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
          <img :src="'http://teamfrankly.kr/images/' + PoliticianDetailData.politicianID + '.png'" />
        </div>
        <div class="politician-detail-name">
          {{ PoliticianDetailData.politicianName }}
        </div>
        <div class="politician-detail-party">
          {{ PoliticianDetailData.partyName }}
        </div>
      </div>
      <div class="assembly-text" />

      <div class="politician-detail-info-2">
        <PoliticianDetailInfo
          v-bind:PoliticianDetailData="PoliticianDetailData"
        />
      </div>

      <div class="assembly-infos">
        <div class="assembly-detail">
          <h2>국회 출석률</h2>
          <h3>{{ this.attendancePercentage }}%</h3>
        </div>
        <div class="assembly-detail">
          <h2>법률안 대표 발의 건수</h2>
          <h3>{{this.billLawNum}}건</h3>
        </div>
        <div class="assembly-detail">
          <h2>당선 횟수</h2>
          <h3>{{ PoliticianDetailData.selectNumber }}선</h3>
        </div>
        <div
          class="assembly-detail"
          @click="goToDashboard(this.PoliticianDetailData.politicianID)"
        >
          <h4>> 통계<br />더보기</h4>
        </div>
      </div>

      <div class="link-statistics-container">
        <!--        <div class="link-statistics" @click="goToPropertyDetail(this.PoliticianDetailData.politicianID)">재산정보</div>-->
        <div
          class="link-statistics"
          @click="goToNewsKeyword(this.PoliticianDetailData.politicianID)"
        >
          뉴스 키워드
        </div>
        <div
          class="link-statistics"
          @click="goToAttendance(this.PoliticianDetailData.politicianID)"
        >
          출석 정보
        </div>
        <div
          class="link-statistics"
          @click="goToBillLaw(this.PoliticianDetailData.politicianID)"
        >
          대표 발의 법률안
        </div>
      </div>
    </div>
    <div class="empty-box"></div>
    <Navigation />
  </div>
</template>

<script>
import axios from "axios";
import PoliticianDetailInfo from "@/views/Politician/PoliticianDetailInfo.vue";
import Navigation from "@/components/Navigation.vue";

export default {
  name: "PoliticianDetail",
  components: {
    Navigation,
    PoliticianDetailInfo,
  },
  data() {
    return {
      PoliticianDetailData: {},
      attendanceList: [],
      attendancePercentage: 0,
      billLawNum: 0,
      billLawList: [],
    };
  },
  methods: {
    goToNewsKeyword(politicianID) {
      this.$router.push({
        name: "PoliticianNewsKeyword",
        params: {
          politicianID: politicianID,
          politicianName: this.PoliticianDetailData.politicianName
        },
      });
    },
    goToAttendance(politicianID) {
      this.$router.push({
        name: "PoliticianAttendance",
        params: {
          politicianID: politicianID,
        },
      });
    },
    goToBillLaw(politicianID) {
      this.$router.push({
        name: "PoliticianBillLaw",
        params: {
          politicianID: politicianID,
        },
      });
    },
    goToDashboard(politicianID) {
      // const router = useRouter()
      this.$router.push({
        name: "PoliticianStatistics",
        params: {
          politicianID: politicianID,
        },
      });
    },
  },
  beforeCreate() {
    const politicianID = this.$route.params.politicianID;
    axios.get(`/api/politician/${politicianID}`).then((response) => {
      this.PoliticianDetailData = response.data;

      console.log(response);
    });
    axios.get(`/api/attendance/${politicianID}`).then((response) => {
      let attendanceList = response.data;
      let jsonss;
      let count = 0;
      for (jsonss of attendanceList) {
        let total =
          jsonss["businessTrip"] +
          jsonss["petitionLeave"] +
          jsonss["attendance"];
        if (total === 0) {
          count++;
        }
      }


        let percentage = ((attendanceList.length - count) / attendanceList.length)*100;
        this.attendancePercentage = percentage.toFixed(1);
        this.attendanceList = attendanceList

      });
      axios.get(`/api/billLaw/${politicianID}`).then((response) => {
        let billLawList = response.data
        this.billLawNum = billLawList.length
        console.log(response.data)
      });
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";

.politician-detail-wrap {
  margin: 54px auto 0 auto;
  max-width: 540px;
  /*max-width*/
  height: 100%;
  background-color: #ffffff;
}

.politician-header {
  top: 0;
  position: fixed;
  width: 100%;
  max-width: 540px; /*max-width*/
  height: 56px;
  z-index: 999;
  background-color: rgb(250, 246, 240);
}

.content {
  background: rgba(246, 238, 225, 0.5);
}

/*국회의원 프로필*/
.politician-detail-info {
  margin: 54px auto 0 auto;
  position: relative;
  width: 500px;
  height: 254px;
  background: #ffffff;
  /* red_lawmaker */
  text-align: center;
}

.politician-detail-info-2 {
  margin: 30px auto 0 auto;
  padding: 10px 0 10px 0;
  width: 500px;
  height: 100%;
  background: #ffffff;
  /* red_lawmaker */
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
  margin: 30px auto 0 auto;
  width: 500px;
  height: 89px;
  background: #ffffff;
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

  color: #2b2b2b;
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
  color: #212121;
}
.assembly-detail h4 {
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  text-align: center;
  letter-spacing: -0.024em;

  color: #808080;
}

.link-statistics-container {
  display: flex;
  justify-content: flex-start;
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
.empty-box {
  height: 40px;
}
</style>
