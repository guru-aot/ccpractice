import { Module } from 'vuex';
import { getters } from './getters';
import { actions } from './actions';
import { mutations } from './mutations';
import { KeyCloakState } from './types';
import { RootState } from '../../types';

/**
 * keycloak state
 */
export const state: KeyCloakState = {
  authenticated: false,
  keycloakAuth: {},
  token: '',
  profile: [],
  isAdmin: false,
  isUser: false,
};

//  namespaced module
const namespaced: boolean = true;

const KeyCloakModule: Module<KeyCloakState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations,
};

export default KeyCloakModule;
