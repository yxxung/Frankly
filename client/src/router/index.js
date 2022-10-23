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
import BusanBoard from '../views/Board/region/BusanBoard.vue'
import ChungbukBoard from '../views/Board/region/ChungbukBoard.vue'
import ChungnamBoard from '../views/Board/region/ChungnamBoard.vue'
import DaeguBoard from '../views/Board/region/DaeguBoard.vue'
import DaejeonBoard from '../views/Board/region/DaejeonBoard.vue'
import GwangjuBoard from '../views/Board/region/GwangjuBoard.vue'
import GangwonBoard from '../views/Board/region/GangwonBoard.vue'
import GyeongbukBoard from '../views/Board/region/GyeongbukBoard.vue'
import GyeongnamBoard from '../views/Board/region/GyeongnamBoard.vue'
import GyeonggiBoard from '../views/Board/region/GyeonggiBoard.vue'
import IncheonBoard from '../views/Board/region/IncheonBoard.vue'
import JejuBoard from '../views/Board/region/JejuBoard.vue'
import JeonbukBoard from '../views/Board/region/JeonbukBoard.vue'
import JeonnamBoard from '../views/Board/region/JeonnamBoard.vue'
import UlsanBoard from '../views/Board/region/UlsanBoard.vue'
import SejongBoard from '../views/Board/region/SejongBoard.vue'
import PoliticianSearchView from "@/views/Politician/PoliticianSearchView.vue"
import Statistics from "@/views/Politician/Statistics.vue"
import PoliticianPropertyDetail from "@/views/Politician/PoliticianPropertyDetail.vue"
import PoliticianNewsKeyword from "@/views/Politician/PoliticianNewsKeyword.vue"

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
    path: '/WriteBoard/:boardID?',
    name: 'WriteBoard',
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
    path: '/BusanBoard',
    name: 'BusanBoard',
    component: BusanBoard
  },
  {
    path: '/ChungbukBoard',
    name: 'ChungbukBoard',
    component: ChungbukBoard
  },
  {
    path: '/ChungnamBoard',
    name: 'ChungnamBoard',
    component: ChungnamBoard
  },
  {
    path: '/DaeguBoard',
    name: 'DaeguBoard',
    component: DaeguBoard
  },
  {
    path: '/DaejeonBoard',
    name: 'DaejeonBoard',
    component: DaejeonBoard
  },
  {
    path: '/GangwonBoard',
    name: 'GangwonBoard',
    component: GangwonBoard
  },
  {
    path: '/GwangjuBoard',
    name: 'GwangjuBoard',
    component: GwangjuBoard
  },
  {
    path: '/GyeongbukBoard',
    name: 'GyeongbukBoard',
    component: GyeongbukBoard
  },
  {
    path: '/GyeonggiBoard',
    name: 'GyeonggiBoard',
    component: GyeonggiBoard
  },
  {
    path: '/GyeongnamBoard',
    name: 'GyeongnamBoard',
    component: GyeongnamBoard
  },
  {
    path: '/IncheonBoard',
    name: 'IncheonBoard',
    component: IncheonBoard
  },
  {
    path: '/JejuBoard',
    name: 'JejuBoard',
    component: JejuBoard
  },
  {
    path: '/JeonbukBoard',
    name: 'JeonbukBoard',
    component: JeonbukBoard
  },
  {
    path: '/JeonnamBoard',
    name: 'JeonnamBoard',
    component: JeonnamBoard
  },
  {
    path: '/SejongBoard',
    name: 'SejongBoard',
    component: SejongBoard
  },
  {
    path: '/UlsanBoard',
    name: 'UlsanBoard',
    component: UlsanBoard
  },
  {
    path: '/BoardDetail/:boardID',
    name: 'BoardDetail',
    component: BoardDetail
  },
  /*admin*/
  {
    path: '/AdminBoard',
    component: AdminBoard
  },
  {
    path: '/DataExtract',
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
    path: '/PoliticianDetail/:politicianID',
    name: 'PoliticianDetail',
    component: PoliticianDetail
  },
  {
    path:'/PoliticianDetail/:politicianID/property',
    name: 'PoliticianPropertyDetail',
    component: PoliticianPropertyDetail,
    props: true
  },
  {
    path:'/PoliticianDetail/:politicianID/keyword',
    name: 'PoliticianNewsKeyword',
    component: PoliticianNewsKeyword,
    props: true
  },
  {
    path: '/Search',
    name: 'Search',
    component: PoliticianSearchView
  },
  /*시각화*/
  {
    path: '/Statistics',
    name: 'Statistics',
    component: Statistics
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "route-active",
  linkExactActiveClass: "route-active"
})

export default router
