import {
  AUTH_USER_REQUEST, AUTH_USER_SUCCESS, AUTH_USER_FAILURE,
  LOG_IN_REQUEST, LOG_IN_SUCCESS, LOG_IN_FAILURE,
  LOG_OUT } from "./types";
import axios from "axios";

const authUserRequest = () => {
  return {
    type: AUTH_USER_REQUEST
  }
}

const authUserSuccess = (user) => {
  return {
    type: AUTH_USER_SUCCESS,
    payload: user
  }
}

const authUserFailure = (err) => {
  return {
    type: AUTH_USER_FAILURE,
    payload: err
  }
}
// 앱 실행 시 유저 로그인 여부 요청
export const authUser = (id) => {
  // jwt 토큰 불러오기
  const jwttoken = localStorage.getItem("jwttoken");
  const yourConfig = {
    headers: {
      // 'Acess-Control-Allow-Origin': '*',
      'Authorization': `Bearer ${jwttoken}`,
      'Accept' : 'application/json',
      "Content-type": "Application/json",
    }
  }

  return (dispatch) => {

    dispatch(authUserRequest());
    // axios.get('http://220.122.5.95:8081/api/users/1', yourConfig),
    axios.get(`http://frankly.kro.kr:8081/api/users/${id}`,
      yourConfig
    )
      .then(function (response) {
        dispatch(authUserSuccess(response.data));
      })
      .catch(function (err) {
        dispatch(authUserFailure(err));
      })
  }
}

// 로그인
const loginRequest = () => {
  return {
    type: AUTH_USER_REQUEST
  }
}

const loginSuccess = () => {
  return {
    type: AUTH_USER_SUCCESS
  }
}

const loginFailure = (err) => {
  return {
    type: AUTH_USER_FAILURE,
    payload: err
  }
}

export const logIn = (user) => {
  return (dispatch) => {
    dispatch(loginRequest());
    axios.post('http://211.117.185.149:8081/api/auth/signin', user)
    // axios.post('http://frankly.kro.kr:8081/api/auth/signin', user)
      .then(function (response) {
        // 로컬스토리지에 토큰
        dispatch(loginSuccess());
        window.localStorage.setItem("jwttoken", response.data.jwttoken);
        // todo 토큰 인증
      })
      .catch(function (err) {
        dispatch(loginFailure(err));
        alert('아이디 혹은 비밀번호가 잘못되었습니다.');
        // todo input 비우기
      });
  }
}

// 로그아웃
export const logOut = () => {
  return {
    type: LOG_OUT,
    payload: ''
  }
}
