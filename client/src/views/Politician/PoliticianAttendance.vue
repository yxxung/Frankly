<template>
  <div class="wrap">
    <h2>국회의원 출석정보</h2>

    <!--시각화할 도넛 차트 부분-->
    <PoliticianAttendanceView
      :attendanceData="attendanceData"
    >
    </PoliticianAttendanceView>
  </div>
</template>

<script>
import axios from "axios";
import PoliticianAttendanceView from "@/views/Politician/PoliticianAttendanceView.vue";

export default {
  name: "PoliticianAttendance",
  components: {
    PoliticianAttendanceView,
  },
  data() {
    return {
      attendanceData: [],
      attendanceTotal: "",
      petitionLeaveTotal: "",
      businessTripTotal: "",
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
        petitionLeaveTotal =
          response.data[i].petitionLeave + petitionLeaveTotal;
        businessTripTotal = response.data[i].businessTrip + businessTripTotal;
      }
      this.attendanceTotal = attendanceTotal;
      this.petitionLeaveTotal = petitionLeaveTotal;
      this.businessTripTotal = businessTripTotal;

      console.log("attendanceTotal", this.attendanceTotal);
      console.log("businessTripTotal", this.petitionLeaveTotal);
      console.log("petitionLeaveTotal", this.businessTripTotal);

      this.attendanceData.push(attendanceTotal);
      this.attendanceData.push(petitionLeaveTotal);
      this.attendanceData.push(businessTripTotal);

      console.log("array", this.attendanceData);

    });
  },
  methods: {},
};
</script>

<style>
</style>