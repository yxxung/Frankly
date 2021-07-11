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
  // // jwt 토큰 불러오기
  // const jwttoken = localStorage.getItem("jwttoken");
  // const bodyParameters = {
  //   key: "value"
  // };
  // const yourConfig = {
  //   headers: {
  //     // "Access-Control-Allow-Origin": "http://frankly.kro.kr:8081",
  //     // "Access-Control-Allow-Credentials": "true",
  //     'Authorization': `Bearer ${jwttoken}`,
  //     'Accept' : 'application/json',
  //     "Content-type": "Application/json",
  //     // "credentials": "include",
  //
  //   }
  // }
  //
  // return (dispatch) => {
  //   dispatch(getUserRequest())
  //   axios.defaults.headers.common["Authorization"] = `Bearer ${jwttoken}`
  //   axios.get('http://frankly.kro.kr:8081/api/users/1',
  //     // bodyParameters,
  //     yourConfig,
  //     { withCredentials: true }
  //   )
  //     .then(function (response) {
  //       dispatch(getUserSuccess(response))
  //     })
  //     .catch(function (err) {
  //       dispatch(getUserFailure(err))
  //     })
  // }

  const jwttoken = localStorage.getItem("jwttoken");
  const httpInstance = axios.create({
    baseURL: "http://frankly.kro.kr:8081/api/users/",
    timeout: 180000,
    headers: {
      Authorization: `Bearer ${localStorage.getItem("jwttoken")}`,
      "Content-Type": "application/json",
    },
    withCredentials: true,
  });

  // httpInstance.defaults.headers.common.Authorization = `Bearer ${jwttoken}`;

  return (dispatch) => {
    dispatch(getUserRequest())
    httpInstance.get(
      `http://frankly.kro.kr:8081/api/users/${id}`,
    )
      .then(function (response) {
        dispatch(getUserSuccess(response.data))
      })
      .catch(function (err) {
        dispatch(getUserFailure(err))
      })
  }
}