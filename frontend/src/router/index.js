import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  // Auth Page View
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/auth/LoginView.vue')
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('../views/auth/SignUpView.vue')
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

  // Category Page View
  {
    path: '/category',
    name: 'category-list',
    component: () => import('../views/category/CategoryListView.vue')
  },
  {
    path: '/category/:categoryId',
    name: 'category-edit',
    component: () => import('../views/category/CategoryEditView.vue')
  },
  {
    path: '/category-add',
    name: 'category-add',
    component: () => import('../views/category/CategoryAddView.vue')
  },

  // Todo Page View
  {
    path: '/todo',
    name: 'todo-list',
    component: () => import('../views/todo/TodoListView.vue')
  },
  {
    path: '/todo/:todoId',
    name: 'todo-edit',
    component: () => import('../views/todo/TodoEditView.vue')
  },
  {
    path: '/todo-add',
    name: 'todo-add',
    component: () => import('../views/todo/TodoAddView.vue')
  },
  {
    path: '/todo/todo-by-category/:categoryId',
    name: 'todo-by-category',
    component: () => import('../views/todo/TodoListByCategoryView.vue')
  },
  {
    path: '/todo-add/todo-by-category/:categoryId',
    name: 'todo-add-by-category',
    component: () => import('../views/todo/TodoAddView.vue')
  },

  // User Page View
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/user/UserPageView.vue')
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
