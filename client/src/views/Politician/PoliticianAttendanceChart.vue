<script>
import DoughnutChart from "@/commons/doughnutChart.js";
import { Doughnut } from 'vue-chartjs';

export default {
  name: "PoliticianAttendanceChart",
  type: "Doughnut",
  components: {
    DoughnutChart
  },
  props: {

  },
  data() {
    return {
      chart: {
        data: {
          labels: ["딸기", "자두", "수박", "복숭아", "메론", "망고"],
          datasets: [
            {
              backgroundColor: [
                "#A684B7",
                "#DD7445",
                "#DE9D11",
                "#E0D295",
                "#B1D166",
                "#78BAA1"
              ],
              borderColor: "#eee",
              hoverBorderColor: "#eee",
              data: [50, 30, 20, 40, 60, 10]
            }
          ]
        },
        options: {
          plugins: {
            legend: {
              display: true,
              position: "left",
              labels: {
                boxWidth: 8,
                padding: 10,
                usePointStyle: true,
                pointStyle: "circle",
                font: {
                  size: 14
                }
              },
              fullSize: true,
              align: "center"
            },
            tooltip: {
              boxWidth: 15,
              bodyFont: {
                size: 14
              }
            }
          },
        responsive: true,
          maintainAspectRatio: false,
          layout: {
            padding: {
              top: 50,
              bottom: 50
            }
          },
          elements: {
            arc: {
              borderWidth: 2
            }
          },
          animation: {
            duration: 5000
          }
        }
      }
    }
  },
}
</script>