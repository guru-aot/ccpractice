
/**
 * AuthorComponent
 */
 <template>
  <v-card class="mx-auto" style="max-width: 500px;">
    <v-alert type="success" v-if="successStatus">Author Added succesfully</v-alert>
    <v-alert type="error" v-if="errorStatus">Something went wrong...</v-alert>

    <v-toolbar color="deep-purple accent-4" cards dark flat>
      <v-card-title class="title font-weight-regular">Add Author</v-card-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-form ref="form" v-model="form" class="pa-4 pt-6">
      <v-text-field
        v-model="firstName"
        filled
        color="deep-purple"
        counter="10"
        label="First name"
        style="min-height: 96px"
        type="text"
        :rules="[rules.required]"
      ></v-text-field>
      <v-text-field
        v-model="lastName"
        filled
        color="deep-purple"
        counter="10"
        label="Last name"
        style="min-height: 96px"
        type="text"
        :rules="[rules.required]"
      ></v-text-field>
      <v-text-field
        v-model="middleName"
        filled
        color="deep-purple"
        counter="10"
        label="Middle name"
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
        @click="addAuthor"
      >Submit</v-btn>
    </v-card-actions>
  </v-card>
</template>
 <script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
const AuthorModule = namespace('AuthorModule');

@Component
export default class AuthorComponent extends Vue {
  @AuthorModule.Getter('successStatus') public successStatus!: boolean;
  @AuthorModule.Getter('errorStatus') public errorStatus!: boolean;
  @AuthorModule.Action('addAuthor') public addAuthorStore!: any;
  public form: boolean = false;
  private isLoading: boolean = false;
  private firstName: string = '';
  private lastName: string = '';
  private middleName: string = '';

  private rules = {
    length: (len: any) => (v: any) =>
      (v || '').length >= len || 'Invalid character length, required' + len,

    required: (v: any) => !!v || 'This field is required'
  };
  /**
   * @description
   */
  private addAuthor() {
    const data = {
      first_name: this.firstName,
      last_name: this.lastName,
      middle_name: this.middleName
    };

    this.addAuthorStore(data);
    // this.$refs.form.reset();
    (this.$refs.form as HTMLFormElement).reset();
  }
}
</script>
 