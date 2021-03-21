import { GetterTree } from 'vuex';
import { RequestState } from './types';
import { RootState } from '../../types';

/**
 * Getters
 */
export const getters: GetterTree<RequestState, RootState> = {
  /**
   * author
   * @param {*} state
   * @returns  {object} author
   */
  getRequestHeaders(state) {
    return state.requestHeaders;
  },
  getRequestList(state) {
    return state.requestList;
  },
  successStatus(state) {
    return state.successStatus;
  },
  errorStatus(state) {
    return state.errorStatus;
  },
};
