<template>
  <v-layout row wrap>
    <v-container grid-list-xl>

      <!-- logo -->
      <custom-logo></custom-logo>

      <v-card>
        <!-- Home page introduction -->
        <v-card-actions class="justify-center" style="text-align:center;">
          <p>Have an item you want to throw out? Not sure which bin it goes in? Find out in 1, 2, 3!</p>
        </v-card-actions>
      </v-card>

      <!-- Steps -->
      <v-card>
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

        <div style="padding: 25px;">
          <v-btn to="scan" class="ma-2" color="primary" block>
            <!--<v-icon class="material-icons">
              mdi-camera
            </v-icon>
            -->
            <v-icon dark left>mdi-camera</v-icon>
            Scan Object
          </v-btn>
        </div>
      </v-card>
    </v-container>
    <!--<v-btn @click.native="process" block secondary dark><a href="pages/scan.vue">Scan Object</a></v-btn>-->
    <!--<v-icon left></v-icon> Analyze</v-btn>-->
    <!--<h4 class="red--text">You should: {{resultText}} it!</h4>-->
  </v-layout>

</template>

<script>
    import CustomLogo from "./CustomLogo";
    export default {
        name: "MainMenu",
      components: {CustomLogo}
    }
</script>

<style scoped>

</style>
