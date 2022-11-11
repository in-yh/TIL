# PJT 09

### 이번 pjt 를 통해 배운 내용

- 영화 정보를 제공하는 SPA 제작
- AJAX 통신과 JSON 구조에 대한 이해
- Vue CLI, Vue Router 플러그인 활용



## A. 최고 평점 영화 출력

- 요구 사항 :

  - 네비게이션 바에서 Movie 링크(/movies)를 클릭하면 
  - AJAX 통신을 이용하여 TMDB API로부터 JSON 데이터를 받아와 
  - 영화 목록 출력

- 결과 :

  - 문제 접근 방법 및 코드 설명
    - App.vue에서 AJAX 통신을 이용하여 JSON 데이터 받아서 store에 저장
    - MovieView.vue에서 store에 저장된 데이터를 가져와 순회하며 하나의 movie 데이터를 MovieCard.vue에 prop 시킴
    - MovieCard.vue에서 카드에 담아 출력
  
  ```vue
  // App.vue
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
  
  
  // MovieView.vue
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
  
  
  // MovieCard.vue
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
  ```
  
  ```javascript
  // router/index.js
  import Vue from 'vue'
  import VueRouter from 'vue-router'
  import MovieView from '../views/MovieView.vue'
  import RandomView from '../views/RandomView.vue'
  import WatchListView from '../views/WatchListView.vue'
  
  Vue.use(VueRouter)
  
  const routes = [
    {
      path: '/movies',
      name: 'movies',
      component: MovieView
    },
  ]
  
  
  // store/index.js
  import Vue from 'vue'
  import Vuex from 'vuex'
  import createPersistedState from 'vuex-persistedstate' // npm i vuex-persistedstate // 새로고침해도 저장된 데이터 가져옴
  
  Vue.use(Vuex)
  
  export default new Vuex.Store({
    plugins: [
      createPersistedState(),
    ],
    state: {
      moviesList: [],
      watchList: [],
    },
    getters: {
    },
    mutations: {
      GET_TOP_RATED(state, moviesList) {
        state.moviesList = moviesList
      },
    },
    actions: {
      getTopRated(context, moviesList) {
        context.commit('GET_TOP_RATED', moviesList)
      },
    },
    modules: {
    }
  })
  ```
  
  - 이 문제에서 어려웠던 점
    - App.vue에서 AJAX 사용할 때 created로 하면 나중에 참조가 불가능하기에 mounted로 변경하였음
  - 내가 생각하는 이 문제의 포인트
    - AJAX 통신 이용해 store에 데이터 저장하는 법과 store 데이터를 사용하는 법

------



## B. 최고 평점 영화 중 랜덤 영화 한 개 출력

- 요구 사항 :

  - 네비게이션 바에서 Random 링크(/random)를 클릭하면 저장된 최고 평점 영화 목록 중 랜덤으로 한 개 출력
  
- 결과 :

  - 문제 접근 방법 및 코드 설명
    - lodash 사용하여 랜덤 영화 추출
  
  ```vue
  // RandomView.vue
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
  ```
  
  ```javascript
  // router/index.js
  import Vue from 'vue'
  import VueRouter from 'vue-router'
  import MovieView from '../views/MovieView.vue'
  import RandomView from '../views/RandomView.vue'
  import WatchListView from '../views/WatchListView.vue'
  
  Vue.use(VueRouter)
  
  const routes = [
    {
      path: '/movies',
      name: 'movies',
      component: MovieView
    },
    {
      path: '/random',
      name: 'random',
      component: RandomView
    },
  ]
  ```
  
  - 이 문제에서 어려웠던 점
    - src 입력할 때 동적 데이터로 하기 위해 콜론 사용
  - 내가 생각하는 이 문제의 포인트
    - store에 있는 데이터를 가져온 후 랜덤으로 뽑아서 바로 출력

------



## C. 보고 싶은 영화 등록 및 삭제하기

- 요구 사항:
  - 네비게이션 바에서 WatchList 링크(/watch-list)를 클릭하면 보고 싶은 영화 제목을 등록할 수 있는 Form 출력
  - 등록된 영화 제목을 클릭하면 취소선 그어짐
  
- 결과 :

  - 문제 접근 방법 및 코드 설명
    - WatchListForm.vue에서 영화 데이터 추가하는 함수 작성 후 store/index.js로 올려줌
    - store에 저장된 데이터를 WatchListView.vue에서 받아서 WatchListItem.vue으로 내려줌
    - WatchListItem.vue에서 취소선 긋는 함수 작성
  
  ```vue
  // WatchListView.vue
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
  
  
  // WatchListForm.vue
  <template>
    <div>
      <input 
        @keyup.enter.prevent="addMovie" 
        type="text"
        v-model="inputData"
      >
      <button @click.prevent="addMovie" type="submit">Add</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'WatchListForm',
    data() {
      return {
        inputData: '', 
        // watchList: [],
      }
    },
    methods: {
      addMovie() {
        // this.watchList.push(this.inputData) // 리스트에 넣을 때 push
        // console.log(this.watchList)
        this.$store.dispatch('addMovie', this.inputData)
        this.inputData = '' // 인풋 데이터 초기화
      }
    },
  }
  </script>
  
  
  // WatchListItem.vue
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
  ```
  
  ```javascript
  // router/index.js
  import Vue from 'vue'
  import VueRouter from 'vue-router'
  import MovieView from '../views/MovieView.vue'
  import RandomView from '../views/RandomView.vue'
  import WatchListView from '../views/WatchListView.vue'
  
  Vue.use(VueRouter)
  
  const routes = [
    {
      path: '/movies',
      name: 'movies',
      component: MovieView
    },
    {
      path: '/random',
      name: 'random',
      component: RandomView
    },
    {
      path: '/watch-list',
      name: 'watch-list',
      component: WatchListView
    },
  ]
  
  
  // store/index.js
  import Vue from 'vue'
  import Vuex from 'vuex'
  import createPersistedState from 'vuex-persistedstate' // npm i vuex-persistedstate // 새로고침해도 저장된 데이터 가져옴
  
  Vue.use(Vuex)
  
  export default new Vuex.Store({
    plugins: [
      createPersistedState(),
    ],
    state: {
      moviesList: [],
      watchList: [],
    },
    getters: {
    },
    mutations: {
      GET_TOP_RATED(state, moviesList) {
        state.moviesList = moviesList
      },
      ADD_MOVIE(state, addMovieData) {
        state.watchList.push(addMovieData) // 리스트에 넣을 때 push
      },
      DELETE_MOVIE(state, deleteMovieData) {
        // 전체 for문을 순회하며, 클릭한 영화와 같다면 그 영화의 isCompleted를 바꿔줌
        state.watchList.forEach((watch) => { 
          if (watch === deleteMovieData) {
            watch.isCompleted = !watch.isCompleted
          }
        }) 
      }
    },
    actions: {
      getTopRated(context, moviesList) {
        context.commit('GET_TOP_RATED', moviesList)
      },
      addMovie(context, inputData) {
        const addMovieData = { // 취소선 구현 위해 객체로 만듦
          title: inputData,
          isCompleted: false,
        }
        // console.log(addMovieData)
        context.commit('ADD_MOVIE', addMovieData)
      },
      deleteMovie(context, movieData) {
        context.commit('DELETE_MOVIE', movieData)
      }
    },
    modules: {
    }
  })
  ```
  
  - 이 문제에서 어려웠던 점
    - 취소선 긋기 위해 데이터에 is-completed 속성 추가하여 Object로 만들어줌
    - 취소선 그을 때 v-bind 사용하는 방법
    - 새로고침하여도 데이터 날라가지 않게 하기 위해 `vuex-persistedstate` 라이브러리 사용
  - 내가 생각하는 이 문제의 포인트
    - 취소선 긋는 방법

------



# 후기

- 기능 구현은 그래도 복습하면서 진행하였기에 큰 어려움은 없었으나
- CSS는 부트스트랩과 부트스트랩뷰가 은근 달라서.. 쉽지 않았고 아직도 어렵다.. 많이 해보는게 필요할 듯 하다.
