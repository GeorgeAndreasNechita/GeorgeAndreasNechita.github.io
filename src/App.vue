<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue'

</script>

<template>
  <div id="parent-container">
    <Header />
     <div style="margin:0px 0"><RouterView /></div>
  </div>
</template>

<style scoped>

</style>

