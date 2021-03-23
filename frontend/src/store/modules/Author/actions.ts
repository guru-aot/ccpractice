import { ActionTree } from 'vuex';
import { AuthorState, AuthorModel } from './types';
import { RootState } from '../../types';
import { BASE_URL, AUTHORURL } from '@/config/urlList';
import axios from '@/lib/axios';

/**
 * author Actions
 *
 */
export const actions: ActionTree<AuthorState, RootState> = {
  /**
   * @param  {} {commit, dispatch}
   * @param  {} author  list
   */
  addAuthor({ commit, dispatch }, data) {
    commit('SET_LOADING', true);
    axios
      .post(BASE_URL + AUTHORURL, data)
      .then(_ => {
        commit('SET_LOADING', false);
        commit('SET_AUTHOR_SUCCESSFULLY', true);
        commit('SET_AUTHOR_ERROR', false);
        dispatch('loadAuthor');
      })
      .catch(() => {
        commit('SET_CONTACT_SUCCESSFULLY', false);
        commit('SET_CONTACT_ERROR', true);
      });
  },

  /**
   * load author from server and set to store
   * @param {*} { commit }
   */
  loadAuthor({ commit }) {
    commit('SET_LOADING', true);
    axios
      .get(BASE_URL + AUTHORURL)
      .then((r: any) => r.data)
      .then((data: AuthorModel[]) => {
        commit('SET_AUTHORLIST', data);
        commit('SET_LOADING', false);
      });
  },
  /**
   * clear message
   * @param {*} { commit }
   */
  clearStatus({ commit }) {
    commit('SET_AUTHOR_SUCCESSFULLY', false);
    commit('SET_AUTHOR_ERROR', false);
  },
};
