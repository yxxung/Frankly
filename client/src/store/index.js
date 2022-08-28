import { createStore } from 'vuex'

export default createStore({
  state: {
    access_token: sessionStorage.getItem("access_token"),
    refresh_token: sessionStorage.getItem("refresh_token"),
    expires_in: "",
    claims: JSON.parse(sessionStorage.getItem("claims")),
    intervalId: null
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
