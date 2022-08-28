<template>
    <div>
        <div class="wrap">
            <!--헤더-->
            <header class="header header--back">
                <a class="icon-button-56 header__back-button" href="index.html">
                    <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기">
                </a>
                <div class="header-right-icon">
                    <a class="icon-button-56">
                        <img src="@/assets/icon/Share.svg" alt="공유하기">
                    </a>
                    <a class="icon-button-56">
                        <img src="@/assets/icon/Other2.svg" alt="더보기">
                    </a>
                </div>
            </header>

            <!--타이틀-->
            <div class="post-header">
                <div class="post-header__kategorie">커뮤니티 > 자유게시판</div>
                <h3 class="post-header__title">게시글 제목임이밍미</h3>
                <div class="post-header__info">
                    <div class="post-header__writer">익명</div>
                    <div class="post-header__reg-date">2021.12.03 15:03</div>
                </div>
            </div>

            <!--내용-->
            <article class="post-content">
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ducimus est eum nemo perferendis! Accusantium consequatur, dicta dignissimos, earum, illo ipsa iste officiis pariatur provident quam quo ratione reiciendis sed totam!</p>
            </article>

            <!--좋아요, 싫어요-->
            <div class="post-like">
                <button>좋아요</button>
                <button>싫어요</button>
            </div>

            <!--댓글-->
            <div class="comments">
                <ul>
                    <li class="comments__box">
                        <div class="comments__info">
                            <div class="comments__info-left">
                                <img src="@/assets/icon/Anonymous_user.svg" alt="익명유저">
                                <h6>익명</h6>
                                <span class="comments__info__date">36분전</span>
                            </div>

                            <div class="comments__info-right">
                                <button class="icon-button-24">
                                    <img src="@/assets/icon/Other1.svg" alt="더보기">
                                </button>
                            </div>
                        </div>
                        <div class="comments__text">
                            나는 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
                        </div>
                    </li>

                    <li class="comments__box">
                        <div class="comments__info">
                            <div class="comments__info-left">
                                <img src="@/assets/icon/Anonymous_user.svg" alt="익명유저">
                                <h6>익명</h6>
                                <span class="comments__info__date">36분전</span>
                            </div>

                            <div class="comments__info-right">
                                <button class="icon-button-24">
                                    <img src="@/assets/icon/Other1.svg" alt="더보기">
                                </button>
                            </div>
                        </div>
                        <div class="comments__text">ㅋㅋㅋㅋㅋ웃기</div>
                    </li>

                    <!--대댓글 class에 comments__box--reply 추가-->
                    <li class="comments__box comments__box--reply">
                        <div class="comments__info">
                            <div class="comments__info-left">
                                <img src="@/assets/icon/Anonymous_user.svg" alt="익명유저">
                                <h6>익명</h6>
                                <span class="comments__info__date">36분전</span>
                            </div>

                            <div class="comments__info-right">
                                <button class="icon-button-24">
                                    <img src="@/assets/icon/Other1.svg" alt="더보기">
                                </button>
                            </div>
                        </div>
                        <div class="comments__text">엌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ</div>
                    </li>

                </ul>

                <div class="comments__plus">
                    <button class="comments__plus-button">댓글 32개 더보기...</button>
                </div>
            </div>
        </div>

        <!--댓글 입력창-->
        <div class="enter-comment">
            <textarea name="comment" id="comment" cols="30" rows="10" placeholder="댓글 입력..." class="enter-comment__textarea"></textarea>
            <button class="enter-comment__submit">
                <img src="@/assets/icon/Comment.svg" alt="댓글 전송 버튼">
            </button>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style lang="style.scss">
@import "@/assets/scss/style.scss";

</style>