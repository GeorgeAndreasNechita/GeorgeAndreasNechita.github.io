<script setup>
import {  RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'

</script>

<template>
  <div id="parent-container">
    <Navbar />
     <div style="margin:0px 0"><RouterView /></div>
  </div>
</template>

<style scoped>

</style>

