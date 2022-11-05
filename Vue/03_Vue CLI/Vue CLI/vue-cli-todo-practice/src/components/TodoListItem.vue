<template>
  <!-- ul태그로 받기 때문에 -->
  <li> 
    {{ todo.title }}
    <button @click="deleteTodo">X</button>
  </li>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo: function () {
      this.$emit('delete-todo', this.todo) // 누가 눌렸는지 필요함!!!(반복문 안에 있는 특정 todo임)
    }
  }
}
</script>

<style>

</style>