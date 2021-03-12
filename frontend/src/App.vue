<template>
  <div id="app">
    <router-view/>
    <h1>HELLO</h1>
     <h2 style="margin-left: 50px;">User: {{keycloak.tokenParsed.preferred_username}}</h2>
  </div>
</template>

<script>
/* eslint-disable */
import Home from "./components/Home.vue";
import axios from "axios";

export default {
  name: "App",
  props: ["keycloak"],
  components: {
    Home
  },
  data() {
    return {
      user: this.user,
    };
  },
  mounted() {
    axios
      .get("http://localhost:5000/user", {
        headers: {
          Authorization: "Bearer " + this.keycloak.token          
        }
      })
      .then(response => (this.user = response));
  }
};
</script>
