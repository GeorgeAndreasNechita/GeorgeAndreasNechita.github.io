<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
        <ul id="nav_ul">
          <li><RouterLink class="nav_item" to="/">Home</RouterLink></li>
          <li><RouterLink class="nav_item" to="/lebenslauf">Lebenslauf</RouterLink></li>
          <li><RouterLink class="nav_item" to="/project1">Project1</RouterLink></li>
        </ul>
</template>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

#nav_ul{
  display: grid;
  padding-left:40%;
  padding-right:20%;
  grid-template-columns: 1fr 1fr 1fr;
  align-items: center;
  /* background-color: #1f1f1f; */
  background-color: #181818;

  height: 60px;

    border-bottom: 1px solid #1a1a1a;
    backdrop-filter: blur(8px);
    box-shadow: 0 4px 4px rgba(0,0,0,0.3);
    z-index: 99999999999;
}
li {
  text-align: center;
}
.nav_item{
  font-family: 'Poppins', sans-serif;
  color: white;
  font-weight: 600;
  font-size: 19px;
  text-align: center;
}
.router-link-active, .nav_item:hover{
  text-decoration: underline;  
  text-decoration-color: red;  
  text-decoration-thickness: 3px;
  text-underline-offset: 8px;
}

</style>
