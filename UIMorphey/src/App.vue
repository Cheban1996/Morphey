<template>
    <div id="app">
        <div id="nav">
            <router-link to="/">Home</router-link>
            <router-link to="/trade">Trade</router-link>
            <router-link to="/exchange">Exchange</router-link>
        </div>
        <router-view class="view"/>
    </div>
</template>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        /*text-align: center;*/
        color: #2c3e50;
        margin-left: 30px;
        margin-right: 30px;
    }

    #nav {
        margin-top: 15px;
        margin-bottom: 15px;
    }

    #nav a {
        font-weight: bold;
        color: #2c3e50;
        padding-right: 15px;
    }

    #nav a.router-link-exact-active {
        color: #42b983;
    }
</style>
