<template>
  <div>
    <!-- 취소선 구현 -->
    <span 
      @click="updateTodoStatus" 
      :class="{ 'is-completed' : todo.isCompleted }"
    >
    <!-- class v-bind 해줘야 문자열로 안 들어가고 자스 표현식으로 들어감 -->
    <!-- v-bind 복습 필요.. -->
      {{ todo.title }}
    </span>
    <!-- 삭제버튼은 item 옆에 -->
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    deleteTodo() {
      // console.log('삭제 메서드 호출!')
      this.$store.dispatch('deleteTodo', this.todo)
      // this.$store.commit('DELETE_TODO', this.todo) // 액션에서 할게 없을 때는 이렇게 가능
    },
    updateTodoStatus() {
      // console.log('업데이트 메서도 호출!')
      this.$store.dispatch('updateTodoStatus', this.todo)
    },
  },
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>