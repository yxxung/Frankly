import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { logOut } from "../../redux";
import { Header, Nav } from "../../components";

const Profile = (props) => {
  const [userName, setUserName] = useState("");

  const dispatch = useDispatch();
  const loginSuccess = useSelector(store => store.user.loginSuccess);
  const userInfo = useSelector(store => store.user.userInfo);
  const loading = useSelector(store => store.user.loading);
  console.log(userInfo);

  const onClickLogOut = (e) => {
    e.preventDefault();
    dispatch(logOut());
    window.localStorage.removeItem("jwttoken");
    props.history.push("/");
  }

  return (
    <div className="contents">
      <Header />
      <Nav />
      <h1>내정보 화면</h1>
      <p>이름 : {}</p>
      <Link to="/signUp">
        <p>회원가입</p>
      </Link>

        { loginSuccess ?
          (
            <a onClick={onClickLogOut}>
              <p>로그아웃</p>
            </a>
          ) : (
            <Link to="/signIn">
              <p>로그인</p>
            </Link>
          )
        }

    </div>
  )
};

export default Profile;