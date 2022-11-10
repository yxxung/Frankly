<template>
  <div class="chart-container" @forceUpdate="handleForceUpdate">
    <Doughnut
      :chart-options="chartOptions"
      :chart-data="chartData"
      :chart-id="chartId"
      :dataset-id-key="datasetIdKey"
      :plugins="plugins"
      :css-classes="cssClasses"
      :styles="styles"
      :width="width"
      :height="height"
    />
  </div>
</template>

<script>
import axios from "axios";
import { Doughnut } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
} from "chart.js";

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale);

export default {
  name: "PoliticianAttendanceChart",
  components: { Doughnut },
  props: {
    propsAttendanceTotal: {
      type: Number,
    },
    propsAbsenceTotal: {
      type: Number,
    },
    propsPetitionLeaveTotal: {
      type: Number,
    },
    propsBusinessTripTotal: {
      type: Number,
    },
    chartId: {
      type: String,
      default: "doughnut-chart",
    },
    datasetIdKey: {
      type: String,
      default: "label",
    },
    width: {
      type: Number,
      default: 250,
    },
    height: {
      type: Number,
      default: 250,
    },
    cssClasses: {
      default: "",
      type: String,
    },
    styles: {
      type: Object,
      default: () => {},
    },
    plugins: {
      type: Object,
      default: () => {},
    },
  },
  watch: {
    /*
    handler() {
      this.chartData.datasets[0].data = [
        parseInt(this.propsAttendanceTotal),
        //parseInt(this.propsPetitionLeaveTotal),
        //parseInt(this.propsBusinessTripTotal),
      ];
      this.chartData.datasets[1].data = [
        //(this.propsAttendanceTotal),
        parseInt(this.propsPetitionLeaveTotal),
        //(this.propsBusinessTripTotal),
      ];
      this.chartData.datasets[2].data = [
        //parseInt(this.propsAttendanceTotal),
        //parseInt(this.propsPetitionLeaveTotal),
        parseInt(this.propsBusinessTripTotal),
      ];
    },*/
    propsAttendanceTotal() {
      this.chartData.datasets[0].data = [
        parseInt(this.propsAttendanceTotal),
        parseInt(this.propsAbsenceTotal),
        parseInt(this.propsBusinessTripTotal),
        parseInt(this.propsPetitionLeaveTotal),
      ];
    },
    deep: true,
  },
  data() {
    return {
      componentKey: 0,
      chartData: {
        labels: ["출석", "결석", "출장", "결석신고서"],
        datasets: [
          {
            backgroundColor: ["#8ed2cd", "#ff9797", "#b9bfff", "#f8d374"],
            //data: [this.attendanceTotal, this.petitionLeaveTotal, this.businessTripTotal],
            data: [
              this.propsAttendanceTotal,
              this.propsAbsenceTotal,
              this.propsBusinessTripTotal,
              this.propsPetitionLeaveTotal,
            ],
          },
        ],
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
/*
  beforeCreate() {
    const politicianID = this.$route.params.politicianID;
    axios.get(`/api/attendance/${politicianID}`).then((response) => {
      //시각화//
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
    });
  },*/
};

</script>

<style>
.chart-container{
  display: flex;
  width: 100%;
  max-width: 540px;
  justify-content: center;
  justify-items: center;
}

</style>
