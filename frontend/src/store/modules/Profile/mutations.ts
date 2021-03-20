import { MutationTree } from 'vuex';
import { ProfileState } from './types';

/**
 * mutation
 */
export const mutations: MutationTree<ProfileState> = {
  /**
   * Sets loading
   * @param {*} state
   * @param {boolean} flag - loading
   */

  SET_LOADING(state, flag: boolean) {
    state.loading = flag;
  },
  /**
   * Sets contact
   * @param {*} state
   * @param payload contact list
   */

  // TODO - change to type
  SET_USERS_PROFILE(state, payload: any) {
    state.currentUser = payload;
  },
  SET_PROFILE_SUCCESSFULLY(state, payload: any) {
    // console.log('payload', payload);
    state.successStatus = payload;
  },
  SET_PROFILE_ERROR(state, payload: any) {
    // console.log('payload', payload);
    state.errorStatus = payload;
  },
};
