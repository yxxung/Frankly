import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios"
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import * as d3 from "d3"

axios.defaults.baseURL = 'https://teamfrankly.kr'
//axios.defaults.baseURL = 'http://localhost:8081'
//createApp(App).use(store).use(router).mount('#app')
const app = createApp(App)
app.config.globalProperties.$axios = axios;
app.use(store).use(router).use(BootstrapVue3).use(d3).mount('#app');

const token = sessionStorage.getItem("token");

axios.defaults.headers.common["Authorization"] = token ? ('Bearer ' + token) : null;
