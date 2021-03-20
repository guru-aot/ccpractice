import { shallowMount } from '@vue/test-utils'
import Requests from '@/components/Requests.vue'

jest.mock("axios", () => ({
    get: () => Promise.resolve({ data: [{ val: 1 }] })
  }));

describe('Test Requests Component: ', () => {
    let wrapper
  
    beforeEach(() => {
        wrapper = shallowMount(Requests, {
            methods: { getRequests: ()=> {}}
        })
    })
    it('reders', () => {
        expect(wrapper.exists()).toBe(true)
    })

    it('does h1 exist', () => {
        expect(wrapper.find('h1').text()).toBe('Requests')
    })

    it('fetches async on created', () => { 
        wrapper.vm.$nextTick(() => {
            expect(wrapper.vm.requests.length).toBe(1);
        })        
    })
})