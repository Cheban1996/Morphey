import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vSelect from 'vue-select'
import './websockets'
// import {init_websocket} from "./websockets";
//
// init_websocket();

Vue.config.productionTip = false;
Vue.component('v-select', vSelect);


new Vue({
  router,
  store,
  render: function (h) {
    return h(App)
  }
}).$mount('#app');
