<template>
  <div class="wrap">
    <!--헤더-->
    <header class="header header--back">
      <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
        <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
      </a>
      <h2>국회 출석 정보</h2>
    </header>

    <PoliticianAttendanceChart
      v-bind:propsAttendanceTotal="attendanceTotal"
      v-bind:propsPetitionLeaveTotal="petitionLeaveTotal"
      v-bind:propsBusinessTripTotal="businessTripTotal"
      v-bind:propsAbsenceTotal="absenceTotal"
    >
    </PoliticianAttendanceChart>

    <!-- 출석 표-->
    <PoliticianAttendanceTable
      :politicianAttendance="conferenceAttendanceList"
    >
    </PoliticianAttendanceTable>
    <Navigation />
  </div>
</template>

<script>
import axios from "axios";
import PoliticianAttendanceChart from "@/views/Politician/PoliticianAttendanceChart.vue";
import PoliticianAttendanceTable from "@/views/Politician/PoliticianAttendanceTable.vue";
import Navigation from "@/components/Navigation";

export default {
  name: "PoliticianAttendance",
  components: {
    Navigation: Navigation,
    PoliticianAttendanceChart,
    PoliticianAttendanceTable,
  },
  data() {
    return {
      componentKey: 0,
      //시각화에 쓸 데이터
      attendanceTotal: null,
      absenceTotal: null,
      petitionLeaveTotal: null,
      businessTripTotal: null,
      //표에 쓸 데이터
      politicianAttendance: {},
      conferenceAttendanceList: [],
    };
  },
  beforeCreate() {
    const politicianID = this.$route.params.politicianID;
    axios.get(`/api/attendance/${politicianID}`).then((response) => {
      //시각화//
      let businessTripTotal = 0;
      let attendanceTotal = 0;
      let petitionLeaveTotal = 0;
      let absenceTotal = 0;
      for (let i = 0; i < response.data.length; i++) {
        attendanceTotal = response.data[i].attendance + attendanceTotal;
        petitionLeaveTotal = response.data[i].petitionLeave + petitionLeaveTotal;
        businessTripTotal = response.data[i].businessTrip + businessTripTotal;
        if((response.data[i].businessTrip + response.data[i].petitionLeave + response.data[i].attendance) === 0) {
          absenceTotal += 1;
        }
      }
      this.attendanceTotal = attendanceTotal;
      this.petitionLeaveTotal = petitionLeaveTotal;
      this.businessTripTotal = businessTripTotal;
      this.absenceTotal = absenceTotal;

      //표//
      this.politicianAttendance = response.data;
      let attendanceData = response.data;

      let conferenceAttendanceResultList = [];
      let conferenceSet = new Set();
      let attendanceJsons;
      for (attendanceJsons of attendanceData) {
        conferenceSet.add(attendanceJsons["conferenceTitle"]);
      }
      // conference set 에 저장된 출석정보 불러오기.
      conferenceSet.forEach(function (val) {
        let perConferenceAttendaceDataList;
        let newJson = {
          totalNumber: 0,
          conferenceTitle: val,
          attendanceTotal: 0,
          petitionLeaveTotal: 0,
          businessTripTotal: 0,
          absenceTotal: 0,
        };

        perConferenceAttendaceDataList = attendanceData.filter(function (e) {
          return e.conferenceTitle === val;
        });
        for (let conferenceAttendanceData of perConferenceAttendaceDataList) {
          if (conferenceAttendanceData["attendance"] === 1) {
            newJson["attendanceTotal"] += 1;
          } else if (conferenceAttendanceData["businessTrip"] === 1) {
            newJson["businessTripTotal"] += 1;
          } else if (conferenceAttendanceData["petitionLeave"] === 1) {
            newJson["petitionLeaveTotal"] += 1;
          } else {
            newJson["absenceTotal"] += 1;
          }
          newJson["totalNumber"] += 1;
        }

        conferenceAttendanceResultList.push(newJson);
      });


      this.conferenceAttendanceList = conferenceAttendanceResultList;
    });
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";
</style>
