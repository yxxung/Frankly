<template>
  <AdminNav />

  <div class="hello">
    <b-card
      header="회원 관리"
      style="max-width: 80rem; margin: auto; margin-top: 10vh"
      class="mb-2"
      border-variant="info"
      align="left"
    >
      <b-form-group id="board-search-input">
        <b-container fluid>
          <b-row class="my-1">
            <b-col sm="10">
              <b-form-input
                v-bind:value="inputUserInfo"
                v-on:input="updateInput"
                type="text"
                placeholder="유저 정보를 입력하세요."
              />
            </b-col>
            <b-col sm="2">
              <b-button variant="outline-primary" v-on:click="searchUser(this.inputUserInfo)">검색</b-button>
            </b-col>
          </b-row>
        </b-container>
      </b-form-group>

      <table class="edit-user-list">
        <thead>
          <tr>
            <th class="id">ID</th>
            <th class="name">이름</th>
            <th class="button">수정</th>
            <th class="button">삭제</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="userinfo in userinfos" :key="userinfo.id">
            <th>{{ userinfo.id }}</th>
            <td>{{ userinfo.name }}</td>
            <td class="button">
              <!--수정 버튼 모달-->
              <ModalEditUser v-if="doChange" @close-modal="doChange=false"></ModalEditUser>
              <button @click="doChange=true">수정</button>
              </td>
            <td class="button">
              <!--삭제 버튼 모달-->
              <button v-on:click="doRemove(userinfo)">제거</button>
              </td>
          </tr>
        </tbody>
      </table>

      <!-- 페이징 처리-->
      <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="perPage"
            size="sm"
            align="center"
            class="mt-4">
      </b-pagination>
    </b-card>
  </div>
</template>

<script>
import AdminNav from "@/components/AdminNav.vue";
import ModalEditUser from '@/views/Admin/ModalEditUser.vue'
import axios from "axios";

export default {
  name: "EditBoard",
  components: {
    AdminNav,
    ModalEditUser
  },
  data() {
    return {
      perPage: 15,
      currentPage: 1,
      userinfos: [],
      inputUserInfo : ""
    };
  },
  methods: {
    searchUser: function (input){
      axios.get('/api/users/' + input)
        .then(response => {
          this.userinfos = response.data.map(r => r.data)
        })
        .catch(e => {
          console.log('error:', e)
        })
    },
    updateInput: function (event){
      var text = event.target.value;
      this.inputUserInfo = text;
    },
    //수정
    doChange: function(userinfo) {

    },
    //삭제
    doRemove:  function(userinfo) {

    }
  },
  computed: {
    rows() {
      return this.userinfos.length
    }
  },
  created() {
    axios.get('/api/users')
    .then(response => {
      this.userinfos = response.data.map(r => r.data)
    })
    .catch(e => {
      console.log('error:', e)
    })
  },

};
</script>

<style>
</style>
