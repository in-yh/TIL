import Vue from 'vue'
import Vuex from 'vuex'
// import createPersistedState from 'vuex-persistedstate'

// vuex-persistedstate
//  Vuex state를 자동으로 브라우저의 Local Storage에 저장해주는 라이브러리 중 하나
//  페이지가 새로고침 되어도 Vuex state를 유지시킴
//  Local Storage에 저장된 data를 자동으로 state로 불러옴
// npm i vuex-persistedstate => import => plugins

Vue.use(Vuex)

export default new Vuex.Store({
  // plugins: [
  //   createPersistedState(),
  // ],
  state: {
    todos: [ // 출력을 위한 기본 todo 작성
      // {
      //   title: '할 일 1',
      //   isCompleted: false,
      // },
      // {
      //   title: '할 일 2',
      //   isCompleted: false,
      // }
    ]
  },
  getters: {
    allTodosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state) {
      // 1. 완료된 투두만 모아놓은 새로운 배열을 생성
      const completedTodos = state.todos.filter((todo) => {
        return todo.isCompleted === true
      })
      // 2. 그 새로운 배열의 길이를 반환
      return completedTodos.length
    },
    // 두번째 인자가 getters
    unCompletedTodosCount(state, getters) {
      return getters.allTodosCount - getters.completedTodosCount
    }
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem) // push 메서드로 넣기
    },
    DELETE_TODO(state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1) 
      // 인덱스 찾고 빼버리기
    },
    UPDATE_TODO_STATUS(state, todoItem) {
      // console.log(todoItem)
      // todos 배열에서 선택된 todo의 isCompleted값만 토글한 후
      // 업데이트 된 todos 배열로 되어야 함

      // 반복으로 돈 결과가 todos로 할당
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })

      // 내 코드와 비슷..
      // const index = state.todos.indexOf(todoItem)
      // state.todos[index].isCompleted === !state.todos[index].isCompleted
    },
    LOAD_TODOS(state) {
      const localStorageTodos = localStorage.getItem('todos')
      const parsedTodos = JSON.parse(localStorageTodos) // 문자열 데이터를 다시 object 타입으로 변환(JSON.parse)
      console.log(parsedTodos)
      state.todos = parsedTodos
    }
  },
  actions: {
    createTodo(context, todoTitle) {
      // Todo 객체 만들기
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      // console.log(todoItem)
      context.commit('CREATE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage') // 저장
    },
    deleteTodo(context, todoItem) {
      // 딱히 할 게 없음 바로 뮤테이션 호출
      context.commit('DELETE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage') // 저장
    },
    updateTodoStatus(context, todoItem) {
      context.commit('UPDATE_TODO_STATUS', todoItem)
      context.dispatch('saveTodosToLocalStorage') // 저장
    },
    // 브라우저의 Local Storage에 todo 데이터 저장하여 브라우저를 종료 후 실행해도 데이터가 보존될 수 있게 하기
    // Window.localStorage.메서드()
    // 데이터가 문자열 형태로 저장됨
    // 관련 메서드
    //  setItem(key, value) - key, value 형태로 데이터 저장
    //  getItem(key) - key에 해당하는 데이터 조회
    saveTodosToLocalStorage(context) { // state를 변경하지 않기에 액션에 작성
      const jsonTodos = JSON.stringify(context.state.todos) // 데이터가 문자열 형태로 저장되어야 하기 때문에 JSON.stringify를 사용해 문자열로 변환
      localStorage.setItem('todos', jsonTodos)
    },
    loadTodos(context) {
      context.commit('LOAD_TODOS')
    }
    // 불러오기 버튼을 누르면 Local Storage에 저장된 데이터를 가져오도록 할 것
    //  1. 불러오기 버튼 작성
    //  2. loadTodos 메서드 작성
    //  3. loadTodes actions 메서드 작성
    //  4. LOAD_TODOS mutations 메서드 작성
  },
  modules: {
  }
})
