

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
    <v-card-text v-if="getRequestList && getRequestList.length == 0">No Author found. Add one</v-card-text>
    <v-card-text v-if="getRequestList && getRequestList.length != 0">
      <v-simple-table fixed-header>
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
      </v-simple-table>
    </v-card-text>
  </v-card>
</template>
  <script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Getter, namespace, Action } from 'vuex-class';
const RequestModule = namespace('RequestModule');

@Component
export default class ListRequestComponent extends Vue {
  @RequestModule.Action('loadRequest') public loadRequest!: any;
  @RequestModule.Getter('getRequestList') public getRequestList!: [];

  private mounted() {
    this.loadRequest();
  }
}
</script>
 