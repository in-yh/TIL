<template>
  <div id="app">
    <!-- 사용하기 -->
    <TodoList :todos="todos" @delete-todo="deleteTodo"/>
    <TodoForm
      @create-todo="createTodo"
    />
  </div>
</template>

<script>
// 불러오고
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm, // 등록하고
    TodoList,
  },
  data: function () {
    return {
      todos: [
        // {
        //   title: '할 일',
        // }
      ]
    }
  },
  methods: {
    createTodo: function (todoTitle) {
      const todo = {
        title: todoTitle
      }
      this.todos.push(todo) // 객체를 만들어 data 배열에 푸쉬!
    },
    deleteTodo: function (todo) {
      const index = this.todos.indexOf(todo) // 해당 todo의 인덱스 찾기
      this.todos.splice(index, 1) // 해당 인덱스의 요소를 삭제하고 이것만 빼고 다시 리스트 만들어줌
    }
    // 데이터가 있는 곳에서 생성하고 삭제 가능!
    // App에 데이터를 놓지 않으면(TodoList에 데이터를 놓으면), 생성하고 삭제할 때 emit하고 props을 섞어서 해야함
  }
}
</script>

<style>

</style>
