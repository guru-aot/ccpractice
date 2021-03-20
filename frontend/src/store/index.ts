import Vue from 'vue';
import Vuex, { StoreOptions } from 'vuex';
import { RootState } from './types';
import AuthorModule from './modules/Author';
import KeyCloakModule from './modules/KeyCloak/';
import ProfileModule from './modules/Profile';

Vue.use(Vuex);

/**
 * Main store with modules
 */
const store: StoreOptions<RootState> = {
  modules: {
    AuthorModule,
    KeyCloakModule,
    ProfileModule,
  },
  strict: true,
};

export default new Vuex.Store<RootState>(store);
