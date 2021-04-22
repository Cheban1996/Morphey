import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vSelect from 'vue-select'
import './websockets'
import api from "./apiMorphey";


Vue.config.productionTip = false;
Vue.component('v-select', vSelect);

Vue.prototype.api = api;


new Vue({
    router,
    store,
    render: function (h) {
        return h(App)
    }
}).$mount('#app');
