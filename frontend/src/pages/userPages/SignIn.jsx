import React, { useState, memo } from "react";
import { Header } from "../../components";
import { Link } from "react-router-dom";
import { connect } from "react-redux";
import axios from "axios";

const SignIn = memo(({ history }) => {
  const [email, setEmail] = useState("");
  const [pw, setPw] = useState("");
  const [saveId, setSaveId] = useState(false);
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
  const postSignIn = (e) => {
    console.log('postSignIn');
    e.preventDefault();
    if (email === "" || pw === "") {
      window.alert("아이디와 비밀번호를 입력해주세요.");
    } else {
      // POST 로그인 api
      axios.post('http://220.122.5.95:8081/api/auth/signin', {
        username: email,
        password: pw,
      })
        .then(function (response) {
          // 로컬스토리지에 토큰
          window.localStorage.setItem("jwttoken", response.data.jwttoken);
          // todo 홈으로 이동
        })
        .catch(function (error) {
          // 로그인 오류
          alert('아이디 혹은 비밀번호가 잘못되었습니다.')
        });
    }
  }

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
        <form onSubmit={postSignIn} className="form">
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