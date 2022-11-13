<template>
  <div>
    <TodoListItem
      v-for="(todo, index) in todos"
      :key="index"
      :todo="todo"
    />
    <!-- :todo="todo"는 Pass Props -->
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem';

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  // store에 state를 computed로 받기
  computed: {
    todos() {
      return this.$store.state.todos
    }
  },
}
</script>

<style>

</style>