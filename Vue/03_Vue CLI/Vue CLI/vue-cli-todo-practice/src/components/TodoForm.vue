<template>
  <div>
    <input 
      type="text"
      v-model="todoTitle"
      @keyup.enter="createTodo" 
    >
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () { // data로 먼저 정의!
    return {
      todoTitle: null, 
    }
  },
  methods: {
    createTodo: function () {
      this.$emit('create-todo', this.todoTitle)
      this.todoTitle = null // 비워주기
    }
  }
}
</script>

<style>

</style>