<template>
  <body>
  <div class="wrap">
    <!--헤더-->
    <header class="header header__community">
      <h2 class="community-title">커뮤니티</h2>
    </header>

    <div class="community-list">
      <h4>일반 커뮤니티</h4>
      <ul>
        <li><router-link to="/HotBoard"><img src="@/assets/icon/Fire.svg" style="filter: invert(45%) sepia(59%) saturate(5685%) hue-rotate(340deg) brightness(108%) contrast(103%);" alt="">인기게시글</router-link></li>
        <li><router-link to="/FreeBoard"><img src="@/assets/icon/Document.svg" alt="">자유게시판</router-link></li>
      </ul>
    </div>

    <div class="community-list">
      <h4>지역 커뮤니티</h4>
      <ul>
        <li><router-link to="/SeoulBoard"><img src="@/assets/icon/Location.svg" alt="">서울특별시</router-link></li>
        <li><router-link to="/BusanBoard"><img src="@/assets/icon/Location.svg" alt="">부산광역시</router-link></li>
        <li><router-link to="/DaeguBoard"><img src="@/assets/icon/Location.svg" alt="">대구광역시</router-link></li>
        <li><router-link to="/IncheonBoard"><img src="@/assets/icon/Location.svg" alt="">인천광역시</router-link></li>
        <li><router-link to="/GwangjuBoard"><img src="@/assets/icon/Location.svg" alt="">광주광역시</router-link></li>
        <li><router-link to="/DaejeonBoard"><img src="@/assets/icon/Location.svg" alt="">대전광역시</router-link></li>
        <li><router-link to="/UlsanBoard"><img src="@/assets/icon/Location.svg" alt="">울산광역시</router-link></li>
        <li><router-link to="/SejongBoard"><img src="@/assets/icon/Location.svg" alt="">세종특별자치시</router-link></li>
        <li><router-link to="/GyeonggiBoard"><img src="@/assets/icon/Location.svg" alt="">경기도</router-link></li>
        <li><router-link to="/GangwonBoard"><img src="@/assets/icon/Location.svg" alt="">강원도</router-link></li>
        <li><router-link to="/ChungbukBoard"><img src="@/assets/icon/Location.svg" alt="">충청북도</router-link></li>
        <li><router-link to="/ChungnamBoard"><img src="@/assets/icon/Location.svg" alt="">충청남도</router-link></li>
        <li><router-link to="/JeonbukBoard"><img src="@/assets/icon/Location.svg" alt="">전라북도</router-link></li>
        <li><router-link to="/JeonnamBoard"><img src="@/assets/icon/Location.svg" alt="">전라남도</router-link></li>
        <li><router-link to="/GyeongbukBoard"><img src="@/assets/icon/Location.svg" alt="">경상북도</router-link></li>
        <li><router-link to="/GyeongnamBoard"><img src="@/assets/icon/Location.svg" alt="">경상남도</router-link></li>
        <li><router-link to="/JejuBoard"><img src="@/assets/icon/Location.svg" alt="">제주특별자치도</router-link></li>
      </ul>
    </div>

    <div class="community-list">
      <h4>내 기록</h4>
      <ul>
        <li><router-link to="/MyWriteBoard"><img src="@/assets/icon/Document.svg" alt="">내가 쓴 글</router-link></li>
        <li><router-link to="/MyReplyBoard"><img src="@/assets/icon/Document.svg" alt="">댓글 단 글</router-link></li>
      </ul>
    </div>
    <Navigation />
  </div>
  </body>
</template>

<script>
import Navigation from '@/components/Navigation.vue'
export default {
  name: 'MainBoard',
  components: {
    'Navigation': Navigation
  }
}
</script>

<style>
@import '@/assets/scss/style.scss';
/*
게시판 목록
*/
.community-list {
  padding: 8px 24px;
}
.community-list > h4 {
  font-family: 'Noto Sans KR';
  margin-bottom: 8px;
  font-size: 14px;
  font-weight: normal;
  color: #818181;
}
.community-list a {
  font-family: 'Noto Sans KR';
  padding: 8px;
  display: flex;
  align-items: center;
  color: #2B2B2B;
  font-size: 16px;
  text-decoration: none;
}
.community-list a:hover {
  background-color: #f8f8f8;
}
.community-list img {
  margin-right: 8px;
}
</style>
