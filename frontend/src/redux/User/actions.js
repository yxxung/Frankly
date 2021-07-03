import { GET_USER_REQUEST, GET_USER_SUCCESS, GET_USER_FAILURE } from "./types";

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

export const getUser = (id) => {
  return (dispatch) => {
    // 유저 정보 api
  }
}