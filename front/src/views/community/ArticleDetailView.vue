ArticleDetailView.vue
<template>
  <div>
    <h1>Detail</h1>
    <!-- {{this.$store.state.articles}} -->
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <hr />
    <router-link :to="{ name: 'article_view' }">뒤로가기</router-link>
    <button v-if="isUserAuthorized" @click="deleteArticle">삭제</button>
    <button v-if="isUserAuthorized" @click="updateView">수정</button>

    <h2>댓글</h2>
    <CommentList :comments="comments" />
    <br />
    <br />
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
import CommentList from "@/components/community/CommentList.vue";

export default {
  name: "ArticleDetailView",
  components: {
    CommentList,
  },

  data() {
    return {
      article: [],
      comments: [], // 댓글 목록
      commentContent: "", // 댓글 내용
      isEditing: false,
    };
  },
  created() {
    console.log(this.$store.state.token);
    this.getArticleDetail();
    this.getComments();
  },
  computed: {
    isUserAuthorized() {
      return (
        this.article && this.article.username === this.$store.state.username
      );
    },
  },
  methods: {
    getArticleDetail() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.article = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteArticle() {
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.$router.push({ name: "ArticleView" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updateView() {
      this.$router.push({
        name: "UpdateView",
        params: {
          id: this.article.id,
          title: this.article.title,
          content: this.article.content,
        },
      });
    },
    getComments() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log("rasdsadad", res.data);
          this.comments = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // submitComment() {
    //   console.log("12333333제출");
    //   console.log(this.isEditing, "111111111111111");
    //   const commentData = {
    //     article: this.article.id,
    //     user: this.$store.state.username,
    //     content: this.commentContent,
    //     userid: this.$store.state.userid,
    //   };
    //   console.log("axios로보냄", commentData);
    //   axios({
    //     method: "post",
    //     url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/`,
    //     headers: {
    //       Authorization: `JWT ${this.$store.state.token}`,
    //     },
    //     data: commentData,
    //   })
    //     .then((res) => {
    //       console.log(res);
    //       this.$router.go(this.$router.currentRoute);
    //       // location.reload()
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //     });
    // },
    // editComment(comment) {
    //   console.log(this.isEditing);
    //   this.$set(comment, "isEditing", true);
    //   comment.updateContent = comment.content;
    //   console.log(this.isEditing);
    // },
    // updateComment(comment) {
    //   const data = {
    //     content: comment.updateContent,
    //   };
    //   console.log("dddddd", comment.id);
    //   axios({
    //     method: "put",
    //     url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/${comment.id}/`,
    //     headers: {
    //       Authorization: `JWT ${this.$store.state.token}`,
    //     },
    //     data: data,
    //   })
    //     .then((res) => {
    //       console.log(res);
    //       comment.content = comment.updateContent;
    //       comment.isEditing = false;
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //     });
    // },
  },
};
</script>
