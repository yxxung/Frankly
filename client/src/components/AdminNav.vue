<template>
  <div class="admin-nav">
    <b-nav tabs fill style="margin: auto; padding: 10px">
      <b-nav-item href="/AdminBoard">관리자 페이지</b-nav-item>
      <b-nav-item href="/EditUser">회원 관리</b-nav-item>
      <b-nav-item href="/EditBoard">게시글 관리</b-nav-item>
      <b-nav-item href="/DataExtract">데이터 추출</b-nav-item>
      <b-nav-item href="/EditData">데이터 관리</b-nav-item>
    </b-nav>
  </div>
</template>

<script>
export default {
  name: "AdminNav"
};
</script>

<style>
</style>
