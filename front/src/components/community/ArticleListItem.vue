<template>
  <div id="at_box">
    <div id="at_box2">
      <h3>Number. {{ article.id }}</h3>
      <p>작성자 : {{ article.nickname }}</p>
    </div>
    <router-link
      :to="{
        name: 'article_detail',
        params: { id: article.id },
      }"
    >
      <button>
        <h2>TITLE : {{ article.title }}</h2>
      </button>
    </router-link>
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

<style scoped>
#at_box {
  border: 2px solid rgb(250, 213, 132);
  margin: 15px;
  padding: 20px;
  border-radius: 20px;
  font-family: "NanumSquareRound";
}
#at_box2 {
  display: flex;
  justify-content: space-between;
  font-family: "NanumSquareRound";
}

h3 {
  margin: 8px;
}

h2 {
  color: black;
  margin: 8px;
}
</style>
