import { http } from "./http.js";
import axios from 'axios';

// 로그인 통신함수
async function login(user, success, fail) {
    axios
        .post(`/api/auth/signin`, JSON.stringify(user), {
            headers: { "Content-Type": `application/json`}
        }
        )
        .then(success)
        .catch(fail);
}

// id를 기준으로 토큰 확인 통신함수
async function findById(userID, success, fail) {
    axios.defaults.headers["token"] =
        sessionStorage.getItem("token");

    axios.get(`/api/users/${userID}`).then(success).catch(fail);
}

export { login, findById };