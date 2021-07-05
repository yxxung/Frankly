import React, {useEffect, useState} from "react";
import { Nav } from "../../components";
import {Link} from "react-router-dom";
import axios from "axios";

const Profile = () => {
  const [userName, setUserName] = useState("");


  // 헤더에 토큰


  useEffect(() => {
    let jwttoken = localStorage.getItem("jwttoken");
    let yourConfig = {
      headers: {
        'Authorization': `Bearer ${jwttoken}`,
        'Accept' : 'application/json',
        'Content-Type': 'application/json'
      }
    }
    console.log(jwttoken);
    axios.get('http://frankly.kro.kr:8081/api/users/1', yourConfig)
      .then(function (response) {
        console.log(response);
        setUserName(response.data.name);
      })
      .catch(function (error) {
        console.log(error);
      });
  }, [])

  return (
    <>
      <Nav />
      <h1>내정보 화면</h1>
      <p>이름 : {userName}</p>
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