import { Module } from 'vuex';
import { getters } from './getters';
import { actions } from './actions';
import { mutations } from './mutations';
import { AuthorState } from './types';
import { RootState } from '../../types';

/**
 * author state
 */
export const state: AuthorState = {
  authorList: [],
  loading: false,
  successStatus: false,
  errorStatus: false,
};

const namespaced: boolean = true;

const AuthorModule: Module<AuthorState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations,
};

export default AuthorModule;
