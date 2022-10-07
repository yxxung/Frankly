<template>

</template>

<script>
export default {
  name: "inputValue",
  props: ['inputValue'],
  methods: {
    getInput: function (event){
      this.$emit('input', event.target.value)
    }
  }
}
</script>

<style scoped>

</style>
