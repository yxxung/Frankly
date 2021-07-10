import { combineReducers } from "redux";
import userReducer from "./User/reducer";
import lawmakerReducer from "./Lawmaker/reducer";
import communityReducer from "./Community/reducer";

const rootReducer = combineReducers({
  user: userReducer, // 유저 정보
  lawmaker: lawmakerReducer, // 국회의원 정보
  community: communityReducer, // 커뮤니티
})

export default rootReducer