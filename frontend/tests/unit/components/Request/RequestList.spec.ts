/**
 * ListRequest test
 */
import { shallowMount, createLocalVue } from '@vue/test-utils';
import RequestList from '@/components/Request/RequestList.vue';
import Vuex from 'vuex';
import vuetify from 'vuetify';
describe('component/Request/RequestList.vue', () => {
  let wrapper: any;
  beforeEach(() => {
    const localVue = createLocalVue();
    localVue.use(Vuex);
    localVue.use(vuetify);
    const store = new Vuex.Store({
      modules: {
        RequestModule: {
          namespaced: true,
          state: {},
          getters: {
            getRequestList: jest.fn(() => [
              {
                name: 'request1 ',
                requestid: 1,
                description: 'description1',
                status: 'submitted',
                createdby: 'divya',
              },
            ]),
            successStatus: jest.fn(),
            errorStatus: jest.fn(),
          },
          actions: {},
        },
      },
    });
    wrapper = shallowMount(RequestList, {
      localVue,
      store,
    });
  });
  it('renders props when passed', () => {
    expect(wrapper.element).toMatchSnapshot();
  });
});

