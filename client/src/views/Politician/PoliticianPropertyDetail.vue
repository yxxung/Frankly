<template>
  <div>
  </div>
  <svg :width="width" :height="height">
    <path fill="none" stroke="#76BF8A" stroke-width="3" :d="path"></path>
  </svg>
</template>

<script>
import * as d3 from "d3"
export default {
  name: "PoliticianPropertyDetail",
  props:{
    politicianID: {
      type : String
    },
    politicianInfo:{
      type : Array
    }
  }
  ,
  data(){
    return{
      politicianProperty:[],
      data: [90, 72, 75, 25, 10, 92],
      width: 500,
      height: 300,
      padding: 20,
    };
  },
  computed: {
    path() {
      return this.line(this.data);
    },
    line() {
      return d3
        .line()
        .x((d, i) => this.xScale(i))
        .y((d) => this.ySclae(d));
    },
    xScale() {
      return d3
        .scaleLinear()
        .range([this.padding, this.width - this.padding])
        .domain(d3.extent(this.data, (d, i) => i));
    },
    ySclae() {
      return d3.scaleLinear().range([this.height - this.padding, this.padding]).domain([0, 100]);
    },
    chart: function () {
      const svg = d3.create("svg").attr("viewBox", [0, 0, this.width, this.height]);

      const updateBars = bars(svg);
      const updateAxis = axis(svg);
      const updateLabels = labels(svg);
      const updateTicker = ticker(svg);

      for (const keyframe of keyframes) {
        const transition = svg.transition()
          .duration(duration)
          .ease(d3.easeLinear);

        // Extract the top bar’s value.
        x.domain([0, keyframe[1][0].value]);

        updateAxis(keyframe, transition);
        updateBars(keyframe, transition);
        updateLabels(keyframe, transition);
        updateTicker(keyframe, transition);

        invalidation.then(() => svg.interrupt());
    }
  }

}
</script>

<style scoped>

</style>
