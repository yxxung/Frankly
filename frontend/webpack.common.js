const path = require('path');
const RefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  name: 'frankly-app',
  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.json', '.jsx', '.css'],
  },

  entry: {
    app: './index.js',
  },

  output: {
    path: path.join(__dirname, 'dist'),
    filename: 'app.js',
    publicPath: '/dist/',
  },

  module: {
    rules: [{
      test: /\.jsx?$/,
      exclude: ['/node_modules'],
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
          '@babel/plugin-proposal-class-properties',
          'react-refresh/babel',
        ],
      },
    },
      {
        test: /\.html$/,
        use: [
          {
            loader: 'html-loader',
            options: {
              minimize: true,
            },
          },
        ],
      }],
  },

  plugins: [
    new RefreshWebpackPlugin(),
    // new HtmlWebpackPlugin({
    //   template: './public/index.html',
    // })
  ],
}

