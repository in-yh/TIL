<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle" action="">
      <input type="text" v-model.trim="title"><br>
      <textarea v-model.trim="content"></textarea>
      <input type="submit">
    </form>
    <router-link :to="{ name: 'index' }">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      const payload = {
        title, content
      }
      this.$store.dispatch('createArticle', payload)
      // 게시글 작성 후 index 페이지로 가게 함
      this.$router.push({ name: 'index' })
    }
  }
}
</script>

<style>

</style>