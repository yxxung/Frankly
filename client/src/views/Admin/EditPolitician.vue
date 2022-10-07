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

        <b-button @click="row.toggleDetails" variant="danger">
          삭제
        </b-button>

      </template>

      <template #row-details="row">


          <b-card>
            <ul>
              <li v-for="(value, key) in row.item" :key="key">
                {{key}} <br>
                Original Value : {{value}} <br>
                <textarea property="value">{{value}}</textarea>
                <!--            <b-form-textarea>{{value}}</b-form-textarea>-->
              </li>

              <b-overlay :show="editButtonshow">
                <b-row>
                  <b-button

                    :aria-hidden="editButtonshow ? 'true' : null"
                    squared variant="outline-danger"
                    @click = "editButtonshow = true"
                    v-on:click="doChange">수정</b-button >
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
import ModalEditPolitician from "@/views/Admin/ModalEditPolitician";

export default {
  name: "EditPolitician",
  props: ['propInfos'],
  components: {
    ModalEditPolitician
  },
  data(){
    return{
      editButtonshow: false,
      totalRows: 1,
      perPage: 15,
      currentPage: 1,
      fields: [
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
      ]

    }

  },
  beforeUpdate() {
    this.totalRows = this.propInfos.length
  }
  ,
  methods:{
    doChange: function(userinfo) {


    },
    //삭제
    doRemove:  function(userinfo) {

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
