<template>
  <div class="about">
    <h1>This is an about page</h1>
    <!-- 주소를 이동하는 2가지 방법 -->
    <!-- 1. 선언적 방식 네비게이션 -->
    <!-- <router-link to="/">Home</router-link> -->
    <router-link :to="{ name: 'home' }">Home</router-link>
    <!-- router-link의 'to' 속성으로 주소 전달 -->
    <!--  routes에 등록된 주소와 매핑된 컴포넌트로 이동 -->
    <!-- 동적인 값을 사용하기 때문에 v-bind를 사용해야 정상적으로 작동 -->
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
    // AboutView에서 데이터를 입력 받아 HelloView로 이동하여 입력받은 데이터에게 인사하기
  },
}
// 2. 프로그래밍적 방식 네비게이션
// Vue 인스턴스 내부에서 라우터 인스턴스에 $router로 접근할 수 있음
// 다른 URL로 이동하려면 this.$router.push를 사용
//  history stack에 이동할 URL을 넣는(push) 방식
//  history stack에 기록이 남기 때문에 사용자가 브라우저의 뒤로 가기 버튼을 클릭하면 이전 URL로 이동할 수 있음
// 결국 <router-link :to="...">를 클릭하는 것과 $router.push(...)를 호출하는 것은 같은 동작


// src/Views
//  router-view에 들어갈 컴포넌트 작성
//  기존에 컴포넌트를 작성하던 곳은 컴포넌트 폴더 뿐이었지만 이제 두 폴더로 나뉘어짐
//  각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님
//  이제 폴더별 컴포넌트 배치는 다음과 같이 진행(규약은 아님)
//  views/
//    routes에 메핑되는 컴포넌트, 즉 <router-view>의 위치에 렌더링 되는 컴포넌트를 모아두는 폴더
//    다른 컴포넌트와 구분하기 위해 View로 끝나도록 만드는 것을 권장
//    ex) App 컴포넌트 내부의 AboutView & HomeView 컴포넌트
//  components/
//    routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더
//    ex) HomeView 컴포넌트 내부의 HelloWorld 컴포넌트
</script>