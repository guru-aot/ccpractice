import { shallowMount, createLocalVue } from '@vue/test-utils';
import Author from '@/views/Author.vue';
import Vuex from 'vuex';
import vuetify from 'vuetify';

describe('Author.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(Vuex);
    localVue.use(vuetify);

    const store = new Vuex.Store({
      modules: {
        AuthorModule: {
          state: { authors: [] },
          getters: {
            getAuthorList: jest.fn(),
          },
        },
      },
    });
    wrapper = shallowMount(Author, {
      localVue,
      store,
    });
  });
  it('renders without crashing', () => {
    // const wrapper = shallowMount(Author);
    expect(wrapper.element).toMatchSnapshot();
  });
});
