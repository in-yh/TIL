<template>
  <div class="about">
    <h1>This is an about page</h1>
    <!-- 선언적 방식 -->
    <router-link :to="{ name: 'home' }">Home</router-link>
    <button @click="toHome">홈으로!</button>
    <input 
      type="text"
      v-model="inputData" 
      @keyup.enter="dataShow"
    >
    <!-- v-bind가 아니라 v-model 사용해야 연동됨.. -->
    <!-- .으로! -->
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  data() {
    return {
      inputData: null, // null로 입력 후 위에서 입력하면 자동 저장
    }
  },
  methods: {
    toHome() {
      this.$router.push({ name: 'home' })
    },
    dataShow() {
      this.$router.push({ name: 'hello', params: {userName: this.inputData} })
    }
  },
}
// 프로그래밍적 방식

// src/Views
//  router-view에 들어갈 컴포넌트 작성
//  기존에 컴포넌트를 작성하던 곳은 컴포넌트 폴더 뿐이었지만 이제 두 폴더로 나뉘어짐
//  각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님
</script>