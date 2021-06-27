import React, {useState, useCallback, useEffect} from "react";
import { Link, BrowserRouter, Route, Switch } from "react-router-dom";
import axios from "axios";
import "./assets/scss/App.scss"

import Lawmaker from "./pages/Lawmaker"
import Profile from "./pages/Profile";
import Community from "./pages/Community";
import EmptyPage from "./pages/EmptyPage";

const fetchData = () => {
  return axios.get('https://jsonplaceholder.typicode.com/users')
    .then(res => {
      // console.log(res.data)
      return res.data;
    })
    .catch((err) => {
      console.log(err);
    })
}

const App = () => {
  const [login, setLogin] = useState(false);
  const [lawmakerList, setList] = useState([]);
  const [loading, setLoading]  = useState(true);

  useEffect(() => {
    fetchData().then(lawmakerList => {
      setList(lawmakerList);
      setLoading(false);
    })
  }, []);

  return (
    <BrowserRouter>
      {loading ? ("loading...") : (
      <Switch>
        {/*페이지*/}
        <Route exact path="/" render={(props) => (<Lawmaker list={lawmakerList} />)} />
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
      </Switch>
      )}
    </BrowserRouter>
  )
};

export default App