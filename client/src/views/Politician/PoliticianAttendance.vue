<template>
<div class="wrap">
  <h2>국회의원 출석정보</h2>

  <PoliticianAttendanceView />
</div>
</template>

<script>
import axios from 'axios';
import PoliticianAttendanceView from '@/views/Politician/PoliticianAttendanceView.vue'

export default {
  components: {
    PoliticianAttendanceView
  },
  data() {
    return {

    }
  },
}
</script>

<style>

</style>