import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        klines: {}
    },
    mutations: {
        loadKlines(state, data) {
            state.klines = data;
        }
    },
    actions: {},
    modules: {}
})
