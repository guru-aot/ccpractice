import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';
import { RootState } from './types';
import AuthorModule from './modules/Author';
import KeyCloakModule from './modules/KeyCloak/';
import ProfileModule from './modules/Profile';
import RequestModule from './modules/Requests';

Vue.use(Vuex);

/**
 * Main store with modules
 */
const store: StoreOptions<RootState> = {
  modules: {
    AuthorModule,
    KeyCloakModule,
    ProfileModule,
    RequestModule,
  },
  strict: true,
};

export default new Vuex.Store<RootState>(store);
