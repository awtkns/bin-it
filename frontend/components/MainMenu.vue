<template>
  <v-layout row wrap>
    <v-container grid-list-xl>

      <v-layout column>
        <!-- Home page introduction -->
        <v-card-actions class="justify-center" style="text-align:center;">
          <p>Have an item you want to throw out? Not sure which bin it goes in? Find out in 1, 2, 3!</p>
        </v-card-actions>
      </v-layout>

      <!-- Steps -->
      <v-layout column>
        <v-card-actions class="justify-center">
          <h3>1. Hold your item</h3>
        </v-card-actions>
        <v-card-actions class="justify-center">
          <h3>2. Wait for the scan</h3>
        </v-card-actions>
        <v-card-actions class="justify-center">
          <h3>3. Know where to throw</h3>
        </v-card-actions>
        <v-card-actions class="justify-center" style="text-align:center;">
          <p>Learn about the impact your making!</p>
        </v-card-actions>

        <div class="scan-btn-container">
          <v-btn to="scan" color="primary" block>
            <v-icon dark left>mdi-camera</v-icon>
            Scan Object
          </v-btn>
        </div>
      </v-layout>
    </v-container>
    <!--<v-btn @click.native="process" block secondary dark><a href="pages/scan.vue">Scan Object</a></v-btn>-->
    <!--<v-icon left></v-icon> Analyze</v-btn>-->
    <!--<h4 class="red--text">You should: {{resultText}} it!</h4>-->
  </v-layout>

</template>

<script>
    import Header from "./Header";
    export default {
      name: "MainMenu",
      components: {Header}
    }
</script>

<style scoped>

  .scan-btn-container {
    padding: 25px;
  }

</style>
