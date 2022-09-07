import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Board from '../views/Board/MainBoard.vue'
import Politician from '../views/Politician.vue'
import Mypage from '../views/Mypage.vue'
import Signup from '../views/Auth/Signup.vue'
import Login from '../views/Auth/Login.vue'
import FreeBoard from '../views/Board/FreeBoard.vue'
import HotBoard from '../views/Board/HotBoard.vue'
import BoardContext from '../views/Board/BoardContext.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Signup',
    name: 'Signup',
    component: Signup
  },
  {
    // 중첩된 라우트 : 한 페이지에 url에 따라서 다른 컴포넌트를 보여야 할 때 사용.
    path: '/Auth',
    redirect: '/Auth/Login',
    component: () => import('../views/Auth/AuthPage'),
    children: [
      {
        path: 'Login',
        component: () => import('../views/Auth/Login'),
      },
      {
        path: 'Signup',
        component: () => import('../views/Auth/Signup'),
      },
    ],
  },
  {
    path: '/Board',
    component: Board,
    children: [
      {
        path: '/:region/:start'
      }
    ]
  },
  {
    path: '/Politician',
    name: 'Politician',
    component: Politician
  },
  {
    //콜론으로 시작하는 부분이 동적 세그먼트
    path: '/Mypage/:userID',
    name: 'Mypage',
    component: Mypage
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
    path: '/BoardContext',
    name: 'BoardContext',
    component: BoardContext
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
