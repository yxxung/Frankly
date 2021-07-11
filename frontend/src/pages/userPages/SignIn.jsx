import React, { useState, useEffect, memo } from "react";
import { Header } from "../../components";
import { Link } from "react-router-dom";
import { useSelector, useDispatch } from 'react-redux';
import {authUser, logIn} from "../../redux";
import axios from "axios";

const SignIn = memo(({ history }) => {
  const [email, setEmail] = useState("");
  const [pw, setPw] = useState("");
  const [saveId, setSaveId] = useState(false);
  const dispatch = useDispatch();
  const loginSuccess = useSelector(store => store.user.loginSuccess);
  // 아이디
  const onIdHandler = (e) => {
    console.log('onIdHandler')
    setEmail(e.currentTarget.value);
  };
  // 패스워드
  const onPasswordHandler = (e) => {
    console.log('onPasswordHandler');
    setPw(e.currentTarget.value);
  };
  // 아이디 저장 체크박스
  const checkHandler = (e) => {
    console.log('checkHandler');
    setSaveId(!saveId);
  };

  // 로그인 버튼
  const onClickLogIn = (e) => {
    e.preventDefault();
    const user = {
      username: email,
      password: pw,
    }
    dispatch(logIn(user));
  }

  useEffect(() => {
    if (loginSuccess) {
      history.push("/");
    }
  }, []);


  return (
    <>
      <Header
        title="로그인"
        btn="back"
        history={history}
      />
      <div className="signIn">
        <div className="title">
          <h2>Frankly</h2>
        </div>
        <form onSubmit={onClickLogIn} className="form">
          <label>
            <input type="text" value={email} onChange={onIdHandler} placeholder="아이디" />
            <input type="password" value={pw} onChange={onPasswordHandler} placeholder="비밀번호" />
          </label>
          <div className="check">
            <input type="checkbox" id="saveId" checked={saveId} onChange={checkHandler} />
            <label htmlFor="saveId">아이디 저장</label>
          </div>
          <button type="submit" className="signInBtn" >로그인</button>
        </form>
        <div className="signUpLink">
          <Link to="signUp">회원가입</Link>
          <Link to="/">아이디 / 비밀번호 찾기</Link>
        </div>
      </div>
    </>
  )
})

export default SignIn