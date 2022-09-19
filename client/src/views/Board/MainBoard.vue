<template>
    <body>
        <div class="wrap">
            <!--헤더-->
            <header class="header header__community">
                <h2 class="community-title">커뮤니티</h2>
                <a class="icon-button-56" href="index.html">
                    <img src="@/assets/icon/Bullhorn.svg" alt="공지사항">
                </a>
            </header>

            <div class="community-list">
                <h4>일반 커뮤니티</h4>
                <ul>
                    <li><a href="/HotBoard"><img src="@/assets/icon/Pin.svg" alt="">인기게시글</a></li>
                    <li><a href="/FreeBoard"><img src="@/assets/icon/Pin.svg" alt="">자유게시판</a></li>
                </ul>
            </div>

            <div class="community-list">
                <h4>지역 커뮤니티</h4>
                <ul>
                    <li><a href="/board/${board.region}"><img src="@/assets/icon/Pin.svg" alt="">서울특별시</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">부산광역시</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">대구광역시</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">인천광역시</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">광주광역시</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">대전광역시</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">울산광역시</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">세종특별자치시</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">경기도</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">강원도</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">충청북도</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">충청남도</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">전라북도</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">전라남도</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">경상북도</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">경상남도</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">제주특별자치도</a></li>
                </ul>
            </div>

            <div class="community-list">
                <h4>내 기록</h4>
                <ul>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">내가 쓴 글</a></li>
                    <li><a href="#"><img src="@/assets/icon/Pin.svg" alt="">댓글 단 글</a></li>
                </ul>
            </div>
            <Navigation />
        </div>
    </body>
</template>

<script>
import Navigation from '@/components/Navigation.vue'
export default {
  name: 'Board',
  components: {
    'Navigation': Navigation
  }
}
</script>

<style lang="style.scss">
@import '@/assets/scss/style.scss';

/*
게시판 목록
*/

.community-list {
    padding: 8px 24px;
}

.community-list > h4 {
    margin-bottom: 8px;
    font-size: 14px;
    font-weight: normal;
    color: #818181;
}

.community-list a {
    padding: 8px;
    display: flex;
    align-items: center;
    color: #2B2B2B;
    font-size: 16px;
}
.community-list a:hover {
    background-color: #f8f8f8;
}
.community-list img {
    margin-right: 8px;
}
</style>
