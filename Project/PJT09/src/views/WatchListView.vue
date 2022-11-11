<template>
  <div class="container">
    <h1>보고싶은 영화</h1>
    <WatchListForm/>
    <!-- for문 돌려주기 -->
    <!-- {{ watchList }} -->
    <b-list-group>
      <WatchListItem
        v-for="(watch, index) in watchList" :key="index"
        :movie-props="watch"
      />
    </b-list-group>
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm'
import WatchListItem from '@/components/WatchListItem'

export default {
  name: 'WatchListView',
  components: {
    WatchListForm,
    WatchListItem,
  },
  computed: {
    watchList() {
      return this.$store.state.watchList
    }
  },
}
</script>

<style>

</style>