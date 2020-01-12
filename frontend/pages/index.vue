<template>
  <v-layout column>
    <v-layout row wrap align-center>
      <CustomLogo></CustomLogo>
    </v-layout>
    <MainMenu/>
  </v-layout>
</template>

<script>
import Header from '../components/Header';
import CustomLogo from "../components/CustomLogo";
import MainMenu from "../components/MainMenu";

export default {
  components: {
    Header,
    CustomLogo,
    MainMenu
  }
}
</script>
