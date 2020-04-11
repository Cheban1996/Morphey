<template>
    <div class="exchange">
        <div class="form">
            <input type="text" name="api_key" placeholder="Api Key" v-model="api_key"><br/>
            <input type="text" placeholder="Api Password" v-model="api_password"><br/>
            <button>Save</button>
            <p>{{api_key}}</p>
            <p>{{api_password}}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Exchange",
        data: function () {
            return {
                api_key: "",
                api_password: ""
            }
        },
        methods: {
            save() {

            }
        }
    }
</script>

<style scoped lang="less">
    .form input {
        margin-bottom: 10px;
        width: 550px;
    }
</style>