import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios"
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import { BIconBatteryFull, BIconArrow90degDown, BIconBookmark } from 'bootstrap-icons-vue';
import { BootstrapIconsPlugin } from 'bootstrap-icons-vue';

axios.defaults.baseURL = 'http://localhost:8081'

//createApp(App).use(store).use(router).mount('#app')
const app = createApp(App)
app.component('BIconBatteryFull', BIconBatteryFull);
app.component('BIconArrow90degDown', BIconArrow90degDown);
app.component('BIconBookmark', BIconBookmark);
app.config.globalProperties.$axios = axios;
app.use(store).use(router).use(BootstrapVue3).use(BootstrapIconsPlugin).mount('#app');
