import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import MainBoard from '../views/Board/MainBoard.vue'
import Politician from '../views/Politician/Politician.vue'
import Mypage from '../views/User/Mypage.vue'
import MyReplyBoard from '../views/User/MyReplyBoard.vue'
import MyWriteBoard from '../views/User/MyWriteBoard.vue'
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
import UpdateBoard from '../views/Board/UpdateBoard.vue'
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
import PoliticianPropertyDetail from "@/views/Politician/PoliticianPropertyDetail";
import EditData from "@/views/Admin/EditData";
import PoliticianNewsKeyword from "@/views/Politician/PoliticianNewsKeyword";
import PoliticianSearchView from "@/views/Politician/PoliticianSearchView";
import PoliticianStatistics from "@/views/Politician/PoliticianStatistics";
import PoliticianAttendance from "@/views/Politician/PoliticianAttendance";
import PoliticianVote from "@/views/Politician/PoliticianVote";
//import EditData from "@/views/Admin/EditData"

import store from '@/store/index.js'

const onlyAuthUser = async (to, from, next) => {
  const userID = sessionStorage.getItem("userID");

  //const checkUserInfo = store.getters("userStore/checkUserInfo");

  if (store.getters["userStore/checkUserInfo"] == null && userID) {
    await store.dispatch("userStore/getUserInfo", userID);
  }

  if (store.getters["userStore/checkUserInfo"] === null) {
    alert("로그인이 필요한 페이지입니다.");
    next({ name: "Login" });
  } else {
    next();
  }
};

const onlyNoAuthUser = async (to, from, next) => {
  //const checkUserInfo = store.getters["userStore/checkUserInfo"];
  let userID = sessionStorage.getItem("userID");

  if (store.getters["userStore/checkUserInfo"] == null && userID) {
    store.dispatch("userStore/getUserInfo", userID);
  }

  if (store.getters["userStore/checkUserInfo"] === null) {
    next();
  } else {
    next({ name: "Home" });
  }
};

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/Login',
    name: 'Login',
    beforeEnter: onlyNoAuthUser,
    component: Login,
  },
  {
    path: '/Signup',
    name: 'Signup',
    beforeEnter: onlyNoAuthUser,
    component: Signup
  },
  {
    path: '/',
    name: 'AuthPage',
    beforeEnter: onlyNoAuthUser,
    component: AuthPage
  },
  {
    path: '/Mypage',
    name: 'Mypage',
    beforeEnter: onlyAuthUser,
    component: Mypage
  },
  {
    path: '/MyWriteBoard',
    name: 'MyWriteBoard',
    beforeEnter: onlyAuthUser,
    component: MyWriteBoard
  },
  {
    path: '/MyReplyBoard',
    name: 'MyReplyBoard',
    beforeEnter: onlyAuthUser,
    component: MyReplyBoard
  },
  /*board*/
  {
    path: '/WriteBoard',
    name: 'WriteBoard',
    beforeEnter: onlyAuthUser,
    component: WriteBoard
  },
  {
    path: '/UpdateBoard/:boardID',
    name: 'UpdateBoard',
    beforeEnter: onlyAuthUser,
    component: UpdateBoard
  },
  {
    path: '/MainBoard',
    beforeEnter: onlyAuthUser,
    component: MainBoard,
  },
  {
    path: '/Politician',
    name: 'Politician',
    beforeEnter: onlyAuthUser,
    component: Politician
  },
  {
    path: '/FreeBoard',
    name: 'FreeBoard',
    beforeEnter: onlyAuthUser,
    component: FreeBoard
  },
  {
    path: '/HotBoard',
    name: 'HotBoard',
    beforeEnter: onlyAuthUser,
    component: HotBoard
  },
  {
    path: '/SeoulBoard',
    name: 'SeoulBoard',
    beforeEnter: onlyAuthUser,
    component: SeoulBoard
  },
  {
    path: '/BusanBoard',
    name: 'BusanBoard',
    beforeEnter: onlyAuthUser,
    component: BusanBoard
  },
  {
    path: '/ChungbukBoard',
    name: 'ChungbukBoard',
    beforeEnter: onlyAuthUser,
    component: ChungbukBoard
  },
  {
    path: '/ChungnamBoard',
    name: 'ChungnamBoard',
    beforeEnter: onlyAuthUser,
    component: ChungnamBoard
  },
  {
    path: '/DaeguBoard',
    name: 'DaeguBoard',
    beforeEnter: onlyAuthUser,
    component: DaeguBoard
  },
  {
    path: '/DaejeonBoard',
    name: 'DaejeonBoard',
    beforeEnter: onlyAuthUser,
    component: DaejeonBoard
  },
  {
    path: '/GangwonBoard',
    name: 'GangwonBoard',
    beforeEnter: onlyAuthUser,
    component: GangwonBoard
  },
  {
    path: '/GwangjuBoard',
    name: 'GwangjuBoard',
    beforeEnter: onlyAuthUser,
    component: GwangjuBoard
  },
  {
    path: '/GyeongbukBoard',
    name: 'GyeongbukBoard',
    beforeEnter: onlyAuthUser,
    component: GyeongbukBoard
  },
  {
    path: '/GyeonggiBoard',
    name: 'GyeonggiBoard',
    beforeEnter: onlyAuthUser,
    component: GyeonggiBoard
  },
  {
    path: '/GyeongnamBoard',
    name: 'GyeongnamBoard',
    beforeEnter: onlyAuthUser,
    component: GyeongnamBoard
  },
  {
    path: '/IncheonBoard',
    name: 'IncheonBoard',
    beforeEnter: onlyAuthUser,
    component: IncheonBoard
  },
  {
    path: '/JejuBoard',
    name: 'JejuBoard',
    beforeEnter: onlyAuthUser,
    component: JejuBoard
  },
  {
    path: '/JeonbukBoard',
    name: 'JeonbukBoard',
    beforeEnter: onlyAuthUser,
    component: JeonbukBoard
  },
  {
    path: '/JeonnamBoard',
    name: 'JeonnamBoard',
    beforeEnter: onlyAuthUser,
    component: JeonnamBoard
  },
  {
    path: '/SejongBoard',
    name: 'SejongBoard',
    beforeEnter: onlyAuthUser,
    component: SejongBoard
  },
  {
    path: '/UlsanBoard',
    name: 'UlsanBoard',
    beforeEnter: onlyAuthUser,
    component: UlsanBoard
  },
  {
    path: '/BoardDetail/:boardID',
    name: 'BoardDetail',
    beforeEnter: onlyAuthUser,
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
    path: '/EditData',
    component: EditData
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
    path:'/PoliticianDetail/:politicianID/attendance',
    name: 'PoliticianAttendance',
    component: PoliticianAttendance,
    props: true
  },
  {
    path:'/PoliticianDetail/:politicianID/vote',
    name: 'PoliticianVote',
    component: PoliticianVote,
    props: true
  },
  {
    path: '/Search',
    name: 'Search',
    component: PoliticianSearchView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  linkActiveClass: "route-active",
  linkExactActiveClass: "route-active"
})

export default router