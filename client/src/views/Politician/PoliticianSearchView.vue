<template>
  <div class="searchresult">
    <SearchBar />
    <ul class="all-politician-list">
      <li
        class="politician"
        v-for="politician in politicians"
        v-bind:key="politician.politicianID"
        @click="goToPoliticianDetail(politician.politicianID)"
      >
        <!-- 정치인 리스트 출력 이미지, 이름-->
        <div class="politician-image">
          <img src="@/assets/politician/정진석.png" />
        </div>
        <div class="politician-name">{{ politician.politicianName }}</div>
      </li>
    </ul>
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