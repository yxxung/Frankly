import { http } from "@/js/http.js";

export const userLogStore = {
    namespaced: true,
    state: {
        likeBoardList: [], //좋아요한 게시글 아이디
    },
    mutations: {
        // 게시글 좋아요
        LIKE_POST_LIST(state, boardID) {
            state.likePostList.push(boardID);
        },

        // 게시글 좋아요취소
        UNLIKE_POST_LIST(state, boardID) {
            const i = state.likePostList.indexOf(boardID);
            state.likeBoardList.splice(i, 1);
        },
    },
    actions: {
        // 게시글 좋아요
        likePostList({ commit}, boardID) {
            commit('LIKE_POST_LIST', boardID);
        },

        // 게시글 좋아요취소
        unlikePostList({ commit}, boardID) {
            commit('UNLIKE_POST_LIST', boardID);
        },
    }
};

export default userLogStore;