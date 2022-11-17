<template>

</template>

<script>
import axios from "axios";

export default {
  name: "PoliticianStatistics",
  attendanceList: [],
  billLawList: []
  ,
  setup() {


  },
  mounted: function () {
    const politicianID = this.$route.params.politicianID;
    axios.get(`/api/attendance/${politicianID}`).then((response) => {
      let attendanceList = response.data;
      let jsonss;
      let count = 0;
      for(jsonss of attendanceList){
        let total = jsonss["businessTrip"] + jsonss["petitionLeave"] + jsonss["attendance"];
        if(total === 0){
          count++;
        }
      }
      let percentage = ((attendanceList.length - count) / attendanceList.length)*100;
      this.attendancePercentage = percentage;
      this.attendanceList = attendanceList
    });

    axios.get(`/api/billLaw/${politicianID}`).then((response) => {
      let billLawList = response.data
      this.billLawNum = billLawList.length
    });
  }
}
</script>

<style scoped>

</style>