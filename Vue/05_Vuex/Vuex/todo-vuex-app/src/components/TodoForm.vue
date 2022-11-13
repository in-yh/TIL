<template>
  <div>
    <input 
      type="text"
      v-model.trim="todoTitle"
      @keyup.enter="createTodo"
    >
    <!-- v-model은 양방향 -->
    <!-- trim은 좌우 공백 삭제 -->
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data() {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo() {
      // console.log(this.todoTitle)
      if (this.todoTitle) { // 빈 문자열이 아닐 경우만 작성
        this.$store.dispatch('createTodo', this.todoTitle)
      }
      // this.$store.dispatch('createTodo', this.todoTitle)
      // this.$store.dispatch('액션 메서드 이름', 추가데이터)
      this.todoTitle = null // 빈값으로 초기화
    }
  }
}
</script>

<style>

</style>