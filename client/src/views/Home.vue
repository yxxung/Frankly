<template>
    <body>
        <div class="wrap">
            <Header />
        
            <!--슬라이더-->
            <div id="slider">
                <input type="radio" name="slider" id="slide1" checked>
                <input type="radio" name="slider" id="slide2">
                <input type="radio" name="slider" id="slide3">

                <div id="slides">
                <div id="overflow">
                    <div class="inner">

                    <div class="slide slide_1">
                        <div class="slide-content">
                        <h2>Slide1</h2>
                        </div>
                    </div>

                    <div class="slide slide_2">
                        <div class="slide-content">
                        <h2>Slide2</h2>
                        </div>
                    </div>

                    <div class="slide slide_3">
                        <div class="slide-content">
                        <h2>Slide3</h2>
                        </div>
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
            <div class="politician-search">
                <form class="politician-search-form" action="" method="get">
                    <input class="politician-search-form__text-input" type="text" placeholder="국회의원 검색">
                    <button class="search-button" type="submit" name="click"><img src="@/assets/icon/button.svg"></button>
                </form>
            </div>

            <!-- 인기 검색 국회의원 리스트-->
            <div class="trend-top4-politician-title">
                <div class="icon-button"><img src="@/assets/icon/button.svg"></div>
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

            <!--오늘의 국회 일정-->
            <div class="parliamentary-schedule-title">
                <div class="icon-bookmark"><img src="../assets/icon/Bookmark.svg"></div>
                <h2>오늘의 국회일정</h2>
                <a href="/Politician"><h3>자세히 보기</h3></a>
            </div>

            <div class="parliamentary-schedule-list">
                <div class="parliamentary-schedule">
                    <h2>본 회의</h2>
                    <div>1</div>
                </div>
                <div class="parliamentary-schedule">
                    <h2>위원회</h2>
                    <div>10</div>
                </div>
                <div class="parliamentary-schedule">
                    <h2>의장단</h2>
                    <div>1</div>
                </div>
                <div class="parliamentary-schedule">
                    <h2>세미나</h2>
                    <div>5</div>
                </div>
                <div class="parliamentary-schedule">
                    <h2>국회행사</h2>
                    <div>1</div>
                </div>
            </div>
            <Navigation />
        </div>
    </body>
</template>

<script>
import Navigation from '@/components/Navigation.vue'
import Header from '@/components/Header.vue'
import ImageSlider from '@/components/ImageSlider.vue'

export default {
  name: 'Home',
  components: {
    'Navigation': Navigation,
    'Header': Header,
    'ImageSlider': ImageSlider
  },
  data() {
    return {

    }
  },
  methods: {
  },
}
</script>

<style lang="style.scss">
@import '../assets/scss/style.scss';

/* 슬라이드 */
#slider {
  margin: 0 auto;
  width: 540px;
  max-width: 100%;
  text-align: center;
}

#slider input[type=radio] {
  display: none;
}

#slider label {
  cursor: pointer;
  text-decoration: none;
}

#slides {
  padding: 10px;
  border: 3px solid #F5F5F5;
  background: #fff;
  position: relative;
  z-index: 1;
  border-radius: 25px;
}
#overflow {
  width: 100%;
  overflow: hidden;
}

#slide1:checked ~ #slides .inner{
  margin-left: 0;
}
#slide2:checked ~ #slides .inner{
  margin-left: -100%;
}
#slide3:checked ~ #slides .inner{
  margin-left: -200%;
}

#slides .inner {
  transition: margin-left 800ms cubic-bezier(0.0770, 0.000, 0.175, 1.000);
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

#slides .slide_1{
  background: rgb(53, 144, 144);
}
#slides .slide_2{
  background: lightskyblue;
}
#slides .slide_3{
  background: mediumturquoise;
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
  opacity: .4;
}
#controls label:hover {
  opacity: 1;
}

#slide1:checked ~ #controls label:nth-child(2),
#slide2:checked ~ #controls label:nth-child(3),
#slide3:checked ~ #controls label:nth-child(1)
{
  background: url(https://image.flaticon.com/icons/svg/130/130884.svg) no-repeat;
  float: right;
  margin: 0 -50px 0 0;
  display: block;
}
#slide1:checked ~ #controls label:nth-child(3),
#slide2:checked ~ #controls label:nth-child(1),
#slide3:checked ~ #controls label:nth-child(2)
{
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
  background: #F5F5F5;
  margin: 0 8px;
}

#slide1:checked ~ #bullets label:nth-child(1),
#slide2:checked ~ #bullets label:nth-child(2),
#slide3:checked ~ #bullets label:nth-child(3)
{
  background: rgb(124, 124, 124);
}

/*국회의원 검색*/
.politician-search {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    top: 30px;
    width: 540px;
}

.politician-search-form__text-input {
    align-items: center;
    width: 478px;
    height: 34px;
    left: 16px;
    top: 297px;
    padding: 4px 0 4px 14px;

    background: #F5F5F5;
    border-radius: 55px;
}

.politician-search-form__text-input::placeholder{
    font-family: 'Noto Sans KR';
    font-style: normal;
    font-weight: 300;
    font-size: 16px;
    line-height: 19px;

    letter-spacing: -0.024em;
    color: #A9A9A9;
}

.search-button img{
    width: 25px;
    height: 25px;
    margin-left: 14px;
    vertical-align: middle;
}

/*인기 검색 국회의원*/
.trend-top4-politician-title {
    max-width: 540px;
    width: 100%;
    margin: 0 auto;
    top: 60px;
    position: relative;
}

.icon-button {
    position: absolute;
}

.icon-button img {
    width: 25px;
    height: 25px;
    filter: invert(12%) sepia(98%) saturate(7493%) hue-rotate(1deg) brightness(102%) contrast(106%);
}

.trend-top4-politician-title h2{
    position: absolute;
    left: 36px;
    vertical-align: middle;

    font-family: 'Noto Sans KR';
    font-style: normal;
    font-weight: 500;
    font-size: 21px;
    line-height: 23px;
    color: #2B2B2B;
}

/*인기검색 국회의원 리스트*/
.trend-top4-politician-list{
    position: relative;
    top: 95px;
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
    font-family: 'Noto Sans KR';
    font-style: normal;
    font-weight: 500;
    color: #000000;
}

/*오늘의 국회 일정*/
.parliamentary-schedule-title {
    max-width: 540px;
    width: 100%;
    margin: 0 auto;
    top: 148px;
    position: relative;
}

.icon-bookmark {
    position: absolute;
}

.icon-bookmark img {
    width: 30px;
    height: 30px;
    filter: invert(13%) sepia(100%) saturate(6592%) hue-rotate(259deg) brightness(90%) contrast(126%);
}

.parliamentary-schedule-title h2{
    position: absolute;
    left: 36px;
    vertical-align: middle;

    font-family: 'Noto Sans KR';
    font-style: normal;
    font-weight: 500;
    font-size: 21px;
    line-height: 23px;
    color: #2B2B2B;
}

.parliamentary-schedule-title h3 {
    position: absolute;
    left: 464px;

    vertical-align: middle;
    font-family: 'Noto Sans KR';
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 23px;
    color: #818181;
}

.parliamentary-schedule-list{
    position: relative;
    top: 190px;
    width: 100%;
    max-width: 540px;
    height: 120px;
    display: flex;
    justify-content: center;
}

.parliamentary-schedule {
    width: 96px;
    height: 76px;

    position: relative;
    justify-content: space-between;
    margin: 6px;
    display: flex;
    flex-direction: column;
    align-items: center;

    background: #F7F7F7;
    border-radius: 12px;
}

.parliamentary-schedule h2{
    position: absolute;
    top: 12px;
    font-family: 'Noto Sans KR';
    font-style: normal;
    font-weight: 400;
    font-size: 13px;
    line-height: 14px;
    text-align: center;
    letter-spacing: -0.024em;
    color: #7B7B7B;
}

.parliamentary-schedule div{
    position: absolute;
    top: 35px;
    font-family: 'Noto Sans KR';
    font-style: normal;
    font-weight: 500;
    font-size: 23px;
    line-height: 23px;
    text-align: center;
    letter-spacing: -0.024em;

    color: #111111;
}
</style>
