import { mount } from '@vue/test-utils'
import Alert from '@/components/Alert.vue'
// import HelloWorld from '@/components/HelloWorld.vue';

describe('Alert Component unit tests: ', () => {
    test('is a Vue instance', () => {
        const wrapper = mount(Alert, {
            propsData: {
                message: 'Unit test Alert Component'
            }
        })
        expect(wrapper.isVueInstance()).toBeTruthy()
    })

    test('Render message', () => {
        const msg = 'Unit test Alert Component'
        const wrapper = mount(Alert, {
            propsData: {
                message: msg
            }
        })
        expect(wrapper.html()).toContain(msg)
    })
})