const { defineConfig } = require('@vue/cli-service')
const path = require("path")

module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  css : {
    loaderOptions : {
        sass : {
            additionalData: `
              @import "@/assets/scss/reset.scss";
            `
        }
    }
},
devServer: {
  overlay: false,
  port: 8000,
  proxy:{
    '/api': {
      target:'http://localhost:8081', //요청할 서버 주소
      changeOrigin: true,
      logLevel: 'debug', //터미널에 proxy 로그가 찍힌다.
      pathRewrite: {
        '^api' : ''
      }
    }
  },
  indexPath: '../../templates/vue/index.html',
  outputDir: path.resolve(__dirname, "../restapi/src/main/resources/static/vue")
}
})
