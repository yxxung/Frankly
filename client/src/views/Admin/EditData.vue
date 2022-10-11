<template>
  <AdminNav />

  <div class="hello">
    <b-card
      header="정치인 데이터 관리"
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
    <EditDataDetail v-bind:propInfos="infos" v-bind:select="selected" v-bind:fields="fields"></EditDataDetail>
      <!-- 페이징 처리-->

    </b-card>
  </div>
</template>

<script>
import AdminNav from "@/components/AdminNav.vue";
import axios from "axios";
import EditDataDetail from "@/views/Admin/EditDataDetail";

export default {
  name: "EditData",
  components: {
    AdminNav,
    EditDataDetail
  },
  data() {

    return {
      infos: [],
      inputValue:'',
      selected: null,
      options: [
        { value: 'politician', text: '정치인 기본정보' },
        { value: 'property', text: '재산 데이터' },
        { value: 'vote', text: '표결정보 (국회의원 ID 입력)' },
        { value: 'schedule', text: '본희의정보' },
        { value: 'attendance', text: '출석정보 (국회의원 ID 입력)' }
      ],
      fields:[]
      ,
      politicianFields : [
        {
          key: 'politicianID',
          sortable: true,
          sortDirection: 'desc'
        },
        {
          key: 'politicianName',
          sortable: true
        },
        {
          key: 'partyName',
          sortable: true,
        },
        {
          key: 'sex',
          sortable: false,
        },
        {
          key:"actions",
          label:"Actions"
        }
      ],
      voteFields : [
        {
          key: 'voteID',
          sortable: true,
          sortDirection: 'desc'
        },
        {
          key: 'politicianID',
          sortable: true
        },
        {
          key: 'billNumber',
          sortable: true,
        },
        {
          key: 'voteResult',
          sortable: false,
        },
        {
          key:"actions",
          label:"Actions"
        }
      ],
      attendacneFields : [
      {
        key: 'attendanceID',
        sortable: true,
        sortDirection: 'desc'
      },
      {
        key: 'c',
        sortable: true
      },
      {
        key: 'politicianID',
        sortable: true,
      },
      {
        key:"actions",
        label:"Actions"
      }
      ]
    };
  },
  methods: {
    getInfo: function (){
      var requestURL = '/api/' + this.selected +"/"+ this.inputValue
      this.infos = []

      if(this.selected === "politician"){
        this.fields = this.politicianFields

      }else if(this.selected === "vote"){

        this.fields = this.voteFields
        requestURL = '/api/' + this.inputValue +"/"+ this.selected

      }else if(this.selected === "attendance"){
        this.fields = this.attendacneFields
        requestURL = '/api/' + this.inputValue +"/"+ "attend"
          // this.selected
      }

      axios.get(requestURL)
        .then(response => {
          if( response.data instanceof Array){
            this.infos = response.data
          }else(
            this.infos.push(response.data)
          )

          console.log(this.infos)
        })
        .catch(e => {
          console.log('error:', e)
          console.log(this.inputValue + "request")
        })

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
