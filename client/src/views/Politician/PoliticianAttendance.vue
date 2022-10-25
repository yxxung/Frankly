<template>
  <div class="wrap">
    <!--헤더-->
    <header class="header header--back">
      <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
        <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
      </a>
      <h2>출석정보</h2>
    </header>

    <canvas id="chart" width="400" height="400"></canvas>


    <PoliticianAttendanceChart
      :attendanceData="attendanceData"
    >
    </PoliticianAttendanceChart>

    <!-- 출석 표-->
    <PoliticianAttendanceTable
      :politicianAttendance="politicianAttendance">
    </PoliticianAttendanceTable>
  </div>
</template>

<script>
import axios from "axios";
import PoliticianAttendanceChart from "@/views/Politician/PoliticianAttendanceChart.vue";
import PoliticianAttendanceTable from "@/views/Politician/PoliticianAttendanceTable.vue";

import {Chart, BarElement, BarController, LinearScale, CategotyScale } from 'cahrt.js';
Chart.register(BarElement, BarController, LinearScale, CategotyScale);

export default {
  name: "PoliticianAttendance",
  components: {
    PoliticianAttendanceChart,
    PoliticianAttendanceTable
  },
  data() {
    return {
      //시각화에 쓸 데이터
      attendanceData: [],
      attendanceTotal: "",
      petitionLeaveTotal: "",
      businessTripTotal: "",
      //표에 쓸 데이터
      politicianAttendance: {}
    };
  },
  beforeCreate() {
    const politicianID = this.$route.params.politicianID;
    axios.get(`/api/attendance/${politicianID}`).then((response) => {
      let attendanceData = response.data;
      console.log(attendanceData);
      let businessTripTotal = 0;
      let attendanceTotal = 0;
      let petitionLeaveTotal = 0;
      for (let i = 0; i < response.data.length; i++) {
        attendanceTotal = response.data[i].attendance + attendanceTotal;
        petitionLeaveTotal = response.data[i].petitionLeave + petitionLeaveTotal;
        businessTripTotal = response.data[i].businessTrip + businessTripTotal;
      }
      this.attendanceTotal = attendanceTotal;
      this.petitionLeaveTotal = petitionLeaveTotal;
      this.businessTripTotal = businessTripTotal;

      console.log("attendanceTotal", this.attendanceTotal);
      console.log("businessTripTotal", this.petitionLeaveTotal);
      console.log("petitionLeaveTotal", this.businessTripTotal);

      this.attendanceData.push(attendanceTotal, petitionLeaveTotal, businessTripTotal);

      console.log("array", this.attendanceData);

      //테이블
      for(let titleJson of response.data) {

      }

    });
  },
  methods: {
    
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";
</style>