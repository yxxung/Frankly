<template>
    <div class="politician">
        <div class="politician-image"
        :style="{backgroundImage: `url(${politician.politicianImage})`}">
        </div>
        <div class="politician-name">
          {{politician.politicianName}}
        </div>
    </div>
</template>

<script>
export default {
  props: {
    politician: {
      type: Object,
      default: () => ({

      })
    }
  }
}
</script>

<style>

</style>