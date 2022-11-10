<template>
  <div class="wrap">
    <b-list-group
      v-for="vote in VoteList"
      :key="vote.voteID"
    >
      <b-list-group-item
        class="d-flex justify-content-between align-items-center"
      >
        {{ vote.billTitle }}
        <b-badge variant="primary" pill>{{ vote.voteResult }}</b-badge>
      </b-list-group-item>
    </b-list-group>

    <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      align="center"
      margin="20px auto"
    ></b-pagination>
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
      perPage: 100,
      currentPage: 1,
    };
  },
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

</style>