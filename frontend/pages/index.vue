<template>
  <MainMenu/>
</template>

<script>
import Logo from '~/components/Logo.vue'
import VuetifyLogo from '~/components/VuetifyLogo.vue'
import Capture from "../components/Capture";
import MainMenu from "../components/MainMenu";

export default {
  components: {
    MainMenu,
    Capture,
    Logo,
    VuetifyLogo
  }
}
</script>
