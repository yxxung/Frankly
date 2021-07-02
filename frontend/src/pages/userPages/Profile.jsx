import React from "react";
import { Nav } from "../../components";
import {Link} from "react-router-dom";

const Profile = () => {

  return (
    <>
      <Nav />
      <h1>내정보 화면</h1>
      <Link to="/signUp">
        <p>회원가입</p>
      </Link>
      <Link to="/signIn">
        <p>로그인</p>
      </Link>
    </>
  )
};

export default Profile