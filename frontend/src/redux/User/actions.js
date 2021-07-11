import {
  GET_USER_REQUEST, GET_USER_SUCCESS, GET_USER_FAILURE,
  LOG_IN_REQUEST, LOG_IN_SUCCESS, LOG_IN_FAILURE } from "./types";
import axios from "axios";

export const getUserRequest = () => {
  return {
    type: GET_USER_REQUEST
  }
}

export const getUserSuccess = (user) => {
  return {
    type: GET_USER_SUCCESS,
    payload: user
  }
}

export const getUserFailure = (err) => {
  return {
    type: GET_USER_FAILURE,
    payload: err
  }
}
// 앱 실행 시 유저 로그인 여부 요청
export const getUser = (id) => {
  // jwt 토큰 불러오기
  let jwttoken = localStorage.getItem("jwttoken");
  let yourConfig = {
    headers: {
      'Acess-Control-Allow-Origin': '*',
      'Authorization': `Bearer ${jwttoken}`,
      'Accept' : 'application/json',
      'Content-Type': 'application/json'
    }
  }

  return (dispatch) => {
    dispatch(getUserRequest())
    axios.get('http://frankly.kro.kr:8081/api/users/1', yourConfig)
      .then(function (response) {
        dispatch(getUserSuccess(response))
      })
      .catch(function (err) {
        dispatch(getUserFailure(err))
      })
  }
}
