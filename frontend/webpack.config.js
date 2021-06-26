const path = require('path'); // 여기는 import 가 안되는 이유가 node 로 돌리는거라서 안됨
const RefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');
// process.env.NODE_ENV = 'production'; // 환경변수 production 으로 하면 배포모드

// 웹팩 설정
module.exports = {
  name: 'frankly-app',
  mode: 'development', // 실서비스: production / development
  devtool: 'eval', // 실서비스 : hidden-source-map / eval
  resolve: {
    extensions: ['.js', '.jsx'] // entry 에 확장자 일일이 다 적기 귀찮으니 여기서 설정
  },

  // **중요
  entry: { // 입력
    app: ['./index'], // client 불러옴
  },

  module: {
    rules: [{
      test: /\.jsx?/, // jsx 파일에 옛날브라우저에서도 돌아갈수있는 문법으로 바꿔주겠다.
      loader: 'babel-loader',
      options: {
        presets: [
          ['@babel/preset-env', {
            targets: {
              browsers: ['> 1% in KR',] // 지원할 브라우저 설정 https://github.com/browserslist/browserslist
            },
            debug: true,
          }],
          '@babel/preset-react'
        ],
        plugins: [
          // "@babel/plugin-transform-runtime", // asinc / await 문제 해결하려고 설치 (미해결)
          '@babel/plugin-proposal-class-properties',
          'react-refresh/babel', // 설치를 안해도 리로딩되지만 핫리로딩이랑 리로딩은 다르다. -> 브라우저 새로고침되면 기존 데이터가 다 날라간다.
        ],
      },
    }],
  },
  plugins: [
    new RefreshWebpackPlugin()
  ],
  output: { // 출력
    filename: 'app.js',
    path: path.join(__dirname, 'dist'), // node 에서 쓰는 경로 기술 / 현재폴더 안에 있는 dist 폴더
    publicPath: '/dist/',
  },
  devServer: { // 프론트 개발 편의를 위해 webpack dev server 만듬
    publicPath: '/dist/', // dist 폴더에 결과물을 저장함 webpack devServer 는 핫리로더 변경점이 생기면 저장물 수정을 해준다.
    hot: true,
  },
}

// 결과적으론  index.js 를 찾아서 app.js 로 만들어 준다.