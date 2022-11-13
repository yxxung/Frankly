<template>
  <div class="floating-button-wrap">
    <div class="floating-button"
         @click="write">
      <img src="@/assets/icon/Write.svg" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'FloatingButton',
  methods: {
    write() {
      this.$router.push({
        path: '/WriteBoard'
      })
    }
  },
}
</script>

<style>
.floating-button {
  position: fixed;
  line-height: 63px;
  width: 62px;
  height: 62px;
  border-radius: 50%;
  background-color: #2F2F2F;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.16), 0 2px 10px 0 rgba(0, 0, 0, 0.12);
  z-index: 999;
  top: 75%;
  /*margin: auto 0 0 auto;*/
  margin-left: 60%;
  /*float: right;*/
}
.floating-button-wrap{
  display: flex;
  /*align-items: r;*/
  /*margin-left: auto;*/
  width: 100%;
  max-width: 520px;
}
.floating-button:hover {
  background: #4a4a4a;
}
.floationg-button img {
  widows: 28px;
  height: 28px;
  filter: invert(100%) sepia(6%) saturate(7500%) hue-rotate(305deg) brightness(96%) contrast(96%);
}
</style>
