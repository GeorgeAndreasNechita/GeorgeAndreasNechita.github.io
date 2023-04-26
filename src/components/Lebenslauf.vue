<template>
  <div class="main">
    <vue-pdf-embed :source="source1" class="canvas"/>
  </div>
</template>

<script>
import VuePdfEmbed from 'vue-pdf-embed'

export default {
  components: {
    VuePdfEmbed,
  },
  data() {
    return {
      source1: 'and2.pdf',
      showAllPages: true
    }
  },
}
</script>

<style scoped>
.main{
  
}
.canvas{
  width: 100%;
  height: 90vh;
  overflow-x: none; /* enable vertical scrolling */
  overflow-y: scroll; /* enable vertical scrolling */
}
</style>