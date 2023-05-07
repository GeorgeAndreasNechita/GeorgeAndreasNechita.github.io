import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Lebenslauf from '../components/Lebenslauf.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/lebenslauf',
      name: 'lebenslauf',
      component: Lebenslauf
    },
    {
      path: '/arbeitszeugnis',
      name: 'Arbeitszeugnis',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../components/Arbeitszeugnis.vue')
    }
  ]
})

export default router
