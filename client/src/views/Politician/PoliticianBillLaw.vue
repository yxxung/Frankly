<template>
  <div>
    <div class="law-info-wrap">
      <div class="law-info-title">대표 발의 법률안</div>
      <div class="law-info-content"
      v-for="law in billLawList" :key="law.billID">
        {{law.billTitle}}
      </div>
      <div class="law-info-content" v-if="billLawNum === 0">
        없음
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PoliticianBillLaw",
  props: {
    billLawList: Array,
    billLawNum: Number
  },
  data() {
    return {
    }
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";

.law-info-wrap {
  padding: 10px 30px 0px 30px;
  position: relative;
  background: #ffffff;
}

.law-info-title {
  width: 100%;
  height: 40px;
  margin: 0 auto;
  text-align: center;

  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 700;
  font-size: 17px;
  letter-spacing: -0.024em;

  color: #1b1b1b;
}

.law-info-content {
  margin: 10px auto 15px auto;
  text-align: center;
  width: 100%;
  height: 100%;

  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  letter-spacing: -0.024em;

  color: #1b1b1b;
}
</style>