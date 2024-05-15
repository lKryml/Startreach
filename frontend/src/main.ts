import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { i18n } from '@/libs/i18n';

import "./assets/style.css"
import App from './App.vue'
import router from './router'


const pinia = createPinia()
const app = createApp(App)

app.config.errorHandler = (err, cmp, info) => {
    console.log("Error: ", err)
    console.log("Component (had Error): ", cmp)
    console.log("Info: ", info)
}
app.use(pinia)
    .use(i18n)
    .use(router)
    .mount('#app')
