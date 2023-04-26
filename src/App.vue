<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <div id="parent-container">
    <header>
      <div class="wrapper">
        <nav>
          <RouterLink to="/lebenslauf">Lebenslauf</RouterLink>
          <RouterLink to="/about">About</RouterLink>
        </nav>
      </div>
    </header>
  
    <div style="margin:0px 0"><RouterView /></div>
  </div>
</template>

<style scoped>
#parent-container{
  display: grid;
  grid-template-columns: 20% 80%;
}
</style>

