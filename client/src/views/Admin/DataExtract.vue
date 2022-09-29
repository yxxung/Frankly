<template>
  <AdminNav />

  <b-card>
    <div>
      <h4>재산 데이터</h4>
      <b-card>
        <b-card-text>
          Some quick example text to build on the card and make up the bulk of
          the card's content.
        </b-card-text>
        <b-button>데이터 추출</b-button>
      </b-card>
    </div>
    <div class="mt-4">
      <h4>의회 데이터</h4>
      <b-card>
        <b-card-text>
          Some quick example text to build on the card and make up the bulk of
          the card's content.
        </b-card-text>
        <b-button>데이터 추출</b-button>
      </b-card>
      <h4>뉴스 데이터</h4>
      <b-card>
        <b-card-text>
          Some quick example text to build on the card and make up the bulk of
          the card's content.
        </b-card-text>
        <b-button>데이터 추출</b-button>
      </b-card>
    </div>
  </b-card>
</template>

<script>
import AdminNav from "@/components/AdminNav.vue";

export default {
  name: 'DataExtract',
  components: {
    AdminNav
  },
  data() {

  },
};
</script>