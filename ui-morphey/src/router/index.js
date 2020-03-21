import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Trade from "../views/Trade";
import Exchange from "../views/Exchange";

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },{
        path: '/trade',
        name: 'Trade',
        component: Trade
    },{
        path: '/exchange',
        name: 'Exchange',
        component: Exchange
    }
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

export default router
