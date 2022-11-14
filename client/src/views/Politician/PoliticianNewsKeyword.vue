<template>
  <div class="wrap">
    <!--헤더-->
    <header class="header header--back">
      <a class="icon-button-56 header__back-button" @click="$router.go(-1)">
        <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기" />
      </a>
      <h2>국회의원 뉴스 키워드</h2>
    </header>

    <div>
      <b-nav tabs align="center">
      </b-nav>
    </div>

      <b-row class="my-3" align="center" style="padding: 0 12px 0 12px">
        <b-col cols="8" align="left"><b-form-select v-model="selected" :options="options" style="width: 50%"></b-form-select></b-col>
        <b-col cols="4" align="right">
          <b-button variant="dark" v-on:click="listReturn()">검색</b-button>
        </b-col>
      </b-row>

    <div style="width: 100% max-width: 540px margin: 10px auto" align="center">
      <PoliticianNewsKeywordView
        v-bind:propInfos="infos"
        v-bind:fields="fields"
        v-bind:keywordList="keywordList"
        v-bind:isBusy="isBusy"
      ></PoliticianNewsKeywordView>
    </div>
    <Navigation />
  </div>
</template>

<script>
import { Bar } from "vue-chartjs";
import axios from "axios";
import PoliticianNewsKeywordView from "@/views/Politician/PoliticianNewsKeywordView";
import Navigation from "@/components/Navigation.vue";
export default {
  name: "PoliticianKeywordDetail",
  components: {
    PoliticianNewsKeywordView,
    Navigation,
  },
  data() {
    return {
      perPage: 1,
      apiResult: [],
      jsonList: [],
      infos: [],
      currentPage: 1,
      rows: 1,
      years: [],
      month: [],
      selected: null,
      keywordList: [],
      fields: [
        {
          key: "newsTitle",
          label: "기사 제목",
          sortable: true,
          sortDirection: "desc",
        },
        {
          key: "actions",
          label: "   ",
        },
        // {
        //   key: 'newsKeyword',
        //   sortable: true
        // },
        // {
        //   key: 'newsURL',
        //   sortable: true,
        // },
        // {
        //   key: 'sex',
        //   sortable: false,
        // },
        // {
        //   key:"actions",
        //   label:"Actions"
        // }
      ],
      options: [],
      isBusy: true,
    };
  },
  beforeCreate() {
    const politicianID = this.$route.params.politicianID;
    let keywordResult = [];
    // this.politicianPropertyChange =[]
    axios
      .get("/api/news/" + politicianID)
      .then((response) => {
        if (response.data instanceof Array) {
          this.apiResult = response.data;
        } else this.apiResult.push(response.data);
        let resultArray = new Array(3);
        for (var i = 0; i < resultArray.length; i++) {
          resultArray[i] = new Array(12);
          for (var j = 0; j < resultArray[0].length; j++) {
            resultArray[i][j] = [];
          }
        }
        // let yearSet = new Set()
        let monthSet = new Set();

        let keywordJson;
        let jsonOption = [];
        for (keywordJson of response.data) {
          let parsedDate = new Date(keywordJson["newsDate"]);
          let year = parsedDate.getFullYear() - 2020;
          if (year < 0) continue;
          let month = parsedDate.getMonth();
          resultArray[year][month].push(keywordJson);
          // let json = [{
          //   value: ''
          // }]
          // yearSet.add(year);
          let yearMonth = String(year + 2020) + " " + String(month + 1);
          monthSet.add(yearMonth);
        }

        this.jsonList = resultArray;
        // let yearList = []
        let optionList = [];
        // yearSet.forEach(function(val) {
        //   yearList.push(val);
        // });
        monthSet.forEach(function (val) {
          let splitString = val.split(" ");
          let json = {
            value: val,
            text: splitString[0] + "년 " + splitString[1] + "월",
          };
          optionList.push(json);
        });
        this.options = optionList;
        // 초기
        this.isBusy = false;
        this.selected = optionList[0]["value"];
        this.listReturn();
        // this.years = yearList

      })
      .catch(e => {값
        console.log('error:', e)
      })
      .catch((e) => {
        console.log("error:", e);
      });
  },
  created() {
    this.rows = this.rowCount;
  },
  methods: {
    listReturn() {
      if (this.selected !== null) {
        let splited = this.selected.split(" ");
        this.infos =
          this.jsonList[parseInt(splited[0]) - 2020][parseInt(splited[1]) - 1];
      }
      let jsons;
      let keywordSet = new Set();

      for (jsons of this.infos) {
        if (jsons["newsKeyword"] !== null) {
          keywordSet.add(jsons["newsKeyword"]);
        } else {
          jsons["newsKeyword"] = "else";
        }
      }
      let keywordList = [];
      keywordSet.forEach(function (val) {
        // let splitString = val.split(" ")
        keywordList.push(val);
      });
      if (keywordList.length !== 0) {
        keywordList.push("그 외 기사들");
      }

      this.keywordList = keywordList;
    },
  },
  //수정
  doChange: function (userinfo) {},
  //삭제
  doRemove: function (userinfo) {},
};
</script>

<style>
@import '@/assets/scss/style.scss';
</style>
