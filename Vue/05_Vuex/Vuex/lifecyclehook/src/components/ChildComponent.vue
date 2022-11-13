<template>
  <div>
    value : {{ value }}
    <button @click="changeValue">change value</button><br>
  </div>
</template>

<script>
export default {
  name:'ChildComponent',
  data() {
    return {
      value: 0,
    }
  },
  methods: {
    changeValue() {
      this.value = this.value + 1
    }
  },
  // beforeCreate() {
  //   console.log('beforeCreate')
  // },
  // created() {
  //   console.log('created')
  // },
  // beforeMount() {
  //   console.log('beforeMount')
  // },
  // mounted() { // 생성되면 여기까지 실행
  //   console.log('mounted')
  // },
  // beforeUpdate() { // 수정될 때
  //   console.log('beforeUpdate')
  // },
  // updated() {
  //   console.log('updated')
  // },
  // beforeDestroy() { // 삭제될 때
  //   console.log('beforeDestroy')
  // },
  // destroyed() {
  //   console.log('destroyed')
  // }
}

// created
//  Vue instance가 생성된 후 호출됨
//  data, computed 등의 설정이 완료된 상태
//  서버에서 받은 데이터를 vue instance의 data에 할당하는 로직을 구현하기 적합
//  단, mount되지 않아 요소에 접근할 수 없음!!

// mounted
//  Vue instance가 요소에 mount된 후 호출됨
//  mount된 요소를 조작할 수 있음

// updated
//  데이터가 변경되어 DOM에 변화를 줄 떄 호출됨
</script>

<style>

</style>
