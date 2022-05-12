import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/tailwind.css'
import store from './store'
import axios from 'axios'
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App).use(router, axios).use(store).use(VueSidebarMenu).mount('#app')
