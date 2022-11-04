import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';

import userStore from '@/store/userStore.js'

const store = new Vuex.Store({
  modules: {
      userStore: userStore,
  },
  //vuex plugin 명시
  plugins: [createPersistedState({
      paths: ["userStore"]
  })]
})

export default store