<template>
     <!-- <b-modal ref="addRequestModal"
            id="request-modal"
            title="Add a new request"
            hide-footer> -->
      <b-form @submit.prevent="onSubmit" @reset.prevent="onReset" class="w-100">
      <b-form-group id="form-name-group"
                    label="Name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addRequestForm.name"
                        required
                        placeholder="Enter Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-description-group"
                      label="Description:"
                      label-for="form-description-input">
            <b-form-input id="form-description-input"
                          type="text"
                          v-model="addRequestForm.description"
                          required
                          placeholder="Enter description">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-status-group"
                      label="Status:"
                      label-for="form-status-input">
            <b-form-input id="form-status-input"
                          type="text"
                          v-model="addRequestForm.status"
                          required
                          placeholder="Enter status">
            </b-form-input>
          </b-form-group>
           <b-form-group id="form-createdby-group"
                      label="Created By:"
                      label-for="form-createdby-input">
            <b-form-input id="form-createdby-input"
                          type="text"
                          v-model="addRequestForm.createdby"
                          required
                          placeholder="Enter Created By">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-updated-group">
          <b-form-checkbox-group v-model="addRequestForm.updated" id="form-checks">
            <b-form-checkbox value="true">Updated?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    <!-- </b-modal> -->
</template>
<script>
export default {
  name: 'AddRequest',
  data() {
    return {
      name: '',
      description: '',
      status: '',
      createdby: '',
      updated: false,
    };
  },
  methods: {
    initForm() {
      this.name = '';
      this.description = '';
      this.status = '';
      this.createdby = '';
      this.updated = false;
    },
    onSubmit() {
      if (!this.text) {
        // alert('Please add a Request');
        return;
      }
      const newRequest = {
        name: this.name,
        description: this.description,
        status: this.status,
        createdby: this.createdby,
        updated: this.updated,
      };
      this.$emit('add-request', newRequest);
      this.initForm();
    },
    onReset() {
      this.initForm();
    },
  },
};

</script>
