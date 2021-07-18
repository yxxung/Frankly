import {
  FETCH_LAWMAKER_REQUEST,
  FETCH_LAWMAKER_SUCCESS,
  FETCH_LAWMAKER_FAILURE, } from "./types";
import axios from "axios";

export const fetchLawmakerRequest = () => {
  return {
    type: FETCH_LAWMAKER_REQUEST
  }
}

export const fetchLawmakerSuccess = (list) => {
  return {
    type: FETCH_LAWMAKER_SUCCESS,
    payload: list
  }
}

export const fetchLawmakerFailure = (err) => {
  return {
    type: FETCH_LAWMAKER_FAILURE,
    payload: err
  }
}

export const fetchLawmaker = (id) => {
  return (dispatch) => {
    dispatch(fetchLawmakerRequest())
    axios.get(`http://frankly.kro.kr:8081/api/infos/${id}`)
        // axios.get(`http://220.122.5.95:8081/api/infos/${id}`)
      // .then(res => res.json())
      // .then(list =>
      //   dispatch(fetchLawmakerSuccess(list)))
      // .catch(err => fetchLawmakerFailure(err))
      .then(function (response) {
        dispatch(fetchLawmakerSuccess(response.data))
      })
      .catch(function (err) {
        dispatch(fetchLawmakerFailure(err))
      })
  // todo 만약 10초이상 loading 중이면 "서버와의 연결이 원활하지 않습니다. 다시 시도해주세요..."
  }
}
