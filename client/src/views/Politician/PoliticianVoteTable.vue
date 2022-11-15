<template>
  <div class="wrap">
    <b-list-group
      v-for="vote in VoteList"
      :key="vote.voteID"
    >
      <b-list-group-item
        class="mt-1 d-flex justify-content-between align-items-center"
      >
        <b-link v-on:click = "goLink(vote)" class="b-link-style">{{ vote.billTitle }}</b-link>
        <b-badge v-if="vote.voteResult === '찬성'" variant="info" pill>{{ vote.voteResult }}</b-badge>
        <b-badge v-else-if="vote.voteResult === '반대'" variant="danger" pill>{{ vote.voteResult }}</b-badge>
        <b-badge v-else-if="vote.voteResult === '불참'" variant="warning" pill>{{ vote.voteResult }}</b-badge>
        <b-badge v-else-if="vote.voteResult === '기권'" variant="primary" pill>{{ vote.voteResult }}</b-badge>
      </b-list-group-item>
    </b-list-group>

    <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      align="center"
      first-number
      last-number
      class="mt-5"
    ></b-pagination>
    <div class="empty-box"></div>
  </div>
</template>

<script>
export default {
  name: "PoliticianVoteTable",
  props: {
    VoteList: Array,
  },
  data() {
    return {
      perPage: 80,
      currentPage: 1,
    };
  },
  methods:{
    goLink(vote){
      window.open(vote["voteURL"])
    }
  }
  ,
  computed: {
    VoteList() {
      const votes = this.VoteList
      return votes.slice(
        (this.currentPage - 1) * this.perPage,
        this.currentPage * this.perPage
      )
    },
    rows() {
      return this.VoteList.length
    },
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";

.b-link-style{
  color: #111111;
  text-decoration: none;
}
.b-link-style:hover{
  color: #a00;
}
</style>

