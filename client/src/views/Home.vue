<template>
  <div class="wrap">
    <Header />

    <!--슬라이더-->
    <div id="slider">
      <input type="radio" name="slider" id="slide1" checked />
      <input type="radio" name="slider" id="slide2" />
      <input type="radio" name="slider" id="slide3" />

      <div id="slides">
        <div id="overflow">
          <div class="inner">
            <div class="slide slide_1">
              <div class="slide-content"></div>
            </div>

            <div class="slide slide_2">
              <div class="slide-content"></div>
            </div>

            <div class="slide slide_3">
              <div class="slide-content"></div>
            </div>
          </div>
        </div>
      </div>

      <div id="controls">
        <label for="slide1"></label>
        <label for="slide2"></label>
        <label for="slide3"></label>
      </div>

      <div id="bullets">
        <label for="label1"></label>
        <label for="label2"></label>
        <label for="label3"></label>
      </div>
    </div>

    <!--국회의원 검색-->
    <SearchBar />

    <!-- 인기 검색 국회의원 리스트-->
    <div class="trend-top4-politician-title">
      <div class="icon-button"><img src="@/assets/icon/button.svg" /></div>
      <h2>인기 검색 국회의원 TOP3</h2>
    </div>

    <div class="trend-politician-list-wrap">
      <ul class="trend-politician-list">
        <li
          class="trend-politician"
          v-for="politician in topPoliticians"
          v-bind:key="politician.politicianID"
          @click="
            goToPoliticianDetail(politician.politicianID)"
        >
          <!-- 정치인 리스트 출력 이미지, 이름-->
          <div
            class="trend-politician-image"
            v-bind:style="{ border: getPoliticianColor(politician) }"
          >
            <img
              :src="
                'https://teamfrankly.kr/images/' +
                politician.politicianID +
                '.png'
              "
            />
          </div>
          <div class="trend-politician-name">{{ politician.politicianName }}</div>
        </li>
      </ul>
    </div>
    <Navigation />
  </div>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import Header from "@/components/Header.vue";
import ImageSlider from "@/components/ImageSlider.vue";
import SearchBar from "@/components/SearchBar.vue";
import axios from "axios";

export default {
  name: "Home",
  components: {
    Navigation: Navigation,
    Header: Header,
    ImageSlider: ImageSlider,
    SearchBar: SearchBar,
  },
  mounted() {
    this.getTrendPoliticianList();
  },
  data() {
    return {
      topPoliticians: {}
    };
  },
  methods: {
    getTrendPoliticianList() {
      axios
        .get("/api/politician/rank")
        .then((response) => {
          this.topPoliticians = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getPoliticianColor(politician){
      if(politician.partyName === "국민의힘"){
        return "3px solid #aa0000";
      }
      else if(politician.partyName === "더불어민주당"){
        return "3px solid #0d6efd"
      }
      else if(politician.partyName === "시대전환"){
        return "3px solid #8B00FF"
      }
      else if(politician.partyName === "정의당"){
        return "3px solid #FFD400"
      }
      else if(politician.partyName === "기본소득당"){
        return "3px solid #000000"
      }
    },
    goToPoliticianDetail(politicianID) {
      this.$router.push({
        name: "PoliticianDetail",
        params: {
          politicianID: politicianID,
        },
      });
    },
  },
};
</script>

<style>
@import "@/assets/scss/style.scss";
/* 슬라이드 */
#slider {
  margin: 15px auto 40px auto;
  width: 540px;
  max-width: 100%;
  text-align: center;
  padding: 8px 24px;
}
#slider input[type="radio"] {
  display: none;
}
#slider label {
  cursor: pointer;
  text-decoration: none;
}
#slides {
  padding: 10px;
  border: 3px solid #f5f5f5;
  background: #fff;
  position: relative;
  z-index: 1;
  border-radius: 25px;
}
#overflow {
  width: 100%;
  overflow: hidden;
}
#slide1:checked ~ #slides .inner {
  margin-left: 0;
}
#slide2:checked ~ #slides .inner {
  margin-left: -100%;
}
#slide3:checked ~ #slides .inner {
  margin-left: -200%;
}
#slides .inner {
  transition: margin-left 800ms cubic-bezier(0.077, 0, 0.175, 1);
  width: 300%; /* 아이템 수 * 100 */
  line-height: 0;
  height: 200px;
}
#slides .slide {
  width: 33.333%; /* 100 / 아이템 수 */
  float: left;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  color: #fff;
}
#slides .slide_1 {
  background-image: url("@/assets/home-slide.png");
  background-size: cover;
}
#slides .slide_2 {
  background-image: url("@/assets/home-slide.png");
  background-size: cover;
}
#slides .slide_3 {
  background-image: url("@/assets/home-slide.png");
  background-size: cover;
}
.slide-content {
  padding: 10px;
}
#controls {
  margin: -130px 0 0 0;
  width: 100%;
  height: 50px;
  z-index: 3;
  position: relative;
}
#controls label {
  transition: opacity 0.2s ease-out;
  display: none;
  width: 50px;
  height: 50px;
  opacity: 0.4;
}
#controls label:hover {
  opacity: 1;
}
#slide1:checked ~ #controls label:nth-child(2),
#slide2:checked ~ #controls label:nth-child(3),
#slide3:checked ~ #controls label:nth-child(1) {
  background: url(https://image.flaticon.com/icons/svg/130/130884.svg) no-repeat;
  float: right;
  margin: 0 -50px 0 0;
  display: block;
}
#slide1:checked ~ #controls label:nth-child(3),
#slide2:checked ~ #controls label:nth-child(1),
#slide3:checked ~ #controls label:nth-child(2) {
  background: url(https://image.flaticon.com/icons/svg/130/130882.svg) no-repeat;
  float: left;
  margin: 0 0 0 -50px;
  display: block;
}
#bullets {
  margin: 80px 0 0;
  text-align: center;
}
#bullets label {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: 100%;
  background: #f5f5f5;
  margin: 0 8px;
}
#slide1:checked ~ #bullets label:nth-child(1),
#slide2:checked ~ #bullets label:nth-child(2),
#slide3:checked ~ #bullets label:nth-child(3) {
  background: rgb(124, 124, 124);
}
/*인기 검색 국회의원*/
.trend-top4-politician-title {
  max-width: 540px;
  width: 100%;
  height: 100%;
  margin: 0 auto;
  top: 40px;
  position: relative;
  padding: 8px 24px;
}
.icon-button {
  position: absolute;
}
.icon-button img {
  width: 25px;
  height: 25px;
  filter: invert(12%) sepia(98%) saturate(7493%) hue-rotate(1deg)
    brightness(102%) contrast(106%);
}
.trend-top4-politician-title h2 {
  position: absolute;
  left: 55px;
  vertical-align: middle;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 500;
  font-size: 21px;
  line-height: 23px;
  color: #2b2b2b;
}

/*인기검색 국회의원 리스트*/
.trend-politician-list-wrap{
  width: 100%;
  display: flex;
  margin: 85px auto 0 auto;
  justify-content: space-between;
  align-items: center;
}
.trend-politician-list {
  width: 100%;
  max-width: 540px;
  display: table;
  align-items: center;
  text-align: center;
  padding: 0;
  margin: 0 auto 0 auto;
}
.trend-politician {
  display: inline-table;
  /*align-items: center;*/
  margin-bottom: 20px;
  padding: 0 5%;
}
.trend-politician-image {
  width: 75px;
  height: 75px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  box-sizing: border-box;
  border: 3px solid #0d6efd;
  border-radius: 100%;
}

.trend-politician-image img {
  border-radius: 100%;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.trend-politician-name {
  margin: 5px auto;
  font-size: 16px;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 500;
  color: #000000;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
