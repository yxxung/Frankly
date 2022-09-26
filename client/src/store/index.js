import { createStore } from 'vuex'

export default createStore({
  state: {
    access_token: sessionStorage.getItem("access_token"),
    refresh_token: sessionStorage.getItem("refresh_token"),
    expires_in: "",
    claims: JSON.parse(sessionStorage.getItem("claims")),
    intervalId: null
  },
  //수정 필요
  getters: {
    getFilteredProduct: (state) => (searchKeyword) => {
      const filtered = state.politicians.filter((object) =>
        object.name.toLowerCase().includes(searchKeyword.toLowerCase())
        );
      if (filtered) return filtered;
    },
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
