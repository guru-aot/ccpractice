<template>
  <div>
    <div>
      <AddAuthor />
    </div>
    <div class="mt-6">
      <ListAuthor />
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import AddAuthor from '@/components/Author/AddAuthor.vue'; // @ is an alias to /src
import ListAuthor from '@/components/Author/ListAuthor.vue';
@Component({
  components: {
    AddAuthor,
    ListAuthor
  }
})
export default class Author extends Vue {}
</script>
