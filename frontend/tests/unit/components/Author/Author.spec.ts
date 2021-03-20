/**
 * AddAuthor test
 */
import { shallowMount, createLocalVue } from '@vue/test-utils';
import AddAuthor from '@/components/Author/AddAuthor.vue';

import Vuex from 'vuex';
import vuetify from 'vuetify';

describe('component/Author/AddAuthor.vue', () => {
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
          getters: { successStatus: jest.fn(), errorStatus: jest.fn() },
          actions: {},
        },
      },
    });
    wrapper = shallowMount(AddAuthor, {
      localVue,
      store,
    });
  });
  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});
