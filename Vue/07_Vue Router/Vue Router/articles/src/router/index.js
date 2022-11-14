import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexView from '../views/IndexView.vue'
import CreateView from '../views/CreateView.vue'
import DetailView from '../views/DetailView.vue'
import NotFound404 from '../views/NotFound404.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
  {
    path: '/404-not-found', // 숫자로 먼저 시작하면 detail에 먼저 걸려버림
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/:id', // 번호마다
    name: 'detail',
    component: DetailView
  },
  // detail이 마지막이라서, 없는 번호라면 DetailView의 함수에서 걸러져 NotFound404로 가게됨
  // {
  //   path: '*', 
  //   redirect: {name: 'NotFound404'}
  // },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
