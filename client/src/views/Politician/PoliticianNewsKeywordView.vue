<!--
https://bootstrap-vue.org/docs/components/table#rubin-kincade
-->
<template>
  <!-- Main table element -->
  <b-container fluid>
    <div>
    <b-col >
      <b-row class="m-1" v-for="(value, key) in this.keywordList" :key="key">
        <b-button  variant="outline-secondary" size="sm" v-on:click="getFinalNewsList(value)" v-if="!(value === 'else' ) ">{{value}}</b-button>
      </b-row>
    </b-col>
    </div>
    <b-table
      :items="newsList"
      :fields="fields"
      :busy ="isBusy"
      :fixed="true"
      stacked="md"
      show-empty
      empty-text = "날짜와 키워드를 선택해 주세요"
      sticky-header="300px"
      small
      @filtered="onFiltered"
      max
    >
      <template #table-busy>
        <div class="text-center text-danger my-2">
          <b-spinner class="align-middle"></b-spinner>
          <strong>Loading...</strong>
        </div>
      </template>

      <template #cell(name)="row">
        {{ row.value.first }} {{ row.value.last }}
      </template>

      <template #cell(actions)="row" >
        <!--      <b-button size="sm" @click="info(row.item, row.index, $event.target)" class="mr-1">-->
        <!--        Info modal-->
        <!--      </b-button>-->
        <b-button variant="warning" v-on:click="goLink(row.item)" size="sm" class="mr-1" style="width: 3rem" >
          링크
       </b-button>

      </template>

      <template #row-details="row">


        <b-card>
          <ul>
            <li v-for="(value, key) in row.item" :key="key">
              <span v-if="!key.endsWith('ID') && key !== '_showDetails'">{{key}}</span> <br>
              <!--                Original Value : {{value}} <br>-->
              <textarea property="value" v-model="row.item[key]" v-if="!key.endsWith('ID') && key !== '_showDetails'" @Change="onChange(key,$event)" >{{value}}</textarea>
              <!--            <b-form-textarea>{{value}}</b-form-textarea>-->
            </li>


          </ul>

        </b-card>

      </template>
    </b-table>
<!--    <b-pagination-->
<!--      v-model="currentPage"-->
<!--      :total-rows="totalRows"-->
<!--      :per-page="perPage"-->
<!--      align="fill"-->
<!--      size="sm"-->
<!--      class="my-0"-->
<!--    ></b-pagination>-->

  </b-container>
  <div class="empty-box"></div>
</template>

<script>
import ModalEditPolitician from "@/views/Admin/ModalEditPolitician";
import axios from "axios";

export default {
  name: "EditPolitician",
  props: {
    propInfos : Array,
    select : String,
    fields : Array,
    keywordList: Array,
    isBusy: Boolean
  },
  components: {
    ModalEditPolitician
  },
  data(){
    return{
      totalRows: 1,
      perPage: 5,
      currentPage: 1,
      newsList : []
    }

  },
  mounted() {

  },
  beforeUpdate() {
    this.totalRows = this.propInfos.length
  },
  methods:{
    goLink(newsInfo) {
      window.open(newsInfo["newsURL"])},
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = this.propInfos.length
      this.currentPage = 1
    },
    getFinalNewsList(keyword){
      let resultArray = []
      let newsJson;
      let searchKeyword = keyword;
      if(keyword === "그 외 기사들"){
        searchKeyword = "else"
      }
      for(newsJson of this.propInfos){
        if(newsJson["newsKeyword"] === searchKeyword){
          newsJson["newsTitle"] = newsJson["newsTitle"].replace(/(<([^>]+)>)/ig,"");
          newsJson["newsTitle"] = newsJson["newsTitle"].replace(/(&lt;[^\&]*&gt;)/g, "");
          resultArray.push(newsJson);
        }
        this.newsList = resultArray
      }
    }
  }
}
</script>

<style scoped>

.btn-space {
  margin-bottom: 5px;
}
</style>
