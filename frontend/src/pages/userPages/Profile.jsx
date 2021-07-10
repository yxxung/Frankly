import React, { useState } from "react";
import { useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { Nav } from "../../components";

const Profile = () => {
  const [userName, setUserName] = useState("");

  const userInfo = useSelector(store => store.user.userInfo);
  const loading = useSelector(store => store.user.loading);
  console.log(userInfo);
  console.log(loading);


  return (
    <>
      <Nav />
      <h1>내정보 화면</h1>
      <p>이름 : {}</p>
      <Link to="/signUp">
        <p>회원가입</p>
      </Link>
      <Link to="/signIn">
        <p>로그인</p>
      </Link>
    </>
  )
};

export default Profile;