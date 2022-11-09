<template>
  <div class="container">
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
  name: "PoliticianVoteChart",
  components: { Doughnut },
  props: {
    propsYesTotal: {
      type: Number,
    },
    propsNoTotal: {
      type: Number,
    },
    propsGiveUpTotal: {
      type: Number,
    },
    propsAbsentTotal: {
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
      default: 200,
    },
    height: {
      type: Number,
      default: 200,
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
    propsYesTotal() {
      this.chartData.datasets[0].data = [
        parseInt(this.propsYesTotal),
        parseInt(this.propsNoTotal),
        parseInt(this.propsGiveUpTotal),
        parseInt(this.propsAbsentTotal),
      ];
    },
    deep: true,
  },
  data() {
    return {
      componentKey: 0,
      chartData: {
        labels: ["찬성", "반대", "기권", "불참"],
        datasets: [
          {
            backgroundColor: ["#8ed2cd", "#ff9797", "#b9bfff", "#f8d374"],
            //data: [this.attendanceTotal, this.petitionLeaveTotal, this.businessTripTotal],
            data: [
              this.propsYesTotal,
              this.propsNoTotal,
              this.propsGiveUpTotal,
              this.propsAbsentTotal
            ],
          },
        ],
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  }
};
</script>