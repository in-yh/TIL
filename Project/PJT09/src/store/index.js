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
