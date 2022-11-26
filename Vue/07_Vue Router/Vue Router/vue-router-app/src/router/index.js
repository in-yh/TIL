import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView'
import LoginView from '@/views/LoginView'
import NotFound404 from '@/views/NotFound404'
import DogView from '@/views/DogView'

Vue.use(VueRouter)

const isLoggedIn = true 

const routes = [
  // 라우터에 관련된 정보 및 설정이 작성 되는 곳
  // 장고에서의 urls.py와 비슷
  // routes에 URL과 컴포넌트를 매핑
  {
    path: '/',
    name: 'home',
    // 이름을 가지는 routes
    //  장고에서 path 함수의 name 인자의 활용과 같은 방식
    component: HomeView
  },
  {
    // lazy-loading 방식(첫 로딩에 렌더링 하지 않고 해당 라우터가 동작할 때 컴포넌트를 렌더링 한다.)
    // 처음에 모든 파일을 한 번에 로드하려면 시간이 오래 걸림(로딩을 해놓지 않고 불려지면 그 때 로딩함)
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  },
  // 동적 인자
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: '/login/',
    name: 'login',
    component: LoginView,
    // 라우터 가드 : 로그인 이동할 때만 호출이 됨(home이나 about이나 hello에서는 할 필요 없음)
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인 되어있음')
        next({name: 'home'})
      } else {
        next()
      }
    }
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView,
  },
  // 가장 아래 있어야 함
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '*',
    redirect: '/404',
  }
]
// routes와 직접적으로 연결된 vue는 src/views에 작성해야함(다른 컴포넌트와 구분 위해 View로 끝나도록 만들 것)
// routes와 직접적으로 연결되지 않은 컴포넌트는 src/components에 씀(HomeView 밑에 사용된 HelloWorld 같은 거)

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// 전역가드
// router.beforeEach((to, from, next) => {
//   // console.log('to', to) // 이동할 url 정보가 담긴 route 객체, next()를 호출하기 전에는 화면 전환되지 않고 대기상태, '다른' url로 이동할 때 전역가드 호출
//   // console.log('from', from) // 현재 url 정보가 담긴 route 객체
//   // console.log('next', next) // 지정한 url로 이동하기 위해 호출하는 함수
//   // next() 

//   // 로그인 여부
//   const isLoggedIn = false
//   // 로그인이 필요한 페이지
//   // const authPages = ['hello', 'home', 'about']
//   const authPages = ['login']

//   // const isAuthRequired = authPages.includes(to.name)
//   const isAuthRequired = !authPages.includes(to.name)

//   // 로그인이 필요한 페이지이나, 로그인이 되어있지 않다면
//   if (isAuthRequired === true && !isLoggedIn) {
//     console.log('Login으로 이동!')
//     next({ name:'login' })
//   } else {
//     console.log('to로 이동!')
//     next()
//   }

// })

export default router
