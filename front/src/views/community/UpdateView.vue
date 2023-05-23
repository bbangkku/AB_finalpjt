UpdateView.vue

<template>
  <div>
    <h1>Edit Article</h1>
    <form @submit.prevent="updateArticle">
      <div>
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="form.title" />
      </div>
      <div>
        <label for="content">Content:</label>
        <textarea id="content" v-model="form.content"></textarea>
      </div>
      <button type="submit">Update</button>
      <router-link :to="{ name: 'ArticleDetailView', params: { id: articleId } }">Cancel</router-link>
    </form>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "UpdateView",
  data() {
    return {
      form: {
        title: "",
        content: "",
      },
      articleId: null,
    };
  },
  created() {
    this.getArticleDetail();
  },
  methods: {
    getArticleDetail() {
      this.articleId = this.$route.params.id;
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/${this.articleId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.form.title = res.data.title;
          this.form.content = res.data.content;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updateArticle() {
      axios({
        method: "put",
        url: `${API_URL}/api/v1/articles/${this.articleId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: {
          title: this.form.title,
          content: this.form.content,
        },
      })
        .then((res) => {
          console.log(res);
          this.$router.push({ name: "ArticleDetailView", params: { id: this.articleId } });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

