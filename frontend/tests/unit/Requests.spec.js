import { shallowMount } from '@vue/test-utils'
import Requests from '@/components/Requests.vue'

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
})