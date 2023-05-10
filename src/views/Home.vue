

<script setup>

</script>

<template>
  <main>
    <section id="mountain">
      <div class="header">
        <div class="info">
          <img src="@/assets/try1.png" id="me-photo" alt="">
          <div class="description-text-div">
            <h1>George Andreas Nechita</h1>
            <h1>Full Stack Web Entwickler</h1>
            <h2>Ich bin ein autodidaktischer Web Entwickler mit fast 2 Jahren Berufserfahrung.</h2>
            <h2>Derzeit auf der Suche nach einem neuen Job nach einer Pause von 1 Jahr, um einige persönliche
              Angelegenheiten zu regeln.</h2>
            <h2>Ich wohne in Stuttgart seit April 2019</h2>
          </div>
        </div>
      </div>
    </section>
    <!-- <img class="planguage" src="@/assets/languages.png" alt=""> -->
  </main>
</template>

<style scoped>
@import '../css/mountain-animation.css';


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
  padding: 0% 2% 0 2%;
  z-index: 999;
  animation: fadeIn 1.5s ease-out;
}


#me-photo {
  margin: auto;
  height: auto;
  width: 100%;
  max-width: 230px;
  border-radius: 950px;
  border: 5px solid #fff;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
  filter: brightness(80%);
  transition: transform 0.2s ease-in-out, filter 0.2s ease-in-out;
  animation: fadeInImage 1.5s ease-out;
}

#me-photo:hover {
  transform: scale(1.2);
  filter: brightness(85%);
}

.description-text-div {
  border-radius: 80px;
  padding: 30px 1px 0px 1px;
  /* background-color: rgba(0, 0, 0, 0.6); */
}

h1,
h2 {

  text-align: center;

  line-height: 35px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

h1 {
  color: #ffffff;
  font-weight: 800;
  font-size: 1.4rem;
  line-height: 58px;
  animation: pulse 7s ease-in-out infinite alternate;
}

h2 {
  color: powderblue;
  font-weight: 600;
  font-size: 1rem;
  letter-spacing: 1px;
  margin-top: 15px;
  animation: slideInRight 1.5s ease-out;
}

h1 {
  display: grid;
  align-items: center;
  text-align: center;
  letter-spacing: 0px;
  line-height: 35px;
  text-decoration: none;
  font-weight: 800;
  font-family: 'Lato', sans-serif;
  color: #ffffff;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  animation: fadein 1.5s ease-out;
}

@keyframes fadein {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInRight {
  from {
    transform: translateX(100%);
    opacity: 0;
  }

  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }

  100% {
    transform: scale(1.05);
  }
}

@keyframes fadeInImage {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}


@media only screen and (min-device-width: 320px) and (orientation: landscape) {
  #me-photo {
    margin-top: 3vmax;
  }

  .header {
    height: auto;
    padding-bottom: 10vmax;
  }
}

@media only screen and (max-device-height: 750px) {
  #me-photo {
    width: 200px;
    max-width: 160px;
  }

  h1 {
    font-size: 1.4rem;
    line-height: 2rem;
  }

  h2 {
    font-size: 0.8rem;
    line-height: 2rem;
  }
}

@media only screen and (min-device-width: 1080px) {
  #me-photo {
    width: 70vmax;
  }

  h1 {
    font-size: 1.6rem;
    line-height: 2.5rem;
  }

  h2 {
    line-height: 2rem;
    font-size: 1.3rem;
  }
}
@media screen and (min-width: 768px) and (max-width: 1024px) {
  #me-photo {
    width: 330px;
    max-width: 1000px;
  }

  h1 {
    font-size: 2.2rem;
    line-height: 3.6rem;
  }

  h2 {
    font-size: 1.6rem;
    line-height: 3.2rem;
  }
}

/* Tablets - Landscape */
@media screen and (min-width: 1025px) and (max-width: 1280px) {
  /* CSS rules for tablets in landscape mode */
}
</style>