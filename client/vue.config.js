const { defineConfig } = require('@vue/cli-service')
const path = require("path")

module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  css : {
    loaderOptions : {
        scss : {
            additionalData: `@import "~@/assets/scss/reset.scss";`
        }
    }
  }
})
