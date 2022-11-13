<template>
  <div>
    <button @click="getDogImage">멍멍아 이리온</button><br><br>
    <img v-if="imgSrc" :src="imgSrc" alt="#"><br>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  name:'DogComponent',
  data() {
    return {
      imgSrc: null,
    }
  },
  methods:{
    getDogImage() {
      const dogImageSearchURL = 'https://dog.ceo/api/breeds/image/random'
      
      axios({
        method: 'get',
        url: dogImageSearchURL
      })
        .then((response) => {
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }, 
  created() { // created 시점에 호출하기 때문에 시작할 때 버튼 누르지 않아도 바로 사진 뜨게됨 (뷰의 일생일생에 끼어들게 됨)
    this.getDogImage()
    console.log('Child created!')
    // const button = document.querySelector('button')
    // button.innerText = '멍멍!'
    // => DOM 조작 불가능!!

    // axios와 같이 사용하게 됨
  },
  mounted() { // DOM에 대한 조작이 가능하다 (created는 안됨)
    const button = document.querySelector('button')
    button.innerText = '멍멍!'
    console.log('Child mounted!')
  },
  updated() {
    console.log('새로운 멍멍이!')
    console.log('Child updated!')
  }
  // Lifecycle Hooks 특징
  //  Lifecycle Hooks는 컴포넌트별로 정의할 수 있음
  //  현재 해당 프로젝트는 
  //    App.vue 생성 => ChildComponent 생성 => ChildComponent 부착 => App.vue 부착 => ChildComponent 업데이트 순으로 동작한 것
  //    App created! => Child created! => Child mounted! => App mounted!
}
</script>

<style>

</style>
