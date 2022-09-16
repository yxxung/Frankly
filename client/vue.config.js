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
  proxy:'http://localhost:8081'
},
indexPath: '../../templates/vue/index.html',
publicPath: '/',
outputDir: path.resolve(__dirname, "../restapi/src/main/resources/static/vue"),

})
