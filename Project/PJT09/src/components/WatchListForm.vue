<template>
  <div>
    <input 
      @keyup.enter.prevent="addMovie" 
      type="text"
      v-model="inputData"
    >
    <button @click.prevent="addMovie" type="submit">Add</button>
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data() {
    return {
      inputData: '', 
      // watchList: [],
    }
  },
  methods: {
    addMovie() {
      // this.watchList.push(this.inputData) // 리스트에 넣을 때 push
      // console.log(this.watchList)
      this.$store.dispatch('addMovie', this.inputData)
      this.inputData = '' // 인풋 데이터 초기화
    }
  },
}
</script>

<style>

</style>