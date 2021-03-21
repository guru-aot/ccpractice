import { ActionTree } from 'vuex';
import { RequestState, RequestModel } from './types';
import { RootState } from '../../types';
import { BASE_URL,  REQUESTURL, ADDREQUESTURL, EDITREQUESTURL } from '@/config/urlList';
import axios from '@/lib/axios';

/**
 * request Actions
 *
 */
export const actions: ActionTree<RequestState, RootState> = {
  /**
   * @param  {} {commit, dispatch}
   * @param  {} request  list
   */
  addRequest({ commit, dispatch }, data) {
    commit('SET_LOADING', true);
    axios
      .post(BASE_URL + ADDREQUESTURL, data)
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

  updateRequest({ commit, dispatch }, data) {
    commit('SET_LOADING', true);
    const editRequestURL = EDITREQUESTURL.replace('<requestid>', data.requestid);
    axios
      .post(BASE_URL + editRequestURL, data)
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
        commit('SET_REQUESTHEADER', [
          {
            text: 'ID',
            align: 'start',
            sortable: false,
            value: 'requestid',
          },
          { text: 'Name', value: 'name' },
          { text: 'Description', value: 'description' },
          { text: 'Status', value: 'status' },
          { text: 'Created By', value: 'createdby' },
        ]);
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
