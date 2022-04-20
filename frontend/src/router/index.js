import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/category',
    name: 'category',
    component: () => import('../views/CategoryView.vue')
  },
  {
    path: '/category/:id',
    name: 'category-detail',
    component: () => import('../views/CategoryDetailView.vue')
  },
  {
    path: '/todo',
    name: 'todo',
    component: () => import('../views/TodoView.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
