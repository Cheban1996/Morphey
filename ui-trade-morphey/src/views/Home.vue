<template>
  <div class="home">
    <v-select placeholder="Symbols" :options="symbols" v-model="selectedSymbol"></v-select>
  </div>
</template>

<script>
import api from "../apiMorphey";

export default {
  name: "Home",
  data: function() {
    return {
      symbols: [],
      selectedSymbol: null
    };
  },
  async mounted() {
    this.symbols = await api.getSymbols();
  }
};
</script>
<style scoped lang="less">
div .v-select {
  margin-right: 5px;
  width: 350px;
  display: inline-block;
}
</style>