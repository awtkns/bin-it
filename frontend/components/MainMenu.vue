<template>
  <v-layout row wrap>
    <v-container grid-list-xl>

      <div style="text-align: left; padding: 25px;" class="justify-center">
        <v-layout column>
          <!-- Home page introduction -->
          <v-card-actions>
            <h2>Have an item you want to throw out? Not sure which bin it goes in? Find out in 1, 2, 3!</h2>
          </v-card-actions>
        </v-layout>

        <v-layout column>
          <!-- Home page introduction -->
          <v-card-actions>
            <p>Don’t worry, find out in 1, 2, 3! Scroll down to learn more.</p>
          </v-card-actions>
        </v-layout>
      </div>

      <v-card-actions class="justify-center"><Mountains01></Mountains01></v-card-actions>
      <div class="scan-btn-container">
        <v-btn to="scan" color="primary" block style="padding: 25px;">
          <v-icon dark left>mdi-camera</v-icon>
          Scan Object
        </v-btn>
      </div>

      <!-- Steps -->
      <v-layout column>
        <v-card-actions class="justify-center">
          <h2>3 easy steps</h2>
        </v-card-actions>
        <v-card-actions class="justify-center">
          <p>1. Hold your item</p>
        </v-card-actions>
        <v-card-actions class="justify-center">
          <p>2. Wait for the scan</p>
        </v-card-actions>
        <v-card-actions class="justify-center">
          <p>3. Know where to throw</p>
        </v-card-actions>
        <v-card-actions class="justify-center" style="text-align:center;">
          <p>Learn about the impact your making!</p>
        </v-card-actions>
      </v-layout>
    </v-container>
    <!--<footer></footer>-->
    <!--<v-btn @click.native="process" block secondary dark><a href="pages/scan.vue">Scan Object</a></v-btn>-->
    <!--<v-icon left></v-icon> Analyze</v-btn>-->
    <!--<h4 class="red--text">You should: {{resultText}} it!</h4>-->
  </v-layout>

</template>

<script>
    import Header from "./Header";
    import Mountains01 from "./Mountains01";
    import Footer from "./Footer";
    export default {
      name: "MainMenu",
      components: {Footer, Mountains01, Header}
    }
</script>

<style scoped>

  .scan-btn-container {
    padding: 25px;
  }

</style>
