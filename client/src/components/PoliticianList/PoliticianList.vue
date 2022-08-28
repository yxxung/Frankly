<template>
    <div class="politician-list">
        <div class="politician">
            <PoliticianItem
            v-for="politician in politicians"
            :key="politician.politicianID"
            :politician="politician" />
        </div>
    </div>
</template>
<script>
import PoliticianItem from '@/components/PoliticianList/PoliticianItem.vue'

export default {
    name: 'PoliticianList',
    components: {
        'PoliticianItem': PoliticianItem
    }
}
</script>

<style>
.politician {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
</style>