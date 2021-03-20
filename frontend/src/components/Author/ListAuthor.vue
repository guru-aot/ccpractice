

  /**
   * ListViewComponent Page
   */
  
  <template>
  <v-card class="mx-auto">
    <v-toolbar flat>
      <v-toolbar-title class="grey--text">All Author</v-toolbar-title>
      <div class="flex-grow-1"></div>
    </v-toolbar>
    <v-divider></v-divider>
    <v-card-text v-if="getAuthorList && getAuthorList.length == 0">No Author found. Add one</v-card-text>
    <v-card-text v-if="getAuthorList && getAuthorList.length != 0">
      <v-simple-table fixed-header>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">SI</th>
              <th class="text-left">first_name</th>
              <th class="text-left">last_name</th>
              <th class="text-left">middle_name</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(author ,idx) in  getAuthorList" :key="author.id">
              <td>{{ idx+1 }}</td>
              <td>{{ author.first_name }}</td>
              <td>{{ author.last_name }}</td>
              <td>{{ author.middle_name }}</td>
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
const AuthorModule = namespace('AuthorModule');

@Component
export default class ListAuthorComponent extends Vue {
  @AuthorModule.Action('loadAuthor') public loadAuthor!: any;
  @AuthorModule.Getter('getAuthorList') public getAuthorList!: [];

  private mounted() {
    this.loadAuthor();
  }
}
</script>
 