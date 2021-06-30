import {
  ADD_SUBSCRIBER,
  REMOVE_SUBSCRIBER,
  ADD_VIEW, } from "./types";

export const addSubscriber = () => {
  return {
    type: ADD_SUBSCRIBER
  }
}

export const removeSubscriber = () => {
  return {
    type: REMOVE_SUBSCRIBER
  }
}

export const addView = (number) => {
  return {
    type: ADD_VIEW,
    payload: Number(number),
  }
}
