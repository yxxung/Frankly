<!--
https://bootstrap-vue.org/docs/components/table#rubin-kincade
-->
<template>
  <!-- Main table element -->
  <b-container fluid>
    <b-table
      :items="propInfos"
      :fields="fields"
      :per-page="perPage"
      :current-page="currentPage"
      stacked="md"
      show-empty
      small
      @filtered="onFiltered"
    >

      <template #cell(name)="row">
        {{ row.value.first }} {{ row.value.last }}
      </template>

      <template #cell(actions)="row">
        <!--      <b-button size="sm" @click="info(row.item, row.index, $event.target)" class="mr-1">-->
        <!--        Info modal-->
        <!--      </b-button>-->
        <b-button @click="row.toggleDetails" class="m-3" variant="warning">
          {{ row.detailsShowing ? '접기' : '수정' }}
        </b-button>

        <b-button v-on:click="doRemove(row.item)" variant="danger">
          삭제
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

            <b-overlay :show="editButtonshow">
              <b-row>
                <b-button

                  :aria-hidden="editButtonshow ? 'true' : null"
                  squared variant="outline-danger"
                  v-on:click="doChange(row.item)">수정</b-button >
              </b-row>
            </b-overlay>


          </ul>

        </b-card>



      </template>
    </b-table>
    <b-pagination
      v-model="currentPage"
      :total-rows="totalRows"
      :per-page="perPage"
      align="fill"
      size="sm"
      class="my-0"
    ></b-pagination>
  </b-container>

</template>

<script>
import axios from "axios";

export default {
  name: "EditBoardListView",
  props: {propInfos : Array},
  components: {

  },
  data(){
    return{
      editButtonshow: false,
      totalRows: 1,
      perPage: 15,
      currentPage: 1,
      fields: [
        {
          key: 'boardID',
          sortable: true,
          sortDirection: 'desc'
        },
        {
          key: 'userID',
          sortable: true
        },
        {
          key: 'title',
          sortable: true,
        },
        {
          key: 'regDate',
          sortable: false,
        },
        {
          key:"actions",
          label:"Actions"
        }
      ],
      // politicianInfo : []

    }

  },
  // computed: {
  //   copyProps: function(){
  //     this.politicianInfo = this.propInfos
  //   }
  // },
  beforeUpdate() {
    this.totalRows = this.propInfos.length
  },
  methods:{
    doChange: function(boardInfo) {
      this.editButtonshow = true

      if (!confirm("정말 수정 하시겠습니까?")) {
        this.editButtonshow = true
        alert("취소(아니오)를 누르셨습니다.");
        this.editButtonshow = false;
      } else {
        this.editButtonshow = true
        console.log(boardInfo)

        axios.put('/api/boards/'+ boardInfo["boardID"], boardInfo, {
          headers: { "Content-Type": `application/json`}
        })
          .then(response => {
            if(response.status == 200){
              for(let i = 0; i < this.propInfos.length; i++) {
                if(this.propInfos[i]["boardID"] === boardInfo["boardID"])  {
                  this.propInfos.splice(i, 1);
                  i--;
                }
              }
              alert("수정되었습니다.")
              this.editButtonshow = false;
            }else{
              alert( " 응답 코드" + response.status)
              this.editButtonshow = false;

            }
          })
          .catch(e => {
            console.log('error:', e)
            console.log(this.inputValue + "request")
          })
      }

    },
    //삭제
    doRemove:  function(boardInfo) {

      if (!confirm("정말 삭제 하시겠습니까?")) {
        alert("취소(아니오)를 누르셨습니다.");
      } else {
        axios.delete('/api/boards/'+ boardInfo["boardID"] )
          .then(response => {
            if(response.status == 200){
              for(let i = 0; i < this.propInfos.length; i++) {
                if(this.propInfos[i]["boardID"] === boardInfo["boardID"])  {
                  this.propInfos.splice(i, 1);
                  i--;
                }
              }
              alert("삭제되었습니다.")
            }else{
              alert( " 응답 코드" + response.status)

            }

          })
          .catch(e => {
            console.log('error:', e)
            console.log(this.inputValue + "request")
          })
      }

    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = this.propInfos.length
      this.currentPage = 1
    }

  }
}
</script>

<style scoped>

</style>
