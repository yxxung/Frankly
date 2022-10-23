import { createStore } from 'vuex'

export default createStore({
  state: {
    userInfo: null,
    isLogin: false
  },

  getters: {

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
