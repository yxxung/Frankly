<template>
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
            <b-col sm="3"><b-form-select v-model="selected" :options="options"></b-form-select></b-col>
            <b-col sm="7">
              <b-form-input
                v-model="inputValue"
                type="search"
                placeholder="검색어를 입력하세요"
              />
              <!--    v-bind:value = "inputValue"-->
              <!--    v-on:input="getInput"-->
            </b-col>
            <b-col sm="2">
              <b-button variant="outline-primary" v-on:click="getInfo">검색</b-button>
            </b-col>
          </b-row>
        </b-container>
      </b-form-group>
      <EditUserDetail v-bind:propInfos="infos"></EditUserDetail>
      <!-- 페이징 처리-->

    </b-card>
  </div>
</template>

<script>
import AdminNav from "@/components/AdminNav.vue";
import axios from "axios";
import EditUserDetail from "@/views/Admin/EditUserDetail";

export default {
  name: 'EditData',
  components: {
    AdminNav,
    EditUserDetail
  },
  data() {

    return {
      infos: [],
      inputValue:'',
      selected: null,
      options: [
        { value: '1', text: '회원 ID' },
        { value: '2', text: '회원 이름' },
        // { value: '3', text: '표결정보' },름
        // { value: '4', text: '본희의정보' },
        // { value: '5', text: '출석정보' }
      ]
    };
  },
  methods: {
    getInfo: function (){
      this.infos = []
      if(this.selected === "1") {
        axios.get('/api/users/' + this.inputValue)
          .then(response => {
            if (response.data instanceof Array) {
              this.infos = response.data
            } else (
              this.infos.push(response.data)
            )
            console.log(this.infos)
          })
          .catch(e => {
            console.log('error:', e)
            console.log(this.inputValue + "request")
          })
      }else{
        axios.get('/api/users/' + this.inputValue + '/name')
          .then(response => {
            if (response.data instanceof Array) {
              this.infos = response.data
            } else (
              this.infos.push(response.data)
            )
            console.log(this.infos)
          })
          .catch(e => {
            console.log('error:', e)
            console.log(this.inputValue + "request")
          })
      }
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
      return this.infos.length
    }
  }
};
</script>

<style>
</style>
