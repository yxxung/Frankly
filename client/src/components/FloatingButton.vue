<template>
    <div class="floating-button">
        <img src="@/assets/icon/Write.svg" />
    </div>
</template>

<script>
export default {
    name: 'FloatingButton'
}
</script>

<style>
/*위치 수정 필요*/
.floating-button {
    position: fixed;
    right: 35%;
    line-height: 63px;
    bottom: 90px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background-color: #2F2F2F;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    z-index: 999;
}

.floationg-button img {
    widows: 25px;
    height: 25px;
    filter: invert(100%) sepia(6%) saturate(7500%) hue-rotate(305deg) brightness(96%) contrast(96%);
}
</style>