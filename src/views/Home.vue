

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
            <h2>Ich bin ein autodidaktischer Web Entwickler mit fast 2 Jahren Berufserfahrung.<br> Seit 4 Jahren lebe ich in Stuttgart.
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
  margin-bottom: 60px;
  width: 250px;
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
z-index: 999;
animation: fadeIn 1.5s ease-out;
}

.description-text {
border-radius: 200px;
padding: 50px;
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
font-size: 30px;
line-height: 58px;
animation: pulse 7s ease-in-out infinite alternate;
}

h2{
color:powderblue;
font-weight: 600;
font-size: 24px;
letter-spacing: 1px;
margin-top: 15px;
animation: slideInRight 1.5s ease-out;
}

h1 {
  display: grid;
  align-items: center;
  text-align: center;
  font-size: 27px;
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


</style>