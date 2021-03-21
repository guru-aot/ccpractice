

  /**
   * ListViewComponent Page
   */
  
  <template>
  <v-card class="mx-auto">
    <v-toolbar flat>
      <v-toolbar-title class="grey--text">All Requests</v-toolbar-title>
      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>
    <v-spacer></v-spacer>
    <v-card-text v-if="getRequestList && getRequestList.length == 0">No Author found. Add one</v-card-text>
    <v-card-text v-if="getRequestList && getRequestList.length != 0">
      <v-data-table 
      :headers="getRequestHeaders"     
      :items="getRequestList"
      :items-per-page="5"      
      >
      <template v-slot:top>
        <Request />
      </template>
      <!-- <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template> -->
      <!-- <v-simple-table fixed-header>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">ID</th>
              <th class="text-left">Name</th>
              <th class="text-left">Description</th>
              <th class="text-left">Status</th>
              <th class="text-left">Created By</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(request ,idx) in  getRequestList" :key="request.requestid">
              <td>{{ idx+1 }}</td>
              <td>{{ request.name }}</td>
              <td>{{ request.description }}</td>
              <td>{{ request.status }}</td>
              <td>{{ request.createdby }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table> -->
      </v-data-table>
    </v-card-text>
  </v-card>
</template>
  <script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
import Request from './Request.vue';
const RequestModule = namespace('RequestModule');

@Component({
  components: {
    Request,
  }
})
export default class ListRequestComponent extends Vue {
  @RequestModule.Action('loadRequest') public loadRequest!: any;
  @RequestModule.Action('updateRequest') public updateRequest!: any;
  @RequestModule.Getter('getRequestList') public getRequestList!: [];
  @RequestModule.Getter('getRequestHeaders') public getRequestHeaders!: [];

  private mounted() {
    this.loadRequest();
  }

  // private editItem(item) {
  //       console.log(item);
  //       this.updateRequest(item);
  //       // this.editedIndex = this.desserts.indexOf(item);
  //       // this.editedItem = Object.assign({}, item);
  //       // this.dialog = true;
  // }

  // private deleteItem(item) {
  //   console.log(item);
  //       // this.editedIndex = this.desserts.indexOf(item);
  //       // this.editedItem = Object.assign({}, item);
  //       // this.dialogDelete = true;
  // }
}
</script>
 