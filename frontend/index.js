import React from "react";
import ReactDom from 'react-dom';
import App from './src/App';
import {createStore} from "redux";
import appReducer from './src/redux/reducers/appReducer'

ReactDom.render(
  <App />,
  document.getElementById('root')
);
