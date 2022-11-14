<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>글 제목 : {{ article?.title }}</p>
    <p>글 내용 : {{ article?.content }}</p>
    <!-- <p>글 작성시간 : {{ article?.createdAt }}</p> -->
    <p>글 작성시간 : {{ articleCreatedAt }}</p>
    <!-- optional chaining(?.) -->
    <!-- article이 null이면 에러 발생하는 게 아니라 undefined를 반환 -->
    <button @click="deleteArticle">삭제</button>
    <router-link :to="{ name: 'index' }">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  name: 'DetailView',
  data() {
    return {
      article: null,
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
    articleCreatedAt() { 
      const article = this.article
      const createdAt = new Date(article?.createdAt).toLocaleString() // 로컬시간으로 바꿔줌
      return createdAt
    }
  },
  methods: {
    getArticleById(id) {
      // const id = this.$route.params.id // url로 들어오는 건 문자열
      for (const article of this.articles) {
        if (article.id === Number(id)) {
          this.article = article // data에 있는 article을 찾은 article로 바꿔줘
          break
        }
      }
      if (this.article === null) {
        this.$router.push({ name: 'NotFound404' })
      }
    },
    deleteArticle() {
      this.$store.commit('DELETE_ARTICLE', this.article.id)
      this.$router.push({ name: 'index' }) // 삭제 후 index로 보내줌
    }
  },
  // URL 들어가자마자 호출
  created() { 
    this.getArticleById(this.$route.params.id)
  }
}
</script>

<style>

</style>