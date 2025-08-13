import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './style.css'
import router from './router'
import App from './App.vue'
import  { userAuthStore } from './store/auth'


const app = createApp()

app.use(createPinia())
app.use(router)

const authStore = userAuthStore()
authStore.setCsrfToken()

app.mount('#app')
