import { createStore } from 'vuex'

export default createStore({
  //여러 컴포넌트에서 공유할 공동의 상태
  state: {
    userEmail: null,
    userPassword: null,
    token: ''
  },
  //공동의 상태를 계산하여 state의 값을 반환
  getters: {

  },
  //state를 변경시키기 위한 유일한 방법
  mutations: {
    login: function (state, payload) {
      state.userEmail = payload.userEmail
      state.userPassword = payload.userPassword
      state.token = payload.token
    },
    loginCheck: function (state) {
      if (!state.token) {
        router.push({
          name: 'Login'
        }).catch(error => {
          console.log(error)
        })
      }
    }
  },
  //비동기적 로직 정의
  actions: {

  },
  modules: {
  }
})
