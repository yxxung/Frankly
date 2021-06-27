const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');

const port = process.env.PORT || 8080;

module.exports = merge(common, {
  mode: 'development',
  devtool: 'eval',
  devServer: { // 프론트 개발 편의를 위해 webpack dev server 만듬
    publicPath: '/dist/', // dist 폴더에 결과물을 저장함 webpack devServer 는 핫리로더 변경점이 생기면 저장물 수정을 해준다.
    port: port,
    hot: true,
  },
});