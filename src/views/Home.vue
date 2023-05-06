<script setup>

</script>

<template>
  <main id="main">

    <section id="about-me">
      <div id="left-hero-side"><img id="me-img-circle" src="@/assets/me2-modified.png" alt=""></div>
      <div id="right-hero-side">
        <div id="title">George Andreas Nechita - Full Stack Web Developer</div>
        <div id="description">Autodidaktischer Webentwickler mit fast 2 Jahren Berufserfahrung. Ich wohne seit 4 Jahren in Stuttgart.. Derzeit suche ich nach einem Job, nachdem ich 1 Jahr lang pausiert habe, um mich um persönliche Angelegenheiten zu kümmern.</div>
        <!-- <img class="planguage" src="@/assets/languages.png" alt=""> -->
      </div>
    </section>
  </main>
</template>

<style scoped>
#about-me{
  display: grid;
  grid-template-columns: 30% 70%;
  padding: 5% 5% 5% 5%;
}
#me-img-circle{
  width: 20vmax;
}
#main{
  background: rgb(29, 29, 29);
  height: 100vh;
}
#title{
  margin-top: 2%;
}
#title,#description{
  display: grid;
  align-items: center;
  text-align: center;
  font-size: 27px;
    letter-spacing: 0px;
    color: #fff;
    font-weight: 400;
    line-height: 35px;
    text-decoration: none;
}
#description{
  margin-top: 1%;
}
#left-hero-side{
  display: grid;
  place-items: center;
}
.planguage{
  background: #fff;
  height: 8vmax;
  border-radius: 1vmax;
}
</style>