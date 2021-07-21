import {
  AUTH_USER_REQUEST, AUTH_USER_SUCCESS, AUTH_USER_FAILURE,
  LOG_IN_REQUEST, LOG_IN_SUCCESS, LOG_IN_FAILURE,
  LOG_OUT } from "./types";

const initialState = {
  userInfo: {},
  loginSuccess: false,
  loading: false,
  err: null
}

const userReducer = (state=initialState, action) => {
  switch(action.type){
      // 앱 실행 시 유저 로그인 여부 요청
    case AUTH_USER_REQUEST:
      return {
        ...state,
        loading: true,
      }
      // 유저 정보 인증 성공
    case AUTH_USER_SUCCESS:
      return {
        ...state,
        userInfo: action.payload,
        loginSuccess: true,
        loading: false,
      }
      // 유저 정보 인증 실패
    case AUTH_USER_FAILURE:
      return {
        ...state,
        err: action.payload,
        loading: false,
      }
      // 로그인 버튼 클릭
    case LOG_IN_REQUEST:
      return {
        ...state,
        loading: true,
      }
      // 로그인 성공
    case LOG_IN_SUCCESS:
      return {
        ...state,
        loading: false,
      }
      // 로그인 실패
    case LOG_IN_FAILURE:
      return {
        ...state,
        err: action.payload,
        loginSuccess: false,
        loading: false,
      }
    case LOG_OUT:
      return {
        initialState,
      }
    default: return state
  }
}

export default userReducer