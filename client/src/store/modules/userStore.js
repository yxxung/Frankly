import jwt_decode from "jwt-decode";
import { login, findById } from "@/js/user.js";

export const userStore = {
    namespaced: true,
    state: {
        isLogin: false,
        //로그인 오류
        isLoginError: false,
        //유저정보
        userInfo: null,
    },
    getters: {
        checkUserInfo: function (state) {
            return state.userInfo;
        },
    },
    mutations: {
        //로그인 여부 상태 저장
        SET_IS_LOGIN: (state, isLogin) => {
            state.isLogin = isLogin;

        },
        SET_IS_LOGIN_ERROR: (state, isLoginError) => {
            state.isLoginError = isLoginError;
        },
        SET_USER_INFO: (state, userInfo) => {
            if (userInfo != null) {
                state.isLogin = true;
            }
            state.userInfo = userInfo;
        },
    },
    actions: {
        async userConfirm({ commit }, user) {
            await login(
                user,
                (response) => {
                    console.log(response);
                    if (response.status === 200) {
                        let token = response.data["jwttoken"];
                        commit("SET_IS_LOGIN", true);
                        commit("SET_IS_LOGIN_ERROR", false);
                        sessionStorage.setItem("jwttoken", token);
                    } else {
                        commit("SET_IS_LOGIN", false);
                        commit("SET_IS_LOGIN_ERROR", true);
                    }
                }
            );
        },
        async getUserInfo({ commit }, token) {
            let decode_token = jwt_decode(token);
            await findById(
                decode_token.userID,
                (response) => {
                    if (response.data.message === "success") {
                        console.log(response.data.userInfo); //로그인한 userInfo 확인
                        commit("SET_USER_INFO", response.data.userInfo);
                        console.log(response.data.userInfo)
                    } else {
                        console.log("유저 정보 없음");
                    }
                },
                (error) => {
                    console.log(error);
                }
            );
        },
    }
};