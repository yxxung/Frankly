import { combineReducers } from "redux";
import userReducer from "./User/reducer";
import lawmakerReducer from "./Lawmaker/reducer";
import communityReducer from "./Community/reducer";

const rootReducer = combineReducers({
  user: userReducer, // 유저 정보
  lawmaker: lawmakerReducer, // 국회의원 정보
  community: communityReducer, // 커뮤니티
})

// 새로고침 안하고 store 내용 비울때 사용
// const rootReducer = (state, action) => {
//   if (action.type === 'LOG_OUT') {
//     window.localStorage.removeItem("jwttoken")
//     return appReducer(undefined, action)
//   }
//
//   return appReducer(state, action)
// }

export default rootReducer