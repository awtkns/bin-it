<template>
  <v-card color="white" class="mx-auto" max-width="344" elevation="2">
    <div style="color:black;">
      <v-card-text >
        <h1>
          <v-icon color="black" left>mdi-recycle</v-icon>
          Recycle it!
        </h1>
        <br>
        <p>
          Plastic Bottles are recyclable in blue bins.
        </p>
      </v-card-text>

      <v-card-text>
        <h2>How to Reuse it?</h2>
        <br>
        <p>
          Plastic Bottles are recyclable in blue bins.
        </p>
      </v-card-text>

      <v-card-text>
        <h2>Whats the Impact?</h2>
        <br>
        <p>
          In addition to reducing greenhouse gas emissions, recycling plastic water bottles also helps to decrease the amount of pollution in the air and water sources.
        </p>
      </v-card-text>

      <v-card-actions>
        <v-btn to="/" color="primary" block>
          Back to home
        </v-btn>
      </v-card-actions>

        <!--
      <v-card-actions>

      </v-card-actions>
      -->
    </div>
  </v-card>
  <!--
  <v-overlay :absolute="absolute" :value="overlay">

  </v-overlay>
  -->
</template>

<script>
    export default {
        name: "InfoCard",
        data: () => ({
          absolute: true,
          overlay: false,
        }),
    }
</script>

<style scoped>

</style>
