<template>
  <div class="main">
    <div class="button-parent">
      <button class="button-64 mt-8" @click="changeDocument">
        <span class="text">{{ buttonText }}</span>
      </button>
    </div>
    <div class="button-parent">
      <button class="button-64 mt-8 mb-6">
        <span class="text">
          <a href="George Andreas Nechita - Lebenslauf.pdf" download>Lebenslauf Herunterladen</a>
        </span>
      </button>
    </div>
  </div>

  <vue-pdf-embed :source="source" class="canvas" />
</template>

<script>
import VuePdfEmbed from 'vue-pdf-embed'

export default {
  components: {
    VuePdfEmbed,
  },
  data() {
    return {
      buttonText: 'Arbeitszeugnis von 91Interactive',
      source: 'George Andreas Nechita - Lebenslauf.pdf',
      showAllPages: true
    }
  },
  methods: {
    changeDocument() {
      if (this.buttonText == 'Arbeitszeugnis von 91Interactive') {
        this.source = 'George Andreas Nechita - Arbeitszeugnis.pdf'
        this.buttonText = 'Lebenslauf'
        return
      }
      this.source = 'George Andreas Nechita - Lebenslauf.pdf'
      this.buttonText = 'Arbeitszeugnis von 91Interactive'
      return
    }
  }
}
</script>

<style scoped>
.canvas {
  width: 100%;
  height: 90vh;
  overflow-x: none;
  /* enable vertical scrolling */
  overflow-y: scroll;
  /* enable vertical scrolling */
}

.button-parent {
  display: grid;
}

/* CSS */
.button-64 {
  display: grid;
  justify-self: center;
  height: 3rem;
  align-items: center;
  background-image: linear-gradient(144deg, #AF40FF, #5B42F3 50%, #00DDEB);
  border: 0;
  border-radius: 8px;
  box-shadow: rgba(151, 65, 252, 0.2) 0 15px 30px -5px;
  box-sizing: border-box;
  color: #FFFFFF;
  display: flex;
  font-family: Phantomsans, sans-serif;
  font-size: 1rem;
  justify-content: center;
  line-height: 1em;
  max-width: 100%;
  min-width: 140px;
  padding: 3px;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: nowrap;
  cursor: pointer;
}

.button-64:active,
.button-64:hover {
  outline: 0;
}

.button-64 span {
  background-color: rgb(5, 6, 45);
  padding: 16px 24px;
  border-radius: 6px;
  width: 100%;
  height: 100%;
  transition: 300ms;
}

.button-64:hover span {
  background: none;
}

@media (min-width: 768px) {
  .button-64 {
    display: grid;
    font-size: 1rem;
    min-width: 196px;
  }
}
</style>