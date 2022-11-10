import { http } from "./http.js";

// 로그인 통신함수
async function login(user, success, fail) {
    await http
        .post(`/api/auth/signin`, JSON.stringify(user))
        .then(success)
        .catch(fail);
}

// id를 기준으로 토큰 확인 통신함수
async function findById(userID, success, fail) {
    http.defaults.headers["jwttoken"] =
        sessionStorage.getItem("jwttoken");
    await http.get(`/api/users/${userID}`).then(success).catch(fail);
}

export { login, findById };