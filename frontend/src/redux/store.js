import { createStore } from 'redux';
import subscribersReducer from './reducer';
const store = createStore(subscribersReducer)

export default store;