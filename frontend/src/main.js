import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import VueLogger from 'vuejs-logger';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';

Vue.use(BootstrapVue);
Vue.use(VueLogger);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
