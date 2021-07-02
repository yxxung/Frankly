import {
  FETCH_LAWMAKER_REQUEST,
  FETCH_LAWMAKER_SUCCESS,
  FETCH_LAWMAKER_FAILURE, } from "./types";

const initialState = {
  items: [],
  loading: false,
  err: null
}

const lawmakerReducer = (state=initialState, action) => {
  switch(action.type){
    case FETCH_LAWMAKER_REQUEST:
      return {
        ...state,
        loading: true,
      }
    case FETCH_LAWMAKER_SUCCESS:
      return {
        ...state,
        items: action.payload,
        loading: false,
      }
    case FETCH_LAWMAKER_FAILURE:
      return {
        ...state,
        err: action.payload,
        loading: false,
      }
    default: return state
  }
}

export default lawmakerReducer