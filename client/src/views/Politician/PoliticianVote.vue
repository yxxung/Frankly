<template>
  <div class="wrap">
    <!--헤더-->
    <header class="header header--back">
      <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
        <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
      </a>
      <h2>법안 표결 이력</h2>
    </header>

    <PoliticianVoteChart
    v-bind:propsYesTotal="yesTotal"
    v-bind:propsNoTotal="noTotal"
    v-bind:propsGiveUpTotal="giveUpTotal"
    v-bind:propsAbsentTotal="absentTotal">
    </PoliticianVoteChart>

    <PoliticianVoteTable :VoteList="VoteList">

    </PoliticianVoteTable>

    <Navigation />
  </div>
</template>

<script>
import axios from "axios";
import PoliticianVoteTable from "@/views/Politician/PoliticianVoteTable.vue";
import PoliticianVoteChart from "@/views/Politician/PoliticianVoteChart.vue";
import Navigation from "@/components/Navigation";

export default {
  components: {
    Navigation: Navigation,
    PoliticianVoteTable,
    PoliticianVoteChart,
  },
  data() {
    return {
      yesTotal: null,
      noTotal: null,
      giveUpTotal: null,
      absentTotal: null,
      VoteList: {},
    };
  },
  beforeCreate() {
    const politicianID = this.$route.params.politicianID;
    axios.get(`/api/vote/count/${politicianID}`).then((response) => {
      //시각화//
      let voteData = response.data;

      let yesTotal = 0; //찬성
      let noTotal = 0; //반대
      let giveUpTotal = 0; //기권
      let absentTotal = 0; //불참

      for (let i = 0; i < voteData.length; i++) {
        if (voteData[i].voteResult === "찬성") {
          yesTotal = voteData[i].voteCount;
        } else if (voteData[i].voteResult === "반대") {
          noTotal = voteData[i].voteCount;
        } else if (voteData[i].voteResult === "기권") {
          giveUpTotal = voteData[i].voteCount;
        } else if (voteData[i].voteResult === "불참") {
          absentTotal = voteData[i].voteCount;
        }
      }

      this.yesTotal = yesTotal
      this.noTotal = noTotal
      this.giveUpTotal = giveUpTotal
      this.absentTotal = absentTotal

      axios.get(`/api/vote/${politicianID}`).then((response) => {
        this.VoteList = response.data
      })
    });
  },
  methods: {},
};
</script>
