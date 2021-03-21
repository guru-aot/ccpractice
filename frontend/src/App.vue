<template>
  <div id="app">
    <Navigation/>
    <router-view/>
  </div>
</template>

<script>
import Home from "./components/Home.vue";
import Navigation from "./components/Navigation.vue";


export default {
  name: "App",
  props: ["keycloak"],
  components: {
    Home,
    Navigation
  },
  // data() {
    
  // },
  mounted() {
  
  }
};
</script>
