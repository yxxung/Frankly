<template>
  <div>
  </div>
  <svg :width="width" :height="height">
  </svg>
</template>

<script>
import { Bar } from 'vue-chartjs'
import axios from "axios";
export default {
  name: "PoliticianPropertyDetail",
  props: {
    politicianID: {
      type: String
    },
    politicianInfo: {
      type: Array
    }
  }
  ,
  data() {
    return {
      politicianProperty: [],
      politicianPropertyChange:[],
      data: [90, 72, 75, 25, 10, 92],
      width: 500,
      height: 300,
      padding: 20,
    };
  },
  mounted() {
    this.politicianProperty = []
    // this.politicianPropertyChange =[]
    axios.get('/api/property/' + this.politicianID)
      .then(response => {
        if (response.data instanceof Array) {
          this.politicianProperty = response.data
        } else (
          this.politicianProperty.push(response.data)
        )
        console.log(this.politicianProperty)
      })
      .catch(e => {
        console.log('error:', e)
        console.log(this.inputValue + "request")
      })
    // axios.get('/api/property/change/' + this.politicianID)
    //   .then(response => {
    //     if (response.data instanceof Array) {
    //       this.politicianProperty = response.data
    //     } else (
    //       this.politicianProperty.push(response.data)
    //     )
    //     console.log(this.politicianProperty)
    //   })
    //   .catch(e => {
    //     console.log('error:', e)
    //     console.log(this.inputValue + "request")
    //   })
  },
    //수정
    doChange: function(userinfo) {

    },
    //삭제
    doRemove:  function(userinfo) {

    }
  }
</script>

<style scoped>

</style>
