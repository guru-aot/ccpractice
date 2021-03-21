<template>
     <!-- <b-modal ref="addRequestModal"
            id="request-modal"
            title="Add a new request"
            hide-footer> -->
      <form @submit.prevent="onSubmit" @reset.prevent="onReset" class="w-100">
      <validation-provider
        v-slot="{ errors }"
        name="Name"
        rules="required|max:10"
      >
        <v-text-field
          v-model="name"
          :counter="10"
          :error-messages="errors"
          label="Name"
          required
        ></v-text-field>
      </validation-provider>
        <validation-provider
        v-slot="{ errors }"
        name="Description"
         :rules="{
          required: false
        }"
      >
        <v-text-field
          v-model="description"
          :counter="10"
          :error-messages="errors"
          label="Description"
        ></v-text-field>
      </validation-provider>
      <validation-provider
        v-slot="{ errors }"
        name="Status"
        rules="required|max:10"
      >
        <v-text-field
          v-model="status"
          :counter="10"
          :error-messages="errors"
          label="Status"
          required
        ></v-text-field>
      </validation-provider>
      <validation-provider
        v-slot="{ errors }"
        name="CreatedBy"
        rules="required|max:10"
      >
        <v-text-field
          v-model="createdby"
          :counter="10"
          :error-messages="errors"
          label="Created By"
          required
        ></v-text-field>
      </validation-provider>
        <v-checkbox
          v-model="updated"
          label="Updated?"
        ></v-checkbox>
         <v-btn
        class="mr-4"
        type="submit"
        :disabled="invalid"
      >
        Submit
      </v-btn>
       <v-btn
        class="mr-4"
        type="reset"
        :disabled="invalid"
      >
        Reset
      </v-btn>
      <!-- <v-btn @click="clear">
        clear
      </v-btn> -->
      </form>
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
