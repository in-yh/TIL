<template>
  <div>
    <ul v-for="(todo, index) in todos" :key="index">
      <TodoListItem 
        :todo="todo"
        @delete-todo="deleteTodo"
      />
    </ul>
  </div>
</template>
<!-- deleteTodo 또 써도 상관없음 -->

<script>
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  props: {
    todos: Array,
  },
  methods: {
    deleteTodo: function (todo) { // 자식에서 받은 것을 todo로 정함
      this.$emit('delete-todo', todo) // 이건 위에 인자를 받아서
    }
  }
}
</script>

<style>

</style>