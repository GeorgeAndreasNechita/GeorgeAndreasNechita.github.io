import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Lebenslauf from '../components/Lebenslauf.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/lebenslauf',
      name: 'lebenslauf',
      component: Lebenslauf
    },
    {
      path: '/project1',
      name: 'project1',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Project1.vue')
    }
  ]
})

export default router
