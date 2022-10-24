<template>
  <div>
    <div class="detail-info-wrap">
      <div class="assembly-image-2" />
      <div class="detail-info-title">생년월일</div>
      <div class="detail-info-content">
        {{ elapsedText(PoliticianDetailData.birthday) }}
      </div>
      <div class="detail-info-title">당선이력</div>
      <div class="detail-info-content">
        {{ PoliticianDetailData.selectInfo }}
      </div>
      <div class="detail-info-title">이메일</div>
      <div class="detail-info-content">{{ PoliticianDetailData.email }}</div>
      <div class="detail-info-title">홈페이지</div>
      <div class="detail-info-content">{{ PoliticianDetailData.homepage }}</div>
      <div class="detail-info-title">전화번호</div>
      <div class="detail-info-content">{{ PoliticianDetailData.contact }}</div>
      <div class="detail-info-title">보좌관</div>
      <div class="detail-info-content">{{ PoliticianDetailData.aide }}</div>
      <div class="detail-info-title">비서관</div>
      <div class="detail-info-content">
        {{ PoliticianDetailData.secretary }}
      </div>
    </div>
  </div>
</template>

<script>
import dateformat from "@/commons/dateformat.js";

export default {
  name: "PoliticianDetailInfo",
  props: {
    PoliticianDetailData: Object,
  },
  methods: {
    //date format 변환
    elapsedText(date) {
      return dateformat.elapsedText(new Date(date));
    },
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";

.detail-info-wrap {
  padding: 20px 30px 0px 30px;
  position: relative;
  background: #ffffff;
}

.detail-info-title {
  float: left;
  width: 100px;
  height: 50px;
  text-align: left;

  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  letter-spacing: -0.024em;

  color: #1b1b1b;
}

.detail-info-content {
  display: inline-block;
  text-align: right;
  width: 330px;
  height: 50px;

  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  text-align: right;
  letter-spacing: -0.024em;

  color: #1b1b1b;
}
.detail-info-wrap h2 {
  text-align: left;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 23px;
  letter-spacing: -0.024em;

  color: #1b1b1b;
}

.detail-info-wrap h3 {
  text-align: right;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 23px;
  text-align: right;
  letter-spacing: -0.024em;

  color: #1b1b1b;
}

.assembly-image-2 {
  margin: 25px 0 0 100px;
  position: absolute;
  width: 245px;
  height: 238px;
  background-image: url("@/assets/icon/assembly.svg");
  background-size: cover;
}
</style>