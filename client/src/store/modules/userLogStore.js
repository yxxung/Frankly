export const userLogStore = {
    namespaced: true,
    state: {
        likeBoardList: [], //좋아요한 게시글 아이디,
        BookmarkPoliticianList: []//북마크한 국회의원 아이디
    },
    mutations: {
        // 게시글 좋아요
        LIKE_BOARD_LIST(state, boardID) {
            state.likePostList.push(boardID);
        },

        // 게시글 좋아요취소
        UNLIKE_BOARD_LIST(state, boardID) {
            const i = state.likePostList.indexOf(boardID);
            state.likeBoardList.splice(i, 1);
        },

        // 국회의원 북마크
        BOOKMARK_POLITICIAN_LIST(state, postId) {
            state.BookmarkPoliticianList.push(postId);
        },

        // 국회의원 북마크 취소
        UNBOOKMARK_POLITICIAN_LIST(state, postId) {
            const i = state.BookmarkPoliticianList.indexOf(postId);
            state.BookmarkPoliticianList.splice(i, 1);
        },
    },
    actions: {
        // 게시글 좋아요
        likeBoardList({ commit}, boardID) {
            commit('LIKE_POST_LIST', boardID);
        },

        // 게시글 좋아요취소
        unlikeBoardList({ commit}, boardID) {
            commit('UNLIKE_POST_LIST', boardID);
        },

        // 국회의원 북마크
        bookmarkPoliticianList({ commit }, politicianID) {
            commit('SCRAP_POST_LIST', politicianID);
        },

        // 국회의원 북마크 취소
        unbookmarkPoliticianList({commit}, politicianID) {
            commit('UNSCRAP_POST_LIST', politicianID);
        },
    }
};

export default userLogStore;