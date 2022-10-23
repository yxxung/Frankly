<template>
    <div v-if="edit_modal" @click.self="handleClosePopup" @keyup.self="handleClosePopup">
        <button @click="handleClosePopup" @keyup="handleClosePopup">
        </button>
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>