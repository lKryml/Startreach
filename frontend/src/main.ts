import { createApp } from "vue"
import { createPinia } from "pinia"
import { i18n } from "@/_libs/i18n"

import { QuillEditor } from "@vueup/vue-quill"
import "@vueup/vue-quill/dist/vue-quill.snow.css"
import VueDatePicker from "@vuepic/vue-datepicker"
import "@vuepic/vue-datepicker/dist/main.css"

import "./assets/style.css"
import App from "./App.vue"
import router from "./router"

const pinia = createPinia()
const app = createApp(App)

app.component("VueDatePicker", VueDatePicker)
app.component("QuillEditor", QuillEditor)

app.config.errorHandler = (err, cmp, info) => {
	console.log("Error: ", err)
	console.log("Component (had Error): ", cmp)
	console.log("Info: ", info)
}
app.use(pinia).use(i18n).use(router).mount("#app")
