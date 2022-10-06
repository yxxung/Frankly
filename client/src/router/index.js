import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MainBoard from '../views/Board/MainBoard.vue'
import Politician from '../views/Politician/Politician.vue'
import Mypage from '../views/Mypage.vue'
import AuthPage from '../views/Auth/AuthPage.vue'
import Signup from '../views/Auth/Signup.vue'
import Login from '../views/Auth/Login.vue'
import FreeBoard from '../views/Board/FreeBoard.vue'
import HotBoard from '../views/Board/HotBoard.vue'
import BoardDetail from '../views/Board/BoardDetail.vue'
import AdminBoard from '../views/Admin/AdminBoard.vue'
import DataExtract from '../views/Admin/DataExtract.vue'
import EditBoard from '../views/Admin/EditBoard.vue'
import EditUser from '../views/Admin/EditUser.vue'
import PoliticianDetail from '../views/Politician/PoliticianDetail.vue'
import WriteBoard from '../views/Board/WriteBoard.vue'
import SeoulBoard from '../views/Board/region/SeoulBoard.vue'
import EditData from "@/views/Admin/EditData"

const routes = [
  {
    path: '/',
    component: Home
  },
  {
    path: '/Login',
    component: Login
  },
  {
    path: '/Signup',
    component: Signup
  },
  {
    // 중첩된 라우트 : 한 페이지에 url에 따라서 다른 컴포넌트를 보여야 할 때 사용.
    path: '/Auth',
    component: AuthPage
  },
  {
    path: '/Mypage',
    name: 'Mypage',
    component: Mypage
  },
  /*board*/
  {
    path: '/WriteBoard',
    component: WriteBoard
  },
  {
    path: '/MainBoard',
    component: MainBoard,
  },
  {
    path: '/Politician',
    name: 'Politician',
    component: Politician
  },
  {
    path: '/FreeBoard',
    name: 'FreeBoard',
    component: FreeBoard
  },
  {
    path: '/HotBoard',
    name: 'HotBoard',
    component: HotBoard
  },
  {
    path: '/SeoulBoard',
    name: 'SeoulBoard',
    component: SeoulBoard
  },
  {
    path: '/BoardDetail/:boardID',
    name: 'BoardDetail',
    component: BoardDetail
  },
  // admin page router
  {
    path: '/adminPage',
    component: DataExtract
  },
  {
    path: '/EditBoard',
    component: EditBoard
  },
  {
    path: '/EditUser',
    component: EditUser
  },

  {
    path: '/EditData',
    component: EditData
  },
  {
    path: '/PoliticianDetail',
    name: 'PoliticianDetail',
    component: PoliticianDetail
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "route-active",
  linkExactActiveClass: "route-active"
})

export default router
