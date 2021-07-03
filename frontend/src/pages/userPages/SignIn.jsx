import React, { useState } from "react";
import { } from "../../components";
import { Link } from "react-router-dom";

const SignIn = () => {
  const [id, setId] = useState("");
  const [pw, setPw] = useState("");
  const [saveId, setSaveId] = useState(false);

  const onIdHandler = (e) => {
    setId(e.currentTarget.value);
  };

  const onPasswordHandler = (e) => {
    setPw(e.currentTarget.value);
  };

  const checkHandler = (e) => {
    setSaveId(!saveId);
  };
  // 로그인 버튼
  const onSubmitHandler = (e) => {
    e.preventDefault();
    if (id === "" || pw === "") {
      window.alert("아이디와 비밀번호를 입력해주세요.");
    }
  };

  return (
    <>
      <div className="signIn">
          <div className="title">
            <h2>Frankly</h2>
          </div>
          <form onSubmit={onSubmitHandler} className="form">
            <label>
              <input type="text" value={id} onChange={onIdHandler} placeholder="아이디" />
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
};

export default SignIn