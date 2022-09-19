<template>
    <body>
        <div class="wrap">
            <!--국회의원 검색-->
            <div class="politician-search">
                <form class="politician-search-form" action="" method="get">
                    <input class="politician-search-form__text-input" type="text" placeholder="국회의원 검색">
                    <button class="search-button" type="submit" name="click"><img src="@/assets/icon/button.svg"></button>
                </form>
            </div>

            <div class="political-party-list">
                <h2>대한민국 정당</h2>
                <Slider />
            </div>

            <div class="politician-title">
                <h2>전체 국회의원</h2>
                <h3>가나다 순</h3>
            </div>

            <div class="all-politician-list">
                <PoliticianList />
            </div>

            <Navigation />
        </div>
    </body>
</template>

<script>
import Navigation from '@/components/Navigation.vue'
import Slider from '@/components/Slider.vue'
import PoliticianList from '@/views/Politician/PoliticianList.vue'
export default {
  name: 'Politician',
  components: {
    'Navigation': Navigation,
    'PoliticianList': PoliticianList,
    'Slider': Slider
  }
}
</script>

<style lang="style.scss">
@import "@/assets/scss/style.scss";

/*국회의원 검색*/
.politician-search {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    top: 0px;
    padding: 8px 24px;
}

.politician-search-form__text-input {
    align-items: center;
    width: 448px;
    height: 38px;
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

/*대한민국 정당*/
.political-party-list {
    padding: 8px 24px;
}

.political-party-list > h2 {
    padding-top: 10px;
    font-family: 'Noto Sans KR';
    font-style: normal;
    font-weight: 700;
    font-size: 24px;
    line-height: 26px;
    letter-spacing: -0.024em;

    color: #2B2B2B;
}

.politician-title {
    padding: 8px 24px;
    justify-content: space-evenly;
    align-items: center;
}

.politician-title > h2 {
    padding-top: 10px;
    font-family: 'Noto Sans KR';
    font-style: normal;
    font-weight: 700;
    font-size: 24px;
    line-height: 26px;
    letter-spacing: -0.024em;

    color: #2B2B2B;
}

.politician-title > h3 {
    right: 0;
    display: flex;
    font-size: 14px;
    line-height: 26px;
    letter-spacing: -0.024em;
    font-weight: 00;

    color: #818181;
}

.all-politician-list {
    padding: 8px 24px;
}
</style>