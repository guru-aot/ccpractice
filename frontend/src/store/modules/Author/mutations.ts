import { MutationTree } from 'vuex';
import { AuthorState } from './types';

/**
 * mutation
 */
export const mutations: MutationTree<AuthorState> = {
  /**
   * Sets loading
   * @param {*} state
   * @param {boolean} flag - loading
   */

  SET_LOADING(state, flag: boolean) {
    state.loading = flag;
  },
  /**
   * Sets author
   * @param {*} state
   * @param payload author list
   */

  SET_AUTHORLIST(state, payload: any) {
    state.authorList = payload;
  },

  /**
   * set stae on success
   * @param {*} state
   * @param {*} payload
   */
  SET_AUTHOR_SUCCESSFULLY(state, payload: any) {
    state.successStatus = payload;
  },

  /**
   * set stae on error
   * @param {*} state
   * @param {*} payload
   */
  SET_AUTHOR_ERROR(state, payload: any) {
    state.errorStatus = payload;
  },
};
