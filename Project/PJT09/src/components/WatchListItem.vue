<template>
  <div>
    <b-list-group-item><span @click="deleteMovie" :class="{ 'is-completed' : movieProps.isCompleted }">{{ movieProps.title }}</span></b-list-group-item>
    <!-- <p @click="deleteMovie" :class="{ 'is-completed' : movieProps.isCompleted }">{{ movieProps.title }}</p> -->
    <!-- is-completed가 true이면 취소선 넣기 -->
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  props: {
    movieProps: Object,
  },
  methods: {
    deleteMovie() {
      this.$store.dispatch('deleteMovie', this.movieProps)
      // console.log(this.movieProps)
    }
  },
}
</script>

<style>
.is-completed {
  text-decoration: line-through;
}
.background-completed {
  background-color: #a7aaab;
}
</style>