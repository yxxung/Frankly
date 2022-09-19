<template>
    <div class="politician-list">
        <div class="politician">
            <!-- 정치인 리스트 출력 -->
            <PoliticianItem
            v-for="politician in politicianItem"
            :key="politician.politicianID"
            :politician="politician" />
        </div>
    </div>
</template>
<script>
import PoliticianItem from '@/views/Politician/PoliticianItem.vue'

export default {
    name: 'PoliticianList',
    components: {
        'PoliticianItem': PoliticianItem
    },
    methods: {
        getPoliticianList() {
            console.log(this.$axios);
            axios.get('/api/infos/all')
            .then(response => {
                console.log('politicianItem', response.data)
                this.politicianItem = response.data;
            })
            .catch(error => {
                console.log(error)
            })
        }
    },
}
</script>

<style>
.politician {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
</style>