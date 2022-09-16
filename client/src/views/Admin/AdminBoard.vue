<template>
  <AdminNav />

  <b-card>
    <b-card title="사용자">
      <b-card-text>001</b-card-text>
      <b-card-text>회원 이름</b-card-text>
      <b-card-text>아이디</b-card-text>
      <b-dropdown right split text="수정">
        <b-dropdown-item>사용자</b-dropdown-item>
        <b-dropdown-item>관리자</b-dropdown-item>
      </b-dropdown>
    </b-card>
  </b-card>
</template>

<script>
import AdminNav from "@/components/AdminNav.vue";

export default {
  name: 'AdminBoard',
  components: {
    AdminNav
  },
  data() {

  },
};
</script>

<style>
</style>