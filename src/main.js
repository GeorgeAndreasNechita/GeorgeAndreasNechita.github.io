import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import './assets/main.css'

import * as vuetifyJs from './js/vuetify'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.use(vuetifyJs.vuetify).mount('#app')
