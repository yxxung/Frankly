const path = require('path');
const RefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');
const HtmlWebPackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  name: 'frankly-app',
  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.json', '.jsx', '.css'],
  },

  entry: {
    app: './src/index.js',
  },

  output: {
    path: path.join(__dirname, 'public'),
    // publicPath: '/', // 배포할때 publicPath 주소(?)
    filename: '[name].js',
  },

  module: {
    rules: [
      {
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
          'react-refresh/babel', // 배포할때 주석
        ]},
      },
      {
        test: /\.html$/,
        use: [
          {
            loader: "html-loader",
            options: { minimize: true }
          }
        ]
      },
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: {
              modules: true, // CSS module
            }
          }
        ],
      },
      {
        test: /\.scss$/,
        use: [
          'style-loader',
          'css-loader',
          'resolve-url-loader',
          'sass-loader'
        ]
      },
      {
        test: /\.(ico|png|jpg|jpeg|gif|svg|woff|woff2|ttf|eot)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        loader: 'url-loader',
        options: {
          name: '[hash].[ext]',
          limit: 10000,
        }
      },
    ],
  },

  plugins: [
    new RefreshWebpackPlugin(),
    new HtmlWebPackPlugin({
      template: './src/index.html',
      filename: './index.html',
      showErrors: true,
    }),
    new MiniCssExtractPlugin({
      filename: 'style.css'
    })
  ],
}

