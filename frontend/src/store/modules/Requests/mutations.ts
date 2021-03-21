import { MutationTree } from 'vuex';
import { RequestState } from './types';

/**
 * mutation
 */
export const mutations: MutationTree<RequestState> = {
  /**
   * Sets loading
   * @param {*} state
   * @param {boolean} flag - loading
   */

  SET_LOADING(state, flag: boolean) {
    state.loading = flag;
  },

  /**
   * Sets requestHeader
   * @param {*} state
   * @param payload header list
   */

   SET_REQUESTHEADER(state, payload: any) {
    state.requestHeaders = payload;
  },

  /**
   * Sets request
   * @param {*} state
   * @param payload request list
   */

  SET_REQUESTLIST(state, payload: any) {
    state.requestList = payload;
  },

  /**
   * set stae on success
   * @param {*} state
   * @param {*} payload
   */
  SET_REQUEST_SUCCESSFULLY(state, payload: any) {
    state.successStatus = payload;
  },

  /**
   * set stae on error
   * @param {*} state
   * @param {*} payload
   */
   SET_REQUEST_ERROR(state, payload: any) {
    state.errorStatus = payload;
  },
};
