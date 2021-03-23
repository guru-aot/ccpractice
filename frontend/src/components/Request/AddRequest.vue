
/**
 * RequestComponent
 */
<template>
 <v-dialog max-width="640">
     <!-- <v-btn
      class="succcess"
      :loading="loading"
      :disabled="loading"
      color="secondary"
      @click="loader = 'loading'"
    >
      Add Request
    </v-btn> -->
  <template v-slot:activator="{ on }">
    <v-btn v-on="on" class="succcess">Add Request</v-btn>
  </template>
  <v-card class="mx-auto" style="max-width: 500px;">
    <v-alert type="success" v-if="successStatus">Request Added succesfully</v-alert>
    <v-alert type="error" v-if="errorStatus">Something went wrong...</v-alert>

    <v-toolbar color="deep-purple accent-4" cards dark flat>
      <v-card-title class="title font-weight-regular">Add Request</v-card-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-form ref="form" v-model="form" class="pa-4 pt-6">
      <v-text-field
        v-model="name"
        filled
        color="deep-purple"
        counter="10"
        label="Name"
        style="min-height: 96px"
        type="text"
        :rules="[rules.required]"
      ></v-text-field>
      <v-text-field
        v-model="description"
        filled
        color="deep-purple"
        counter="250"
        label="Description"
        style="min-height: 96px"
        type="text"
        :rules="[rules.required]"
      ></v-text-field>
      <v-text-field
        v-model="status"
        filled
        color="deep-purple"
        counter="10"
        label="Status"
        style="min-height: 96px"
        type="text"
        :rules="[rules.required]"
      ></v-text-field>
      <v-text-field
        v-model="createdby"
        filled
        color="deep-purple"
        counter="10"
        label="Created By"
        style="min-height: 96px"
        type="text"
        :rules="[rules.required]"
      ></v-text-field>
    </v-form>
    <v-divider></v-divider>
    <v-card-actions>
      <v-btn text @click="$refs.form.reset()">Clear</v-btn>
      <v-spacer></v-spacer>
      <v-btn
        :disabled="!form"
        :loading="isLoading"
        class="white--text"
        color="deep-purple accent-4"
        depressed
        @click="addRequest"
      >Submit</v-btn>
    </v-card-actions>
  </v-card>
 </v-dialog>
</template>
 <script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
const RequestModule = namespace('RequestModule');

@Component
export default class RequestComponent extends Vue {
  @RequestModule.Getter('successStatus') public successStatus!: boolean;
  @RequestModule.Getter('errorStatus') public errorStatus!: boolean;
  @RequestModule.Action('addRequest') public addRequestStore!: any;
  public form: boolean = false;
  private isLoading: boolean = false;
  private name: string = '';
  private description: string = '';
  private status: string = '';
  private createdby: string = '';

  private rules = {
    length: (len: any) => (v: any) =>
      (v || '').length >= len || 'Invalid character length, required' + len,

    required: (v: any) => !!v || 'This field is required'
  };
  /**
   * @description
   */
  private addRequest() {
    const data = {
      name: this.name,
      description: this.description,
      status: this.status,
      createdby: this.createdby
    };

    this.addRequestStore(data);
    // this.$refs.form.reset();
    (this.$refs.form as HTMLFormElement).reset();
  }
}
</script>
 