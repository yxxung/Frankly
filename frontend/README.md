##명령어
###$ npm install
* package.json 설치  
###$ npm run dev
* 웹팩 서버에서 핫리로더로 실시간 개발환경
* 배포용 명령어는 아직 없음

##package.json
### webpack webpack-cli
* 웹팩
### @babel/core @babel/preset-env
* core는 기본적이고 env가 브라우저에 맞게 최신문법을 옛날문법 지원
### @babel/preset-react
* preset-react가 jsx를 지원함
### babel-loader
* 바벨이랑 웹팩을 연결해줌
### @babel/plugin-proposal-class-properties
* state = { } << 이 문법 쓰려면 설치
### react-refresh @pmmmwh/react-refresh-webpack-plugin -D
* 핫리로더
### webpack-dev-server
* 개발용 서버
