import { ActionTree } from 'vuex';
import { RequestState, RequestModel } from './types';
import { RootState } from '../../types';
import { BASE_URL,  REQUESTURL } from '@/config/urlList';
import axios from '@/lib/axios';

/**
 * author Actions
 *
 */
export const actions: ActionTree<RequestState, RootState> = {
  /**
   * @param  {} {commit, dispatch}
   * @param  {} author  list
   */
  addRequest({ commit, dispatch }, data) {
    commit('SET_LOADING', true);
    axios
      .post(BASE_URL + REQUESTURL, data)
      .then(_ => {
        commit('SET_LOADING', false);
        commit('SET_REQUEST_SUCCESSFULLY', true);
        commit('SET_REQUEST_ERROR', false);
        dispatch('loadRequest');
      })
      .catch(() => {
        commit('SET_CONTACT_SUCCESSFULLY', false);
        commit('SET_CONTACT_ERROR', true);
      });
  },

  /**
   * load request from server and set to store
   * @param {*} { commit }
   */
  loadRequest({ commit }) {
    commit('SET_LOADING', true);
    axios
      .get(BASE_URL + REQUESTURL)
      .then((r: any) => r.data)
      .then((data: RequestModel[]) => {  
        commit('SET_REQUESTLIST', data);
        commit('SET_LOADING', false);
      });
  },
  /**
   * clear message
   * @param {*} { commit }
   */
  clearStatus({ commit }) {
    commit('SET_REQUEST_SUCCESSFULLY', false);
    commit('SET_REQUEST_ERROR', false);
  },
};
