import { Doughnut } from 'vue-chartjs' //또는 'vue-chartjs/legacy'

export default {
  extends: Doughnut,
  props: ['chartData','options'],
  mounted() {
    // this.chartData is created in the mixin.
    // If you want to pass options please create a local options object
    this.renderChart(this.chartData, this.options)
  },
}