import {createStore} from "vuex";
import createPersistedState from "vuex-persistedstate";

import {userStore} from "@/store/modules/userStore.js";
import {userLogStore} from "@/store/modules/userLogStore.js";

export const store = createStore({
    modules: { userStore, userLogStore },
    state: {},
    getters: {},
    mutations: {},
    actions: {},
    plugins: [
      createPersistedState({
        paths: ["userStore", "userLogStore"],
        // 브라우저 종료시 제거하기 위해 localStorage가 아닌 sessionStorage로 변경. (default: localStorage)
        storage: sessionStorage,
      })
    ]
  });

  export default store