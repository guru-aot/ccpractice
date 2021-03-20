import { GetterTree } from 'vuex';
import { AuthorState } from './types';
import { RootState } from '../../types';

/**
 * Getters
 */
export const getters: GetterTree<AuthorState, RootState> = {
  /**
   * author
   * @param {*} state
   * @returns  {object} author
   */

  getAuthorList(state) {
    return state.authorList;
  },
  successStatus(state) {
    return state.successStatus;
  },
  errorStatus(state) {
    return state.errorStatus;
  },
};
