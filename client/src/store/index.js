import { createStore } from 'vuex'

export default createStore({
  //여러 컴포넌트에서 공유할 공동의 상태
  state: {
    userEmail: null,
    userPassword: null,
    token: null,
  },
  //공동의 상태를 계산하여 state의 값을 반환
  getters: {

  },
  //state를 변경시키기 위한 유일한 방법
  mutations: {
    loginSuccess(state, payload) {
      state.isLogin = true
      state.userInfo = payload
    },
    logout(state) {
      state.isLogin = false
      state.userInfo = null
      localStorage.removeItem("access_token")
    }
  },
  //비동기적 로직 정의
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
