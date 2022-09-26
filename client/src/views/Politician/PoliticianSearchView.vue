<template>
  <div class="searchresult">
    <SearchBar />
    <h2>검색 결과</h2>
    <div class="all-politician-list">
        <!--click 시 상세정보로 넘어가게 해야 함-->
        <div
          class="politician"
          v-for="politician in $store.getters.getFilteredProduct(searchKeyword)"
          :key="politician.politicianID"
        >
          <!-- 정치인 리스트 출력 -->
          <img
            :src="require(`@/assets/politician/${politician.politicianImage}`)"
          />
          <p>{{ politicians.politicianName }}</p>
        </div>
      </div>
  </div>
</template>
<script>
import SearchBar from '@/components/SearchBar.vue'

export default {
  name: "PoliticianSearchView",
  components: {
    SearchBar: SearchBar
  },
  props: ["searchKeyword"], //상위 컴포넌트인 Politician.vue로부터 데이터 받음
  data() {
    return {};
  },
  methods: {},
};
</script>