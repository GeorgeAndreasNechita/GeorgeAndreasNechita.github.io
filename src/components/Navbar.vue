<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <ul id="nav_ul">
    <li>
      <RouterLink class="nav_item" to="/">Startseite</RouterLink>
    </li>
    <li>
      <RouterLink class="nav_item" to="/lebenslauf">Lebenslauf</RouterLink>
    </li>
    <li>
      <RouterLink class="nav_item" to="/arbeitszeugnis">( In Bearbeitung )</RouterLink>
    </li>
    <!-- <li><RouterLink class="nav_item" to="/">huehueheu</RouterLink></li> -->
  </ul>
</template>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

#nav_ul {
  display: grid;
  grid-template-columns: auto auto auto auto;
  grid-template-columns: auto auto auto;
  align-items: center;
  /* background-color: #1f1f1f; */
  background-color: #181818;

  height: 60px;

  border-bottom: 1px solid #1a1a1a;
  backdrop-filter: blur(8px);
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.3);
  z-index: 99999999999;
}

li {
  text-align: center;
}

.nav_item {
  font-family: 'Poppins', sans-serif;
  color: white;
  font-weight: 600;
  font-size: 1rem;
  text-align: center;
}

.router-link-active,
.nav_item:hover {
  text-decoration: underline;
  text-decoration-color: red;
  text-decoration-thickness: 5px;
  text-underline-offset: 8px;
  transition: text-decoration-color 0.3s ease-in-out;
}

@media screen and (min-width: 768px) and (max-width: 1024px) {
  .nav_item {
  font-size: 1.6rem;
}
}

@media only screen and (min-width: 1024px) {
  #nav_ul {
    padding: 0 25%;
  }

  .nav_item {
    font-size: 1.2rem;
  }
}</style>
