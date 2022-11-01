<template>
  <!-- HTML -->
  <div>
    <p>Hello :)</p>
  </div>
</template>

<script>
  // JavaScript
</script>

<style>
  /* CSS */
  p {
    color: black;
  }
</style>

// v-for는 항상 key와 함께 사용하기
//  내부 컴포넌트의 상태를 일관되게 유지하기 위해 v-for에 항상 key를 사용하기
//  데이터의 예측 가능한 행동을 유지 시키기(객체 불변성)
// v-for를 쓴 element에 절대 v-if를 사용하지 말기