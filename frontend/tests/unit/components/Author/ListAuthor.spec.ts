/**
 * ListAuthor test
 */

import { shallowMount, createLocalVue } from '@vue/test-utils';
import ListAuthor from '@/components/Author/ListAuthor.vue';

import Vuex from 'vuex';
import vuetify from 'vuetify';

describe('component/Author/ListAuthor.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(Vuex);
    localVue.use(vuetify);
    const store = new Vuex.Store({
      modules: {
        AuthorModule: {
          namespaced: true,
          state: {},
          getters: {
            getAuthorList: jest.fn(() => [
              {
                created: '2019-10-10T05:59:56.999852',
                first_name: 'author1 ',
                id: 1,
                last_name: 'last',
                middle_name: '',
                modified: '2019-10-10T05:59:56.999881',
              },
            ]),
            successStatus: jest.fn(),
            errorStatus: jest.fn(),
          },
          actions: {},
        },
      },
    });
    wrapper = shallowMount(ListAuthor, {
      localVue,
      store,
    });
  });
  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
