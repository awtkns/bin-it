<template>
  <v-layout>
    <Header></Header>
    <Capture></Capture>
  </v-layout>
</template>

<script>
  import Header from "../components/Header";
  import Capture from "../components/Capture";
  export default {
    name: "scan",
    components: {Header, Capture}
  }
</script>

<style scoped>

</style>
