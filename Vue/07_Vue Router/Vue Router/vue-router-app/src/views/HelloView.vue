<template>
  <div>
    <h1>hello, {{ userName }} </h1>
  </div>
</template>

<script>
export default {
  name: 'HelloView',
  data() {
    return {
      userName: this.$route.params.userName
    }
  },
  // $route.params로 변수에 접근 가능
  // 다만 HTML에서 직접 사용하기 보다는 data에 넣어서 사용하는 것을 권장
  beforeRouteUpdate(to, from, next) {
    this.userName = to.params.userName
    next()
  }
}
</script>

<style>

</style>