<template>
    <!--헤더-->
    <header class="header header-home">
            <div class="header-logo"></div>
            <h2>FRANKLY</h2>
    </header>
</template>

<style lang="style.scss">
@import '../assets/scss/style.scss';
@import url('https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR&display=swap');

/*홈 헤더*/
.header-home {
    display: flex;
    align-items: center;
    justify-content: center;
}

.header-logo {
    display: flex;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
    width: 24px;
    height: 24px;
    background-image: url(../assets/icon/franlogo_black.svg);
    background-size: cover;
}

.header-home h2 {
    padding-left: 18px;
    font-size: 24px;
    font-family: 'Sunflower';
    font-style: normal;
    font-weight: 700;
    line-height: 23px;
    vertical-align: middle;
}
</style>