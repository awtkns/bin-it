<template>
  <v-card>
    <v-row>Stats</v-row>
<!--    <v-row v-for="s in statslist">{{ s }}</v-row>-->
  </v-card>
</template>

<script>
  import axios from 'axios';
  export default {
      name: "Stats",
      data() {
        return {
          statslist: []
        }
      },
      async created() {
        try {
          const res = await axios.get('http://localhost:5000/labellist')
          console.log(res)
          this.statslist = res.data.labels
        } catch (e) {
          console.log(e)
        }
      }
  }
</script>

<style scoped>

</style>
