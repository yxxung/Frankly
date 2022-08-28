<template>
    <div class="wrap">
        <!--헤더-->
        <header class="header header--back">
            <a class="icon-button-56 header__back-button" href="/Community">
                <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기">
            </a>
            <h2>자유게시판</h2>
        </header>

        <ul class="post-list">
            <li class="post-list__container" id="post123">
                <div class="post-list__title">
                    <img src="@/assets/icon/Image.svg" alt="이미지 있음">
                    <h3>정치 잘 모르는 사람들을 위...<span>[110]</span></h3>
                </div>
                <p>자 내글을 잘봐 이건말이</p>
                <div class="post-list__info">
                    <span>1시간 전</span>
                    <img src="@/assets/icon/Like.svg" alt="좋아요">
                    <span>13</span>
                </div>
            </li>

            <li class="post-list__container">
                <div class="post-list__title">
                    <h3>가나다라<span>[11239]</span></h3>
                </div>
                <p>자 내글을 잘봐 이건말이</p>
                <div class="post-list__info">
                    <span>12/11</span>
                    <img src="@/assets/icon/Like.svg" alt="좋아요">
                    <span>20345</span>
                </div>
            </li>
        </ul>
        <FloatingButton />
        <Navigation />
    </div>
</template>

<script>
import Navigation from '@/components/Navigation.vue'
import FloatingButton from '@/components/FloatingButton.vue'

export default {
    components : {
        'Navigation': Navigation,
        'FloatingButton': FloatingButton
    },
    methods: {
        // 무한 스크롤 정의
        handleNotificationListScroll(e) {
        const { scrollHeight, scrollTop, clientHeight } = e.target;
        const isAtTheBottom = scrollHeight === scrollTop + clientHeight;
        // 일정 한도 밑으로 내려오면 함수 실행
        if (isAtTheBottom) this.handleLoadMore();
        },

        // 내려오면 api 호출하여 아래에 더 추가, total값 최대이면 호출 안함
        handleLoadMore() {
        if (this.notifications.length < this.total) {
            const params = {
            limit: this.params.limit,
            page: this.params.page + 1
            };
            this.$store.commit(
            "notification/SET_PARAMS",
            this.filterValue ? { ...params, type: this.filterValue } : params
            );
            this.dispatchGetNotifications(false);
        }
        },

        // 스크롤을 맨위로 올리고 싶을 때
        handleClickTitle() {
        this.$refs["notification-list"].scroll({ top: 0, behavior: "smooth" });
        },

        // 새로고침
        handleClickRefresh() {
        this.$refs["notification-list"].scroll({ top: 0 });
        this.dispatchGetNotifications(true);
        },

        // 처음 렌더링시 이전 알림 불러오기 or reset=true시 새로고침, false시 이전 목록에 추가
        dispatchGetNotifications(reset) {
        this.$store.dispatch("notification/getNotifications", reset);
        }
    }
}
</script>

<style lang="style.scss">
@import "@/assets/scss/style.scss";

/*
게시판 목록
*/

.community-list {
    padding: 8px 24px;
}

.community-list > h4 {
    margin-bottom: 8px;
    font-size: 14px;
    font-weight: normal;
    color: #818181;
}

.community-list a {
    padding: 8px;
    display: flex;
    align-items: center;
    color: #2B2B2B;
    font-size: 16px;
}
.community-list a:hover {
    background-color: #f8f8f8;
}
.community-list img {
    margin-right: 8px;
}

/*
게시글 목록
*/

.post-list {
    padding-top: 14px;
}

/* 게시글 박스 */
.post-list__container {
    position: relative;
    padding: 16px 24px 30px;
    border-bottom: 1px solid #E7E7E7;
    -webkit-transition: all 0.08s ease-in-out;
    -o-transition: all 0.08s ease-in-out;
    transition: all 0.08s ease-in-out;
}
.post-list__container:hover {
    background-color: #f8f8f8;
    cursor: pointer;
}

/* 게시글 제목 */
.post-list__title {
    margin-bottom: 4px;
    display: flex;
    align-items: center;
}
.post-list__title > img {
    margin-right: 8px;
}
.post-list__title > h3 {
    font-size: 16px;
}
.post-list__title > h3 > span {
    font-family: "Roboto", serif;
    font-size: 14px;
    font-weight: bold;
    color: #ff3a3a;
}

/* 게시글 내용 */
.post-list__container > p {
    font-size: 14px;
    color: #7B7B7B;
}

/* 게시글 등록시간, 좋아요 수 */
.post-list__info {
    position: absolute;
    right: 24px;
    bottom: 8px;
    display: flex;
    align-items: center;
    color: #7B7B7B;
}
.post-list__info > span {
    font-size: 12px;
}

/*
게시글 페이지
*/

.post-header {
    padding: 0 16px;
}

.post-header__kategorie {
    padding: 4px 0;
    font-size: 12px;
    color: #696969;
}

.post-header__title {
    font-size: 20px;
    color: #2B2B2B;
}

.post-header__info {
    margin: 8px 0;
    display: flex;
    justify-content: space-between;
}

.post-header__writer {
    font-size: 12px;
    color: #696969;
}

.post-header__reg-date {
    font-size: 12px;
    color: #696969;
}

.post-content {
    padding: 0 16px;
}

/*게시글 좋아요, 싫어요*/
.post-like {
    padding: 24px 16px;
}
.post-like button {
    margin-right: 8px;
    background-color: #f3f3f3;
}

/*댓글창*/
.comments {

}

.comments__box {
    padding: 8px 16px;
    border-bottom: 1px solid #f6f6f6;
}

.comments__box--reply {
    padding-left: 32px;
    position: relative;
}

.comments__box--reply:before {
    position: absolute;
    top: 12px;
    left: 16px;
    content: "";
    display: block;
    width: 14px;
    height: 14px;
    background-image: url("@/assets/icon/Reply.svg");
    background-repeat: no-repeat;
}

.comments__info {
    margin-bottom: 4px;
    display: flex;
    justify-content: space-between;
}

.comments__info h6 {
    padding: 0 12px 0 8px;
    font-size: 14px;
    color: #696969;
}

.comments__info-left {
    display: flex;
    align-items: center;
}

.comments__info-right {

}

.comments__info__date {
    font-size: 12px;
    color: #696969;
}

.comments__plus {
    padding: 16px;
}

.comments__plus-button {
    padding: 14px 0;
    width: 100%;
    border-radius: 12px;
    color: #424242;
    background-color: #f1f1f1;
}

.comments__plus-button:hover {
    background-color: #e7e7e7;
}

/*댓글 입력창*/
.enter-comment {
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 64px;
    display: flex;
    justify-content: center;
    background-color: rgb(255, 255, 255);
}

.enter-comment__textarea {
    margin: 8px 16px 0;
    padding: 8px 40px 0 24px;
    height: 32px;
    border-radius: 24px;
    font-family: "Noto Sans KR", sans-serif;
    font-size: 16px;
    color: #2B2B2B;
    background-color: #f8f8f8;
    outline: 0;
    border: 0;
}

.enter-comment__textarea:focus-visible {
    outline: 0;
    /*box-shadow: 0 0 0 2px #000 inset;*/
}

.enter-comment__submit {
    position: absolute;
    top: 8px;
    right: 16px;
    width: 40px;
    height: 40px;
    border-radius: 40px;
}

.enter-comment__submit:hover {
    background-color: #CCCCCC;
}
</style>