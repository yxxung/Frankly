const ADD_SUBSCRIBER = 'ADD_SUBSCRIBER'
const REMOVE_SUBSCRIBER = 'REMOVE_SUBSCRIBER'

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