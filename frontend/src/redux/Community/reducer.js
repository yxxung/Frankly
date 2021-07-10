// 테스트 코드

import {
  ADD_SUBSCRIBER,
  REMOVE_SUBSCRIBER,
  ADD_VIEW, } from "./types";

const initialState = {
  count: 370,
  view: 0,
}

const communityReducer = (state=initialState, action) => {
  switch(action.type){

    case ADD_SUBSCRIBER:
      return {
        ...state,
        count: state.count + 1
      }
    case REMOVE_SUBSCRIBER:
      return {
        ...state,
        count: state.count - 1
      }
    case ADD_VIEW:
      return {
        ...state,
        view: state.view + action.payload
      }
    default: return state
  }
}

export default communityReducer