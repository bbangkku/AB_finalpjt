ArticleListView.vue

<template>
  <div>
    <h5>{{ article.id }} 번 게시글</h5>
    <p>작성자 : {{ article.username }}</p>
    <p>제목 : {{ article.title }}</p>
    <router-link
      :to="{
        name: 'article_detail',
        params: { id: article.id },
      }"
    >

      [DETAIL]
    </router-link>
    <hr />
  </div>
</template>

<script>
export default {
  name: "ArticleListItem",

  props: {
    article: Object,
  },
};
</script>

<style></style>
