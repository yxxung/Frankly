import React, { useState } from "react";
import { } from "../../components";
import axios from "axios";
import {Link} from "react-router-dom";

const SignUp = () => {
  const [email, setEmail] = useState("");
  const [pw, setPw] = useState("");
  const [name, setName] = useState("");
  const [district, setDistrict] = useState("");
  const [sex, setSex] = useState("");
  const [contact, setContact] = useState("");
  const [params, setParams] = useState("");

  const onEmailHandler = (e) => {
    setEmail(e.currentTarget.value);
  };

  const onPasswordHandler = (e) => {
    setPw(e.currentTarget.value);
  };

  const onNameHandler = (e) => {
    setName(e.currentTarget.value);
  };

  const onDistrictHandler = (e) => {
    setDistrict(e.currentTarget.value);
  };

  const onSexHandler = (e) => {
    setSex(e.currentTarget.value);
  };

  const onContactHandler = (e) => {
    setContact(e.currentTarget.value);
  };

  const onSubmitHandler = (e) => {
    e.preventDefault();
    if (email === "" || pw === "") {
      window.alert("아이디와 비밀번호를 입력해주세요.");
    }
  };

  const postSignUp = (e) => {
    e.preventDefault();
    axios.post('http://frankly.kro.kr:8081/api/users/signup', {
      email: email,
      password: pw,
      name: name,
      district: district,
      sex: sex,
      contact: contact,
      userAuth: "user",
    })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  return (
    <>
      <h1>회원가입 화면</h1>
      <div className="signIn">
        <div className="title">
          <h2>Frankly</h2>
        </div>
        <form onSubmit={postSignUp} className="form">
          <label>
            <input type="text" value={email} onChange={onEmailHandler} placeholder="아이디" />
            <input type="password" value={pw} onChange={onPasswordHandler} placeholder="비밀번호" />
            <input type="text" value={name} onChange={onNameHandler} placeholder="이름" />
            <input type="text" value={district} onChange={onDistrictHandler} placeholder="지역" />
            <input type="text" value={sex} onChange={onSexHandler} placeholder="성별" />
            <input type="text" value={contact} onChange={onContactHandler} placeholder="휴대폰 번호" />
          </label>
          <button type="submit" className="signInBtn" >회원가입</button>
        </form>
      </div>
    </>
  )
};

export default SignUp