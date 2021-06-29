/**
 *@author 최제현
 * @date 2021/06/29
 * 엑션
 */

//GET
export const GET_MEMBER = "GET_MEMBER";
export const GET_MEMBER_CALL = "GET_MEMBER_CALL";
export const GET_MEMBER_OK = "GET_MEMBER_OK";

//인증성공
export const AUTH_SUCCESS = "AUTH_SUCCESS";

//인증실패 또는 JWT 만료
export const AUTH_FAILED = "AUTH_FAILED";

//사용자 기본정보 조회
export const GET_USER = "GET_USER";

//export const GET_USER_CALL = "GET_USER_CALL";
export const GET_USER_OK = "GET_USER_OK";
//
// //POST
// // 아직은 post 활용할 일 없을듯
// export const POST_MEMBER = "POST_MEMBER";
// export const POST_MEMBER_CALL = "POST_MEMBER_CALL";
// export const POST_MEMBER_OK = "POST_MEMBER_OK";

// action create

export const getMember = (params) => ({
    type: GET_MEMBER,
    //전송 데이터
    payload: params
});

export const getMemberCall = (params) => ({
    type: GET_MEMBER_CALL,
    payload: params
});

export const getMemberOK = (params) => ({
    type: GET_MEMBER_OK,
    payload: params
});

export const authSucess = (params) => ({
    type: AUTH_SUCCESS,
    payload: params
});

export const authFailed = (params) => ({
    type: AUTH_FAILED,
    payload: params
});

export const getUser= (params) => ({
    type: GET_USER,
    payload: params
});

export const getUserOK= (params) => ({
    type: GET_USER_OK,
    payload: params
});
