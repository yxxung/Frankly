<template>
    <div class="wrap">
    <!--헤더-->
    <header class="header header--back">
        <a class="icon-button-56 header__back-button" href="#">
            <img src="@/assets/icon/Arrow_left48.svg" alt="뒤로가기">
        </a>
    </header>

    <div class="sign-up-title">
        <h3>회원가입</h3>
    </div>

    <form class="sign-up-form">
<!--이메일-->
        <label>
            <p class="sign-up-form__input-info">이메일</p>
            <input class="sign-up-form__text-input" type="email" placeholder="example@gmail.com">
            <p class="sign-up-form__error-message">올바른 이메일 형식을 입력해주세요.</p>
        </label>

<!--비밀번호-->
        <label>
            <p class="sign-up-form__input-info">비밀번호</p>
            <input class="sign-up-form__text-input" type="email" placeholder="대소문자, 숫자, 특수문자 포함 8~16자리" maxlength="16">
            <p class="sign-up-form__error-message">대소문자, 숫자, 특수문자 포함 8~16자리</p>
        </label>
        <!--input 양식 에러발생 시 label 태그에 sign-up-form--error 클래스-->
        <label class="sign-up-form--error">
            <input class="sign-up-form__text-input" type="password" placeholder="비밀번호 확인">
            <p class="sign-up-form__error-message">비밀번호가 같지 않습니다.</p>
        </label>

<!--지역-->
        <label>
            <p class="sign-up-form__input-info">지역</p>
            <div class="dropdown-container">
                <select class="sign-up-form__dropdown" name="city" id="city">
                    <option value="1">서울</option>
                    <option value="2">Dave</option>
                    <option value="3">Pumpernickel</option>
                </select>

                <select class="sign-up-form__dropdown" name="county" id="county">
                    <option value="100">강남구갑</option>
                    <option value="101">Dave</option>
                    <option value="102">Pumpernickel</option>
                </select>
            </div>
        </label>

<!--이용동의 체크-->
        <div class="form__check">
            <ul>
                <li class="check-box-line">
                    <p>아래 약관에 모두 동의합니다.</p>
                    <input type="checkbox" id="all-check" class="input-checkbox">
                    <label for="all-check"></label>
                </li>
                <li>
                    <a>[필수] 개인정보 수집 및 이용 동의</a>
                    <input type="checkbox" id="privacy-check" class="input-checkbox" name="signUp">
                    <label for="privacy-check"></label>
                </li>
                <li>
                    <a>[필수] 서비스 이용약관 동의</a>
                    <input type="checkbox" id="service-check" class="input-checkbox" name="signUp">
                    <label for="service-check"></label>
                </li>
            </ul>
        </div>
        <button class="sign-up-form__button" onclick="location.href='/index.html'">가입완료</button>
    </form>
</div>
</template>

<style>
.sign-up-title {
    padding: 0 24px;
    height: 48px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.sign-up-title > h3 {
    font-size: 24px;
}

.sign-up-title > h3 > span {
    font-size: 16px;
}

.sign-up-title p {
    font-family: 'Roboto', sans-serif;
    font-size: 16px;
    font-weight: bold;
}

.sign-up-form {
    margin-top: 24px;
    padding: 0 24px;
}

.sign-up-form > label {
    margin-top: 16px;
    display: block;
}

/*
이메일, 비밀번호 입력 input / button
*/
.sign-up-form__text-input[type=email],
.sign-up-form__text-input[type=password] {
    box-sizing: border-box;
    padding-left: 8px;
    width: 100%;
    height: 48px;
    cursor: text;
    background-color: #FAFAFA;
    -webkit-transition: all 0.2s ease-in-out;
    -o-transition: all 0.2s ease-in-out;
    transition: all 0.2s ease-in-out;
}

.sign-up-form__text-input[type=email]:focus-visible,
.sign-up-form__text-input[type=password]:focus-visible {
    outline: 0;
    box-shadow: inset 0 -2px 0 #000000;
}

.sign-up-form__input-info {
    margin: 2px 0;
    font-size: 14px;
    color: #A9A9A9;
}

.sign-up-form__error-message {display: none}
.sign-up-form--error > .sign-up-form__error-message {
    margin-top: 4px;
    display: block;
    font-size: 14px;
    color: #da8282;
}

.sign-up-form--error > input {
    outline: 0;
    box-shadow: inset 0 -2px 0 #ff3030;
}

.sign-up-form__button {
    margin-top: 24px;
    width: 100%;
    height: 48px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 16px;
    color: white;
    background-color: black;
    -webkit-transition: all 0.2s ease-in-out;
    -o-transition: all 0.2s ease-in-out;
    transition: all 0.2s ease-in-out;
}

.sign-up-form__button:hover {
    background-color: #343434;
}

.sign-up-form__button:disabled {
    background-color: #C5C5C5;
}

/*
회원가입 지역 선택 dropdown
*/
.dropdown-container {
    width: 100%;
    display: flex;
    justify-content: space-between;
}

.sign-up-form__dropdown {
    box-sizing: border-box;
    padding-left: 8px;
    height: 48px;
    background-color: #FAFAFA;
}
.dropdown-container > .sign-up-form__dropdown:nth-child(2) { width: 100%; }
.dropdown-container > .sign-up-form__dropdown:nth-child(1) { margin-right: 16px; }

.sign-up-form__dropdown:focus-visible {
    outline: 0;
    box-shadow: inset 0 -2px 0 #000000;
}

.form__check {
    margin-top: 24px;
}
.form__check > ul > li {
    padding: 8px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.check-box-line {
    border-bottom: 1px solid #BFBFBF;
}

.log-in__check {
    margin: 16px 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 14px;
}
.remember-email {
    display: flex;
    align-items: center;
}
.remember-email label {
    margin-right: 8px;
}
</style>