import { GetterTree } from 'vuex';
import { KeyCloakState } from './types';
import { RootState } from '../../types';
/**
 * Getters
 */
export const getters: GetterTree<KeyCloakState, RootState> = {
  /**
   * isLoggedin authentication status
   * @param {*} state
   * @returns {boolean} - authentication status
   */
  isLoggedin(state) {
    return state.authenticated;
  },
  /**
   * keyCloakValues  - all values in keyCloak service
   * @param {*} state
   * @returns {object} keycloak auth
   */
  keyCloakValues(state) {
    return state.keycloakAuth;
  },
  /**
   * userProfile  - user profile details
   * @param {*} state
   * @returns {object} user profile details
   */
  userProfile(state) {
    return state.profile;
  },
  /**
   * userProfile  - user profile details
   * @param {*} state
   * @returns {object} user profile details
   */
  isAdmin(state) {
    return state.isAdmin;
  },
  isUser(state) {
    return state.isUser;
  },
};
