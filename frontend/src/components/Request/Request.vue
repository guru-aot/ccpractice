/**
 * RequestComponent
 */
<template>
   <v-toolbar
        flat
      >
        <v-toolbar-title>My CRUD</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              New Request
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.name"
                      label="Request Name"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.description"
                      label="Description"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.status"
                      label="Status"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.createdby"
                      label="Created By"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >                   
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="save"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="headline">Are you sure you want to delete this item?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>      
</template>
<script lang="ts">
import { Component, Vue, Watch } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
const RequestModule = namespace('RequestModule');

@Component
export default class RequestComponent extends Vue {
  @RequestModule.Getter('successStatus') public successStatus!: boolean;
  @RequestModule.Getter('errorStatus') public errorStatus!: boolean;
  @RequestModule.Action('addRequest') public addRequestStore!: any;
  @RequestModule.Action('updateRequest') public updateRequestStore!: any;
  @RequestModule.Action('deleteRequest') public deleteRequestStore!: any;
  public form: boolean = false;
  private dialog: boolean = false;
  private dialogDelete: boolean = false;
  private name: string = '';
  private description: string = '';
  private status: string = '';
  private createdby: string = '';
  private editedIndex: number = -1;
  private defaultItem: object = {
      name: '',
      description: '',
      status: '',
      createdby: ''
  };
  private editedItem: object = {
      name: '',
      description: '',
      status: '',
      createdby: ''
  };

  private rules = {
    length: (len: any) => (v: any) =>
      (v || '').length >= len || 'Invalid character length, required' + len,

    required: (v: any) => !!v || 'This field is required'
  };
  get formTitle() {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item';
  }
//   @Watch('dialog')
//   onPropertyChanged(value: boolean, oldValue: boolean) {
//     // Do stuff with the watcher here.
//   }
  private close() {
    this.dialog = false;
    this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
    });
  }
  private save() {
    if (this.editedIndex > -1) {
      this.updateRequestStore(this.editedItem);
    } else {
      this.addRequestStore(this.editedItem);
    }
    this.close();
  }
  private closeDelete() {
    this.dialogDelete = false;
    this.$nextTick(() => {
      this.editedItem = Object.assign({}, this.defaultItem);
      this.editedIndex = -1;
    });
  }
  private deleteItemConfirm() {
    this.deleteRequestStore(this.editedItem);
    this.closeDelete();
  }
}
</script>
 