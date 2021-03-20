import { Module } from 'vuex';
import { getters } from './getters';
import { actions } from './actions';
import { mutations } from './mutations';
import { RequestState } from './types';
import { RootState } from '../../types';

/**
 * author state
 */
export const state: RequestState = {
  requestList: [],
  loading: false,
  successStatus: false,
  errorStatus: false,
};

const namespaced: boolean = true;

const RequestModule: Module<RequestState, RootState> = {
  namespaced,
  state,
  getters,
  actions,
  mutations,
};

export default RequestModule;
