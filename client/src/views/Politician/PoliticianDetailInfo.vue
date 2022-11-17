<template>
  <div>
    <div class="detail-info-wrap">
      <div class="assembly-image-2-wrap">
        <div class="assembly-image-2" />
      </div>
        <div class="detail-info-title">생년월일</div>
      <div class="detail-info-content">
        {{ elapsedText(PoliticianDetailData.birthday) }}
      </div>
      <div class="detail-info-title">당선이력</div>
      <div class="detail-info-content">
        {{ PoliticianDetailData.selectInfo }}
      </div>
      <div class="detail-info-title">이메일</div>
      <div class="detail-info-content" v-if="PoliticianDetailData.email !== 'null'">{{ PoliticianDetailData.email }}</div>
      <div class="detail-info-content" v-if="PoliticianDetailData.email === 'null'">없음</div>
      <div class="detail-info-title">홈페이지</div>
      <div class="detail-info-content" v-if="PoliticianDetailData.homepage !== 'null'"><a :href="PoliticianDetailData.homepage">{{PoliticianDetailData.homepage}}</a></div>
      <div class="detail-info-content" v-if="PoliticianDetailData.homepage === 'null'">없음</div>
      <div class="detail-info-title">전화번호</div>
      <div class="detail-info-content" v-if="PoliticianDetailData.contact !== 'null'">{{ PoliticianDetailData.contact }}</div>
      <div class="detail-info-content" v-if="PoliticianDetailData.contact === 'null'">없음</div>
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
  padding: 20px 15px 0px 15px;
  position: relative;
  background: #ffffff;
  z-index: 0;
}

.detail-info-title {
  float: left;
  width: 20%;
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
  width: 80%;
  height: 50px;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  text-align: right;
  letter-spacing: -0.024em;

  color: #1b1b1b;
}
.content{
  width: 100%;
  max-width: 540px;
  vertical-align: middle;
  display: inline-block;
}
.detail-info-wrap{
  width: 100%;
  max-width: 540px;
}

.detail-info-content > a {
  text-decoration: none;
  color: #1b1b1b;
}
.detail-info-content > a:hover {
  color: #865935;
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
  margin: auto 0 auto 0;
  position: absolute;
  width: 245px;
  height: 238px;
  background-image: url("@/assets/icon/assembly.svg");
  background-size: cover;
  z-index: -1;
}

.assembly-image-2-wrap{
  display: flex;
  justify-content: center;
  justify-items: center;
}
</style>
