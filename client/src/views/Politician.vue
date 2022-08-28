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

            <div class="politician-title">
                <h2>대한민국 정당</h2>
            </div>

            <div class="political-party-list">
            </div>

            <div class="politician-title">
                <h2>전체 국회의원</h2>
                <h3>가나다 순</h3>
            </div>

            <div class="all-politician-list">

            </div>
            <Navigation />
        </div>
    </body>
</template>

<script>
import Navigation from '@/components/Navigation.vue'
import PoliticianList from '@/components/PoliticianList/PoliticianList.vue'
export default {
  name: 'Politician',
  components: {
    'Navigation': Navigation,
    'PoliticianList': PoliticianList
  }
}
</script>

<style lang="style.scss">
@import "../assets/scss/style.scss";

/*국회의원 검색*/
.politician-search {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    top: 0px;
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

/*대한민국 정당*/

</style>