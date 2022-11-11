<template>
  <div>
    <b-card :title="movieProps.title" :img-src="`https://image.tmdb.org/t/p/original${movieProps.poster_path}`" img-alt="Image" img-top>
      <b-card-text>
        {{ movieProps.overview }}
      </b-card-text>
    </b-card>
  </div>

    <!-- <div> -->
      <!-- <img :src="`https://image.tmdb.org/t/p/original${movieProps.poster_path}`" alt="no-img">
      <p>{{ movieProps.title }}</p>
      <p>{{ movieProps.overview }}</p> -->
    <!-- </div> -->
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movieProps: [],
  }
}
</script>

<style>

</style>