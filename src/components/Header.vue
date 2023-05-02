<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header class="" id="header">
    <nav id="nav">
        <ul class="nav_list" id="navlist">
          <li><RouterLink class="nav_item" to="/">Home</RouterLink></li>
          <li><RouterLink class="nav_item" to="/lebenslauf">Lebenslauf</RouterLink></li>
          <li><RouterLink class="nav_item" to="/project1">Project1</RouterLink></li>
        </ul>
    </nav>
  </header>
</template>


<style scoped>
#header{
  display: grid;
  align-items: center;
  background-color: #1f1f1f;
  height: 80px;
}
#nav{
  margin: 0 10%;
}
#navlist{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}
li {
  text-align: center;
}
.nav_item{
  color: white;
  font-weight: 600;
  font-size: 21px;
  text-align: center;
}
.router-link-active{
  text-decoration: underline;  
  text-decoration-color: red;  
  text-decoration-thickness: 3px;
  text-underline-offset: 8px;
}

</style>
