<template>
  <div class="container">
    <!-- 가운데 정렬 mx-auto -->
    <div class="mx-auto w-50">
      <b-button variant="success" class="mb-2">PICK</b-button>
      <b-card :title="pickMovie.title" :img-src="`https://image.tmdb.org/t/p/original${pickMovie.poster_path}`" img-alt="Image" img-top>
      </b-card>
    </div>

    <!-- <img alt="no-img" :src="`https://image.tmdb.org/t/p/original${pickMovie.poster_path}`"> -->
    <!-- 콜론(:) 필요! 동적데이터이기 때문 -->
    <!-- <p>{{ pickMovie.title }}</p> -->
  </div>
</template>

<script>
import _ from 'lodash' // npm install lodash

export default {
  name: 'RandomView',
  data() {
    return {
      pickMovie: {},
    }
  },
  computed: {
    moviesList() {
      return this.$store.state.moviesList
    }
  },
  created() {
    this.pickMovie = this.moviesList[_.random(this.moviesList.length-1)]
    // console.log(this.moviesList[_.random(this.moviesList.length-1)].poster_path)
    // console.log(this.moviesList.length-1)
    
  },
}
</script>

<style>

</style>