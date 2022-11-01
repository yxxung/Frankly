import { createStore } from 'vuex'
import jwt_decode from "jwt-decode";
import { findByEmail } from '@/api/users'

export default createStore({
  //여러 컴포넌트에서 공유할 공동의 상태
  state: {
    isLogin: false, //로그인 여부
    userInfo: null
  },
  //공동의 상태를 계산하여 state의 값을 반환
  getters: {

  },
  //state를 변경시키기 위한 유일한 방법
  mutations: {
    // 로그인 했는지 안했는지 상태를 지정.
    setIsLogined(state, isLogin) {
      state.isLogin = isLogin;
    },
    // 멤버정보를 state에 넣어줌
    setUserInfo(state, userInfo) {
      state.isLogin = true;
      state.userInfo = userInfo;
    },
    // 로그아웃
    // 로그인 상태를 체크하는 isLogin을 false로, memberInfo를 null로 비움으로써 초기화.
    logout(state) {
      state.isLogin = false;
      state.userInfo = null;
    }
  },
  //비동기적 로직 정의
  actions: {
    async GET_USER_INFO({ commit }, token) {
      let decode = jwt_decode(token);
      decode.email
      await findByEmail(
        decode.email,
        (response) => {
          if (response.data.message === "success") {
            commit("setUserInfo", response.data.userInfo);
            // router.push("/");
            // router.go(router.currentRoute);
          } else {
            console.log("유저 정보 없음!!");
          }
        },
        (error) => {
          console.log(error);
        }
      );
    },
    LOGOUT({ commit }) {
      commit("logout");
      localStorage.removeItem("access-token");
      // axios.defaults.headers.common["auth-token"] = undefined;
    }
  },
  modules: {
  }
})
