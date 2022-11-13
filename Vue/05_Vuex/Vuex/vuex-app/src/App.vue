<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <h2>입력된 문자의 길이는 {{ messageLength }}</h2>
    <h3>x2 : {{ doubleLength }}</h3>
    <input 
      type="text"
      @keyup.enter="changeMessage"
      v-model="inputData"
    >
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      inputData: null,
    }
  },
  computed: {
    // $store.state로 바로 접근하기보다 computed에 정의 후 접근하는 것을 권장
    // getters 역시 state와 마찬가지로 computed에 정의해서 사용하는 것을 권장
    message() {
      return this.$store.state.message // 이 컴포넌트에서 가져오기에 this 사용
    },
    messageLength() {
      return this.$store.getters.messageLength // store에 있는 getters
    },
    doubleLength() {
      return this.$store.getters.doubleLength
    },
  },
  methods: {
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
      // this.$store.dispatch('액션 메서드 이름', 추가데이터)
      // dispatch 메서드로 actions 호출
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
