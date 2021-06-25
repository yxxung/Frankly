import React, {useState, useCallback, useEffect} from "react";
import { Link, BrowserRouter, Route, Switch } from "react-router-dom";
import Axios from "axios";

import Lawmaker from "./pages/Lawmaker"
import Profile from "./pages/Profile";
import Community from "./pages/Community";
import EmptyPage from "./pages/EmptyPage";
import Nav from "./components/Nav";

const App = () => {
  const [login, setLogin] = useState(false);
  // 로그인 여부 체크
  // if 로그인 -> 지역 체크 -> 지역 번호 데이터 요청 -> 받고 화면 뿌려주기(?)
  // page 값 Lawmaker
  // else 로그아웃 -> 기본값 (서울 송파구을 배현진ㅋ) 요청 -> 받고 화면 뿌려주기

  return (
    <BrowserRouter>

      <Switch>
        {/*페이지*/}
        <Route exact path="/" component={Lawmaker} />
        <Route exact path="/community" component={Community} />
        <Route exact path="/profile" component={Profile} />
        {/*추가해야할 페이지 :
          로그인
          회원가입
          회원정보 수정
          설정
          FAQ
          글쓰기
          글 내용보기
        */}
        {/*빈 페이지*/}
        <Route component={EmptyPage} />
      </Switch>

      {/*하단 네비게이션 (로그인 props 전달 해야하나?)*/}
      <Nav />

    </BrowserRouter>
  )
};

export default App