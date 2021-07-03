import { combineReducers } from "redux";
import subscribersReducer from "./Community/reducer";
import lawmakerReducer from "./Lawmaker/reducer";

const rootReducer = combineReducers({
  subscribers: subscribersReducer,
  lawmaker: lawmakerReducer,
})

export default rootReducer