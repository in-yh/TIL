<template>
  <div class="container">
    <div class="row">
        <MovieCard
          v-for="movie in moviesList" :key="Number(`${movie.id}`)"
          :movie-props="movie"
          class="col-4 mb-2"
        />
        <!-- key 설정해줘야 vue component 창에 key값이 movie.id로 출력됨 -->
        <!-- class="col-4"를 카드 내부에 설정 -->
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'


export default {
  name: 'MovieView',
  components: {
    MovieCard,
  },
  computed: {
    moviesList() {
      return this.$store.state.moviesList
    }
  },
}
</script>

<style>

</style>