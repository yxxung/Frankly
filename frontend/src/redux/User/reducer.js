import {
  GET_USER_REQUEST, GET_USER_SUCCESS, GET_USER_FAILURE,
  LOG_IN_REQUEST, LOG_IN_SUCCESS, LOG_IN_FAILURE } from "./types";

const initialState = {
  userInfo: {},
  loading: false,
  err: null
}

const userReducer = (state=initialState, action) => {
  switch(action.type){
      // 앱 실행 시 유저 로그인 여부 요청
    case GET_USER_REQUEST:
      return {
        ...state,
        loading: true,
      }
      // 유저 정보 성공
    case GET_USER_SUCCESS:
      return {
        ...state,
        userInfo: action.payload,
        loading: false,
      }
      // 유저 정보 실패
    case GET_USER_FAILURE:
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
        userInfo: action.payload,
        loading: false,
      }
      // 로그인 실패
    case LOG_IN_FAILURE:
      return {
        ...state,
        err: action.payload,
        loading: false,
      }
    default: return state
  }
}

export default userReducer