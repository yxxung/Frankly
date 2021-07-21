import React, { useState, useEffect, memo } from "react";
import { Header } from "../../components";
import { Link } from "react-router-dom";
import { useSelector, useDispatch } from 'react-redux';
import { authUser, logIn } from "../../redux";

const checkEmail = (str) => {
  let reg_email = /^([0-9a-zA-Z_\.-]+)@([0-9a-zA-Z_-]+)(\.[0-9a-zA-Z_-]+){1,2}$/;
  if(!reg_email.test(str)) {
    return false;
  }
  else {
    return true;
  }
}

const LogIn = memo(({ history }) => {
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
    // 이메일 양식, 비밀번호 8자리 체크
    if (!checkEmail(email)) {
      alert('이메일 양식에 맞게 넣어주세요');
    } else if (pw.length < 8) {
      alert('비밀번호는 8자리 이상입니다');
    } else {
      const user = {
        username: email,
        password: pw,
      }
      dispatch(logIn(user));
    }
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

export default LogIn