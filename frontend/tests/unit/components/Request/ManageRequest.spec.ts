/**
 * Request test
 */
 import { shallowMount, createLocalVue } from '@vue/test-utils';
 import Request from '@/components/Request/Request.vue';
 import Vuex from 'vuex';
 import vuetify from 'vuetify';
 describe('component/Request/Request.vue', () => {
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
           getters: { successStatus: jest.fn(), errorStatus: jest.fn() },
           actions: {},
         },
       },
     });
     wrapper = shallowMount(Request, {
       localVue,
       store,
     });
   });
   it('renders props when passed', () => {
     expect(wrapper.element).toMatchSnapshot();
   });
 });
