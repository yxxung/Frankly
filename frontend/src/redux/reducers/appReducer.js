import * as ACTIONS from "../actions";

function appReducer(state, action) {

    switch (action.type) {

        case ACTIONS.AUTH_SUCCESS:
            return Object.assign({}, state, {
                init:true
            });

        case ACTIONS.AUTH_FAILED:
            return Object.assign({}, state, {
                init:false,
                pending:false
            });

        case ACTIONS.GET_MEMBER:
            return Object.assign({}, state, {
                pending: true
            });

        case ACTIONS.GET_MEMBER_OK:
            return Object.assign({}, state, {
                response: aciton.response,
                pending: true
            });

        case ACTIONS.GET_USER:

            return {...state, user: action.payload}

        default:
            return state;

    }

}

export default appReducer;
