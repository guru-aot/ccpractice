<template>
  <div>
    <div>
      
       <!-- <button type="button" class="btn btn-success btn-sm" @click="openAddRequest">
          Add Request
        </button> -->
      <!-- <AddRequest v-show="this.showAddRequest" /> -->
      <AddRequest />
    </div>
    <div class="mt-6">
      <ListRequest />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import AddRequest from '@/components/Request/AddRequest.vue'; // @ is an alias to /src
import ListRequest from '@/components/Request/ListRequest.vue';
@Component({
  components: {
    AddRequest,
    ListRequest
  }
})
export default class Request extends Vue {
  private showAddRequest: boolean = false;
  private openAddRequest() {
      this.showAddRequest = !this.showAddRequest;
  }
}
</script>
