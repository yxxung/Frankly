import { createStore } from 'vuex'

export default createStore({
  state: {
    userInfo: null,
    isLogin: false
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
    oginSuccess(state, payload) {
      state.isLogin = true
      state.userInfo = payload
    },
    logout(state) {
      state.isLogin = false
      state.userInfo = null
      localStorage.removeItem("access_token")
    }
  },
  actions: {
    getAccountInfo({ commit }) {
      let token = localStorage.getItem("access_token")
      axios
        .get("/userinfo", {
          headers: {
            "X-AUTH-TOKEN": token
          }
        })
        .then((response) => {
          commit("loginSuccess", response.data.data)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  modules: {
  }
})
