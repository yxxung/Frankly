<template>
  <div class="wrap">
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th class="confTitle"></th>
            <th class="attendance">출석</th>
            <th class="leave">결석</th>
            <th class="trip">출장</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="i in politicianAttendance" v-bind:key="i.attendanceID">
            <th>{{ i.conferenceTitle }}</th>
            <td>{{ i.attendance }}</td>
            <td>{{ i.petitionLeave }}</td>
            <td>{{ i.businessTrip }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    politicianAttendance: Array,
    propsConferenceAttendanceResultList: Array,
  },
  data() {
    return {
        conferenceAttendanceResultList: [],
    };
  },
  beforeCreate() {
    const politicianID = this.$route.params.politicianID;
    axios.get(`/api/attendance/${politicianID}`).then((response) => {
    //표//
      let attendanceData = response.data;

      let conferenceAttendanceResultList = [];
      let conferenceSet = new Set();
      let attendanceJsons;
      for (attendanceJsons of attendanceData){
        conferenceSet.add(attendanceJsons["conferenceTitle"])
      }

      conferenceSet.forEach(function (val) {
        let perConferenceAttendaceDataList;
        let newJson = {
          "totalNumber": 0,
          "conferenceTitle" : val,
          "attendanceTotal" : 0,
          "petitionLeaveTotal" : 0,
          "businessTripTotal" : 0,
          "absenceTotal" : 0
        }

        perConferenceAttendaceDataList = attendanceData.filter(function(e){

            return e.conferenceTitle === val
          }
        )
        for(let conferenceAttendanceData of perConferenceAttendaceDataList){
          if(conferenceAttendanceData["attendance"] == 1){
            newJson["attendanceTotal"] += 1;
          }
          else if(conferenceAttendanceData["businessTrip"] == 1){
            newJson["businessTripTotal"] += 1;
          }
          else if(conferenceAttendanceData["petitionLeave"] == 1){
            newJson["petitionLeaveTotal"] += 1;
          }
          else{
            newJson["absenceTotal"] += 1;
          }
          newJson["totalNumber"] += 1;
        }
        conferenceAttendanceResultList.push(newJson);

        console.log("conferenceAttendanceResultList",conferenceAttendanceResultList);
      });
    });
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";

table {
  margin: 0 auto;
  border-collapse: collapse;
  border: 0;
}
th,
td {
  border: 1px solid rgb(255, 255, 255);
  background-clip: padding-box;
  scroll-snap-align: start;
}
tbody tr:last-child th,
tbody tr:last-child td {
  border-bottom: 0;
}
thead {
  position: relative;
}
th,
td {
  padding: 0.6rem;
  min-width: 6rem;
  text-align: center;
  margin: 0;
}
thead tr {
  text-align: center;
}
thead th {
  position: sticky;
  background-clip: padding-box;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 20px;

  color: #444444;
}
thead th.pin {
  left: 0;
  border-left: 0;
}
tbody th {
  background-clip: padding-box;
  border-left: 0;
}
tbody {
  position: relative;
}
tbody th {
  position: sticky;
  left: 0;
}
thead th,
tbody th {
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 20px;

  color: #444444;
}

tbody td {
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 800;
  font-size: 16px;
  line-height: 23px;
  text-align: center;

  color: #444444;
}
</style>