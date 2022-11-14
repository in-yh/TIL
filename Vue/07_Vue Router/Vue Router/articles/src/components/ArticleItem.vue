<template>
  <div @click="goDetail(article.id)"> 
    <!-- article.id를 인자로 받음 -->
    <p>글 번호 : {{ article.id }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object,
  },
  methods: {
    goDetail(id) {
      this.$router.push({ name: 'detail', params: {id} })
      // this.$router.push({ name: 'detail', params: {id: `${this.article.id}`} })
    }
  }
}
</script>

<style>

</style>