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
            <th class="petitionLeave">공결</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(i,key) in politicianAttendance" v-bind:key="key">
            <th>{{ i.conferenceTitle }}</th>
            <td>{{ i.attendanceTotal }}</td>
            <td>{{ i.absenceTotal }}</td>
            <td>{{ i.businessTripTotal }}</td>
            <td>{{ i.petitionLeaveTotal }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="empty-box"></div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    politicianAttendance: Array,
    conferenceAttendanceResultList: Array,
  },
  data() {
    return {

    };
  },
  // beforeCreate() {
  //   const politicianID = this.$route.params.politicianID;
  //   axios.get(`/api/attendance/${politicianID}`).then((response) => {
  //   //표//
  //
  //   });
  // },
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
th{
  /*width: 30%;*/
  padding: 0.6rem;
  min-width: 3rem;
  text-align: center;
  margin: 0;
}
td {
  padding: 0.6rem;
  min-width: 3rem;
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

.table-wrap{
  display: flex;
  width: 100%;
  max-width: 540px;
  justify-items: center;
  justify-content: center;
}
</style>
