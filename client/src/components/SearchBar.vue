<template>
  <div class="politician-search">
    <form class="politician-search-form" action="" method="get">
      <input
        class="politician-search-form__text-input"
        type="text"
        placeholder="국회의원 검색"
        v-model="politicianKeyword"
        @keyup.enter="searchResultShow(searchKeyword)"
      /><!--엔터 클릭시 searchresultshow 실행-->
      <button
        class="search-button"
        type="submit"
        @click="searchResultShow(searchKeyword)"
      ><!--버튼 클릭시 searchresultshow 실행-->
        <img src="@/assets/icon/button.svg" />
      </button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchKeyword: "",
    };
  },
  methods: {
    searchResultShow(searchKeyword) {
      if (searchKeyword !== "") {
        this.router.push({
            name: 'Politician',
            params: {
                searchKeyword: this.searchKeyword,
                isResultShow: true
            }
        });
        this.searchKeyword = ''
        console.log('"', searchKeyword, '"' + '검색')
      } else {
        alert('검색어를 입력해주세요 !')
      }
    },
  },
};
</script>

<style>
/*국회의원 검색*/
.politician-search {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  padding: 8px 24px;
  margin-top: -30px;
}

.politician-search-form__text-input {
  align-items: center;
  width: 448px;
  height: 38px;
  left: 16px;
  top: 297px;
  padding: 4px 0 4px 18px;
  border: none;
  outline: none;
  background: #f5f5f5;
  border-radius: 55px;
}

.politician-search-form__text-input::placeholder {
  font-family: "Noto Sans KR";
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;

  letter-spacing: -0.024em;
  color: #a9a9a9;
}

.search-button img {
  width: 25px;
  height: 25px;
  margin-left: 14px;
  vertical-align: middle;
}

</style>