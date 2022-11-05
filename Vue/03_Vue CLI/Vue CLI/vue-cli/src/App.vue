<template>
  <div id="app">
    <!-- npm run serve하면 나오는 마크 -->
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- npm run serve하면 나오는 내용 -->
    <!-- 3. 보여주기 -->
    <MyComponent/>
    <HelloWorld msg-title="Welcome to Your Vue.js App!!!"/>
    <!-- 1. -->
    <!-- 정적인 데이터를 전달하는 경우 static props라고 명시하기도 함 -->
    <!-- props를 내려준다(pass props) : 부모=>자식 -->
    <!-- prop-data-name="value"의 형태로 데이터를 전달 (이 때 속성의 키 값은 kebab-case를 사용) html은 대소문자 구분 없이 사용하기 때문에 -->
    <!-- html(케밥케이스) -> JS(카멜케이스) -->
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
// 1. 불러오기
// import MyComponent from './components/MyComponent.vue'
import MyComponent from '@/components/MyComponent'
// @는 src를 의미(절대경로로 바꾸기) / .vue도 생략

export default {
  name: 'App',
  components: {
    HelloWorld,
    // 2. 등록하기
    MyComponent,
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

<!-- public/index.html 과 연결되어 있음! -->

<!-- component 등록 3단계(반드시 외우기!!) -->
<!-- 1. 불러오기 -->
<!-- 2. 등록하기 -->
<!-- 3. 보여주기 -->