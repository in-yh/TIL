<template>
  <div>
    <h3>이건 MyComponent의 하위 컴포넌트</h3>
    <p>{{ staticProps }}</p>
    <!-- 개발자 도구 보면 MyComponentItem에 뜨긴하지만, 부모가 내려준 데이터이고, props라고도 명시되어 있음 -->
    <p>{{ dynamicProps }}</p>
    <!-- e1. 클릭이벤트가 발생했을 때 함수 실행 -->
    <button @click="childToParent">클릭!</button>
    <input 
      type="text" 
      v-model="childInputData"
      @keyup.enter="childInput"  
    >
    <!-- 양방향은 v-model -->
  </div>
</template>

<script>
export default {
  name: 'MyComponentItem',
  props: {
    staticProps: String, // 카멜케이스로 바꿔줘야 함
    dynamicProps: String, // 왼쪽의 dynamic-props을 받은 거임
  },
  data: function () {
    return {
      childInputData: null, // v-model로 연결하면 input하면 바로바로 바뀜
    }
  },
  methods: {
    // e2. $emit 발생시키기
    childToParent: function () {
      // data = {

      // }
      this.$emit('chlid-to-parent', '나는 자식이 보낸 데이터다') // 또다른 emit과 겹칠 수 있으니 $emit로 작성. emit은 소리를 친다. 바로 위 부모에게. 케밥케이스로 보내줌. 첫번째 인자는 이름, 두번째 인자는 데이터
    },
    childInput: function () {
      this.$emit('child-input', this.childInputData) // 사용자가 입력한 데이터를 넣어 부모로 가자!
    }
  },
}
// 1. 부모에서 내려주고
// 2. 자식에서 선언하고 출력하기
</script>

<style>

</style>