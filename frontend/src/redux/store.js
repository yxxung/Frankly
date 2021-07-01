import {defaultState} from "./defaultState";
import {createStore} from "redux";
import {appReducer} from "./reducers";

//middleware 삽입
const store = createStore(
    appReducer,
    defaultState
);

//middleware 실

export default store;
