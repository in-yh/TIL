<template>
  <div id="app">
    <div style="background-color: #ccf2fc;">
    <!-- 배경색 넣기 -->
      <div class="container">
        <b-navbar variant="faded" type="light" class="d-flex justify-content-between">
        <!-- 양쪽 정렬 -->
          <b-navbar-brand href="#">
            <img src="https://placekitten.com/g/30/30" class="d-inline-block align-top" alt="Kitten">
            BootstrapVue
          </b-navbar-brand>
  
          <b-navbar-nav>
            <b-nav-text class="mx-4"><router-link class="text-decoration-none" to="/movies">Movie</router-link></b-nav-text>
            <b-nav-text class="mx-4"><router-link class="text-decoration-none" to="/random">Random</router-link></b-nav-text>
            <b-nav-text class="mx-4"><router-link class="text-decoration-none" to="/watch-list">WatchList</router-link></b-nav-text>
            
          </b-navbar-nav>
  
        </b-navbar>

      </div>
    </div>

    <router-view/>
  </div>
</template>

<script>
import axios from 'axios' // npm i axios 설치

const API_KEY = '55a806b044eebd05ba19b9855d6e8323'

export default {
  data() {
    return {
      moviesList: [],
    }
  },
  mounted() { // random에서 참조해야하기에 mounted로 설정, created로 하면 참조할 수 없음
    axios.get(`https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}&language=ko-KR&page=1`)
      .then((response) => {
        this.moviesList = response.data.results // axios의 결과값(무비 리스트 20개) 담기
        // console.log(this.moviesList)
        this.$store.dispatch('getTopRated', this.moviesList)
      })
      .catch((error) => {
        console.log(error)
      })
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
