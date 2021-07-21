import React, { useEffect } from "react";
import { Route, Switch } from "react-router-dom";
import { Community, Lawmaker, Profile, LogIn, SignUp, EmptyPage } from "./pages"
import { useDispatch } from "react-redux";
import { authUser } from "./redux";

const App = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(authUser(1)) // 토큰으로 유저정보 가져오기 / id 값
  }, [])

  return (
    <>
      <Switch>
        <Route exact path="/"  component={Lawmaker} />)} />
        <Route exact path="/community" component={Community} />
        <Route exact path="/profile" component={Profile} />
        <Route exact path="/login" component={LogIn} />
        <Route exact path="/signup" component={SignUp} />
        {/*todo 추가해야할 페이지 :
          회원정보 수정
          설정
          FAQ
          글쓰기
          글 내용보기
        */}
      </Switch>
    </>
  )
};

export default App