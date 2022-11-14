import { login, findById } from "@/js/user.js";

export const userStore = {
    namespaced: true,
    state: {
        //로그인 여부
        isLogin: false,
        //로그인 오류
        isLoginError: false,
        //유저정보
        userInfo: null,
        //userID
        userID: null
    },
    getters: {
        checkUserInfo(state) {
            return state.userInfo;
        },
    },
    mutations: {
        //로그인 여부 상태 저장
        SET_IS_LOGIN(state, isLogin) {
            state.isLogin = isLogin;

        },
        SET_IS_LOGIN_ERROR(state, isLoginError){
            state.isLoginError = isLoginError;
        },
        //유저 정보 저장
        SET_USER_INFO(state, userInfo) {
            if (userInfo != null) {
                state.isLogin = true;
            }
            state.userInfo = userInfo;
        },
        //유저 아이디 저장
        SET_USER_ID(state, userID) {
            state.userID = userID
        }
    },
    actions: {
        /*async userConfirm({ commit }, user) {
            await login(
                user,
                (response) => {
                    console.log("userConfirm", response);
                    if (response.data.status === 200) {
                        let token = response.data.token;
                        let userID = response.data.userID;
                        commit("SET_IS_LOGIN", true);
                        commit("SET_IS_LOGIN_ERROR", false);
                        commit("SET_USER_ID", response.data.userID);
                        sessionStorage.setItem("token", token);
                        sessionStorage.setItem("userID", userID);
                    } else {
                        commit("SET_IS_LOGIN", false);
                        commit("SET_IS_LOGIN_ERROR", true);
                    }
                }
            );
        },*/
        async getUserInfo({ commit }, userID) {
            await findById(
                userID,
                (response) => {
                    console.log("getUserInfo", response);
                    if (response.status === 200) {
                        commit("SET_USER_INFO", response.data);
                        console.log("SET_USER_INFO", response.data)
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