import { GET_USER_REQUEST, GET_USER_SUCCESS, GET_USER_FAILURE } from "./types";

const initialState = {
  userInfo: {},
  loading: false,
  err: null
}

const userReducer = (state=initialState, action) => {
  switch(action.type){
      // 로그인 요청
    case GET_USER_REQUEST:
      return {
        ...state,
        loading: true,
      }
      // 로그인 성공
    case GET_USER_SUCCESS:
      return {
        ...state,
        userInfo: action.payload,
        loading: false,
      }
      // 로그인 실패
    case GET_USER_FAILURE:
      return {
        ...state,
        err: action.payload,
        loading: false,
      }
    default: return state
  }
}

export default userReducer