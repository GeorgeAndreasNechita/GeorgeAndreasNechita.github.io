<template>
  <VuePDF :pdf="pdf" :page="1" />
</template>

<script>
import {usePDF, VuePDF} from '@tato30/vue-pdf'

export default {
  components: {
    VuePDF
  },
  setup(){
    const { pdf, pages, info } = usePDF("./and.pdf")

    console.log(`Document has ${pages} pages`)
    console.log(`Document info: ${info}`)

    return {
      pdf
    }
  }
}
</script>