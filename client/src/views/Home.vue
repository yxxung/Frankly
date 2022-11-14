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
      <h2>인기 검색 국회의원 TOP4</h2>
    </div>

    <div class="trend-top4-politician-list">
      <div class="trend-top4-politician">
        <div class="background"></div>
        <p>정진석</p>
      </div>
      <div class="trend-top4-politician">
        <div class="background"></div>
        <p>정진석</p>
      </div>
      <div class="trend-top4-politician">
        <div class="background"></div>
        <p>정진석</p>
      </div>
      <div class="trend-top4-politician">
        <div class="background"></div>
        <p>정진석</p>
      </div>
    </div>
    <Navigation />
  </div>
</template>

<script>
import Navigation from "@/components/Navigation.vue";
import Header from "@/components/Header.vue";
import ImageSlider from "@/components/ImageSlider.vue";
import SearchBar from "@/components/SearchBar.vue";
export default {
  name: "Home",
  components: {
    Navigation: Navigation,
    Header: Header,
    ImageSlider: ImageSlider,
    SearchBar: SearchBar,
  },
  data() {
    return {};
  },
  methods: {},
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
.trend-top4-politician-list {
  padding: 8px 24px;
  position: relative;
  top: 65px;
  width: 100%;
  max-width: 540px;
  height: 120px;
  display: flex;
  justify-content: center;
}
.trend-top4-politician {
  width: 100%;
  display: flex;
  justify-content: space-between;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.background {
  box-sizing: border-box;
  border: 2px solid #d5e1e6;
  border-radius: 100%;
  position: relative;
  width: 74px;
  height: 74px;
  top: 12px;
  background-image: url(../assets/politician/정진석.png);
  background-size: cover;
}
.trend-top4-politician p {
  position: absolute;
  top: 92px;
  font-size: 18px;
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 500;
  color: #000000;
}

</style>
