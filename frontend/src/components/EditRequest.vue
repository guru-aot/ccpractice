<template>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-name-edit-group"
                    label="Name:"
                    label-for="form-name-edit-input">
          <b-form-input id="form-name-edit-input"
                        type="text"
                        v-model="name"
                        required
                        placeholder="Enter Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-description-edit-group"
                      label="Description:"
                      label-for="form-description-edit-input">
            <b-form-input id="form-description-edit-input"
                          type="text"
                          v-model="description"
                          required
                          placeholder="Enter description">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-status-edit-group"
                      label="Status:"
                      label-for="form-status-edit-input">
            <b-form-input id="form-status-edit-input"
                          type="text"
                          v-model="status"
                          required
                          placeholder="Enter status">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-createdby-edit-group"
                      label="Created By:"
                      label-for="form-createdby-edit-input">
            <b-form-input id="form-createdby-edit-input"
                          type="text"
                          v-model="createdby"
                          required
                          placeholder="Enter Created By">
            </b-form-input>
          </b-form-group>
        <!-- <b-form-group id="form-updated-edit-group">
          <b-form-checkbox-group v-model="editForm.updated" id="form-checks"> -->
            <b-form-checkbox checked="true">Updated?</b-form-checkbox>
          <!-- </b-form-checkbox-group>
        </b-form-group> -->
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
</template>
<script>
export default {
  name: 'EditRequest',
  props: {
    request: Object,
  },
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
    onSubmitUpdate() {
      this.updated = true;
      const payload = {
        name: this.name,
        description: this.description,
        status: this.status,
        createdby: this.createdby,
        updated: this.updated, // property shorthand
      };
      this.$emit('update-request', payload);
      this.initForm();
    },
    clear() {
      this.initForm();
    },
  },
};
</script>
