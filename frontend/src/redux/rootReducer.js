import { combineReducers } from "redux";
import subscribersReducer from "./Community/reducer";
import lawmakerReducer from "./Lawmaker/reducer";
import userReducer from "./User/reducer";

const rootReducer = combineReducers({
  subscribers: subscribersReducer,
  lawmaker: lawmakerReducer,
  user: userReducer,
})

export default rootReducer