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
    name: 'category-list',
    component: () => import('../views/category/CategoryListView.vue')
  },
  {
    path: '/category/:id',
    name: 'category-edit',
    component: () => import('../views/category/CategoryEditView.vue')
  },
  {
    path: '/category-add',
    name: 'category-add',
    component: () => import('../views/category/CategoryAddView.vue')
  },
    {
    path: '/category-add',
    name: 'category-add',
    component: () => import('../views/category/CategoryAddView.vue')
  },
  {
    path: '/todo',
    name: 'todo-list',
    component: () => import('../views/todo/TodoListView.vue')
  },
  {
    path: '/todo/:id',
    name: 'todo-edit',
    component: () => import('../views/todo/TodoEditView.vue')
  },
  {
    path: '/todo-add',
    name: 'todo-add',
    component: () => import('../views/todo/TodoAddView.vue')
  },
  {
    path: '/todo/todo-by-category/:id',
    name: 'todo-by-category',
    component: () => import('../views/todo/todo-by-category/TodoListView.vue')
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
