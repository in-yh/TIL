<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'home' }">Home</router-link> |
      <router-link :to="{ name: 'about' }">About</router-link> |
      <router-link :to="{ name: 'hello', params: {userName: 'yuhyun'} }">Hello</router-link> |
      <router-link :to="{ name: 'login' }">Login</router-link>
      <!-- a 태그와 '비슷한' 기능(페이지를 다시 로드를 하진 않음) -> URL만 이동시킴 -->
      <!--  routes에 등록된 컴포넌트와 매핑됨 -->
      <!--  히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a 태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함 -->
      <!-- 목표 경로는 'to' 속성으로 지정됨 -->
      <!-- 기능에 맞게 HTML에서 a태그로 렌더링되지만, 필요에 따라 다른 태그로 바꿀 수 있음 -->
      <!-- v-bind 이용 -->
      <!-- 'yuhyun' 현재 고정됨, 변수로 만드려면 input과.. -->
    </nav>
    <router-view/>
    <!-- 컴포넌트가 렌더링 될 위치, 컴포넌트가 그려질 화면, 주어진 URL에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트 -->
    <!-- 실제 컴포넌트가 DOM에 부착되어 보이는 자리를 의미 -->
    <!-- 장고에서의 block tag와 비슷함 -->
    <!--  App.vue가 base.html 역할 -->
    <!--  router-view는 block 태그로 감싼 부분 -->
  </div>
</template>

<!-- 
  주소를 이동하는 2가지 방법
  1. 선언적 방식
    router-link의 'to' 속성으로 주소 전달
      routes에 등록된 주소와 매핑된 컴포넌트로 이동
  2. 프로그래밍 방식 네비게이션
    Vue 인스턴스 내부에서 라우터 인스턴스에 $router로 접근할 수 있음
    다른 URL로 이동하려면 this.$router.push를 사용
      history stack에 이동할 URL을 넣는(push) 방식

 -->

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
