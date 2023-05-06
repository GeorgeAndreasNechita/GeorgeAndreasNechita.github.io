<script setup>

</script>

<template>
  <main>
    <section id="mountain">
      <div class="header">
        <div class="info">
          <img src="@/assets/try1.png" id="me-photo" alt="">
          <div class="description-text">
            <h1>George Andreas Nechita - Full Stack Web Entwickler</h1>
            <h2>Ich bin ein autodidaktischer Web Entwickler mit fast 2 Jahren Berufserfahrung.<br> Ich wohne
              seit 4 Jahren in Stuttgart.
              Derzeit auf der Suche nach einem neuen Job nach einer Pause von 1 Jahr, um einige persönliche
              Angelegenheiten zu regeln.</h2>
          </div>
        </div>
      </div>
    </section>
    <!-- <img class="planguage" src="@/assets/languages.png" alt=""> -->
  </main>
</template>

<style scoped>
@import '../css/mountain-animation.css';

#me-photo {
  margin: auto;
  margin-bottom: 20px;
  width: 250px;
  border-radius: 950px;
}

#main {
  background: rgb(29, 29, 29);
  z-index: -99;
  height: 100vh;
}

#title {
  margin-top: 2%;
}

.info {
  width: 100%;
  padding: 0% 22% 0 22%;
}

.description-text {
  border-radius: 200px;
  padding: 30px;
  background-color: rgba(0, 0, 0, 0.6);
}

h1,
h2 {
  display: grid;
  align-items: center;
  text-align: center;
  font-size: 27px;
  letter-spacing: 0px;
  line-height: 35px;
  text-decoration: none;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

h1 {
  color: #ffffff;
  font-weight: 800;
  font-family: 'Lato', sans-serif;
  font-size: 30px;
  line-height: 58px;
}
h2{
  color:powderblue;
}
</style>