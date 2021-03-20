<template>
  <div>
    <div>
      <!-- <AddAuthor /> -->
    </div>
    <div class="mt-6">
      <ListRequest />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
// import AddAuthor from '@/components/Request/AddRequest.vue'; // @ is an alias to /src
import ListRequest from '@/components/Request/ListRequest.vue';
@Component({
  components: {
    // AddRequest,
    ListRequest
  }
})
export default class Request extends Vue {}
</script>
