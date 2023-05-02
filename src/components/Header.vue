<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>



<template>
  <header class="" id="header">
    <nav id="nav">
        <ul class="nav_list" id="navlist">
          <li><RouterLink class=" text-4xl font-bold underline " to="/">Home</RouterLink></li>
          <li><RouterLink class="nav_item" to="/lebenslauf">Lebenslauf</RouterLink></li>
          <li><RouterLink class="nav_item" to="/about">About</RouterLink></li>
        </ul>
    </nav>
  </header>
</template>


<style scoped>
#nav{
  margin: 0 10%;
}
#navlist{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}
.nav_item{
  text-decoration: none;

  background-color: transparent;
  border: none;
  margin: 0;
  padding: 0;

  color: red;
  font-weight: 600;
  font-size: 21px;
  text-align: center;
}
</style>
