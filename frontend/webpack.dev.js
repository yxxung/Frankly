const path = require('path');
const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');

const port = process.env.PORT || 3000;

module.exports = merge(common, {
  mode: 'development',
  devtool: 'eval',

  devServer: { // 프론트 개발 편의를 위해 webpack dev server 만듬
    historyApiFallback: true, // Cannot GET /.. 에러 문제
    publicPath: '/', // webpack devServer 는 핫리로더 변경점이 생기면 저장물 수정을 해준다.
    contentBase: path.join(__dirname, "public"),
    port: port,
    hot: true,
    // CORS 에러
    proxy: {
      '/api': {
        target: 'http://frankly.kro.kr:8081',
        changeOrigin: true,
        pathRewrite: { '^/api': '' },
      }
    },
  },
});