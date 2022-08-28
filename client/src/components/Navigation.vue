<template>
    <nav class="bottom-nav">
        <div class="bottom-nav-area">
            <a href="/">
                <img src="@/assets/icon/nav/Home.svg" alt="홈으로 이동">
                <p>홈</p>
            </a>
            <a href="/Community">
                <img src="@/assets/icon/nav/Chat.svg" alt="홈으로 이동">
                <p>커뮤니티</p>
            </a>
            <a href="/Politician">
                <img src="@/assets/icon/nav/NtnlAsmbl.svg" alt="홈으로 이동">
                <p>국회의원</p>
            </a>
            <a href="/Mypage">
                <img src="@/assets/icon/nav/User.svg" alt="홈으로 이동">
                <p>내 정보</p>
            </a>
        </div>
    </nav>
</template>

<script>
export default {
    data() {
        return {
            lists: [
                { link: '/', title: 'Home' },
                { link: '/Community', title: 'Community' },
                { link: '/Politician', title: 'Politician' },
                { link: '/Mypage', title: 'Mypage' }
            ]
        }
    },
}
</script>

<style lang="style.scss">
@import '../assets/scss/style.scss';

.bottom-nav {
    position: fixed;
    bottom: 0;
    width: 100%;
    max-width: 540px;
    height: 64px;
    display: flex;
    justify-content: center;
    background-color: rgb(255, 255, 255);
    box-shadow: 0 -1px 2px rgba(0, 0, 0, 0.1);
}

.bottom-nav-area {
    width: 90%;
    display: flex;
    justify-content: space-between;
}

.bottom-nav-area a {
    width: 56px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-decoration: none;
}

.bottom-nav-area span {
    color: #B5B5B5;
}

.bottom-nav-area p {
    margin-top: 2px;
    font-size: 10px;
    color: #B5B5B5;
}

.nav--active p {
    color: black;
}
</style>
