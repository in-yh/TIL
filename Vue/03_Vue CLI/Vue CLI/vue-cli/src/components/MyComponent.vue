<template>
  <!-- 2. template 요소 추가(컴포넌트를 구성하는 최상위 태그 단 한 개가 있어야 함(div가 아니어도 되지만)!! template는 영역표시 정도일 뿐, 렌더링은 div부터 시작됨) -->
  <div class="border"> 
    <h1>내가 만든 새로운 컴포넌트!</h1>
    <!-- 3. 보여주기 -->
    <MyComponentItem 
      static-props="MyComponent에서 보낸 데이터"
      :dynamic-props="dynamicProps"
      @chlid-to-parent="parentGetEvent"
      @child-input="getDynamicData"
    />
    <!-- 복붙하면 재사용성! 바닐라 자스는 골치아픈데, 뷰는 이렇게 쉽게 됨! -->
    
    <!-- props 내려주기 (정적) -->
    <!-- 동적으로 내려줄 수도 있음 (v-bind 사용) : 부모 컴포넌트의 데이터가 업데이트 되면 자식 컴포넌트로 전달되는 데이터 또한 업데이트 됨 -->
    <!-- <a href="url"></a> : 문자열 url을 받음 -->
    <!-- <a :href="url"></a> : url 주소를 받음 -->
    <!-- 
      <SomeComponent num-props="1"/> : 문자열 1 받음
      <SomeComponent :num-props="1"/> : 숫자 1 받음
    -->
    <!-- 단방향 데이터 흐름 -->
    <!--  모든 props는 부모에서 자식으로 즉 아래로 단방향 바인딩을 형성 -->
    <!--  부모 속성이 업데이트되면 자식으로 흐르지만 반대 방향은 아님 -->
    <!--    부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 prop들이 최신 값으로 새로고침 됨 -->
    <!--  목적 -->
    <!--    하위 컴포넌트가 실수로 상위 컴포넌트 상태를 변경하여 앱의 데이터 흐름을 이해하기 힘들게 만드는 것을 방지 -->
    <!--  하위 컴포넌트에서 prop를 변경하려고 시도해서는 안되며 그렇게 하면 Vue는 콘솔에서 경고를 출력함 -->
    
    <!-- emit event : 아래에서 위로 갈 때는 소리를 쳐야 함, 부모가 청취해야 함 -->
    <!-- e3. 청취 후 parentGetEvent 함수 실행 -->
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'

export default {
  name: 'MyComponent', // 1. 이름 설정(이름(PascalCase)을 지어줘야 상위 컴포넌트가 가져갈 수 있음(파일명 인식 못함, 이름을 인식함))
  // vue 공식문서 확인
  //  베이스 컴포넌트 이름 : 앞에 Base 붙여라
  //  싱글 인스턴스 컴포넌트 이름(하위로 들어가지 않는 컴포넌트라면) : 앞에 The를 사용하라 
  //  컴포넌트간 강한 연관성이 있다면 : 이름을 이어가라 (MyComponent-MyComponentItem)
  // data: {
  //   url: 'www.naver.com'
  // },
  components: {
    // 2. 등록하기
    MyComponentItem,
  },
  data: function () { // vue-cli에서는 data를 return값으로 받아야 함 // 각 vue인스턴스는 같은 data 객체를 공유하므로 새로운 data 객체를 반환(return)하여 사용해야 함 // 이렇게 안하면 에러남(큰 고민하지 말고 이렇게 해!)
    return {
      dynamicProps: '이건 동적인 데이터!', // 이게 바뀌면 위에도 바뀌고 자식도 바뀌고 // 동적이 8할 이상!
    }
  },
  methods: {
    // e4. parentGetEvent 함수 실행
    parentGetEvent: function (childeData) { // 데이터를 여기에 인자로 넣어줌
      console.log('자식 컴포넌트에서 발생한 이벤트!')
      console.log(childeData)
      // this.$emit('name', childeData) // 또 소리치면 또 위로
    },
    getDynamicData: function (childInputData) { // 걍 변수 입력해주면 됨
      console.log(`사용자가 입력한 값은 ${childInputData}입니다.`) // 작은따옴표 아니고!
    }
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>

<!-- 1. 파일 만들기 -->
<!-- 2. 이름 설정 -->
<!-- 3. template 요소 추가(templates 안에 최상위 태그 단 한 개(비어있어도 안됨) 추가, SPC 때문?) -->

