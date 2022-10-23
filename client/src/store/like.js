import { createStore } from 'vuex'
import BoardDetail from '@/views/Board/BoardDetail.vue';

export default createStore({
    state: {
        BoardDetail: BoardDetail
    },
    mutations: {
        changeLikes(state) {
            console.log(state.BoardDetail.marked);
            
        }
    }

})