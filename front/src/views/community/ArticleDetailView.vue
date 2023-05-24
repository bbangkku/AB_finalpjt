ArticleDetailView.vue
<template>
  <div>
    <!-- <h1>Detail</h1> -->
    <div id="at_box">
      <!-- {{this.$store.state.articles}} -->
      <div id="at_box2">
        <h4>Number : {{ article?.id }}</h4>
        <router-link :to="{ name: 'article_view' }">
          <button>뒤로가기</button></router-link>
      </div>
      <h2>TITLE : {{ article?.title }}</h2>
      <hr>
      <h3>CONTENT </h3>
      <h4>{{ article?.content }}</h4>
      <div id="at_box3">
        <h5>WRITE TIME : {{ article?.created_at }}</h5>
        <h5>UPDATE TIME : {{ article?.updated_at }}</h5>
      </div>
      
      <button v-if="isUserAuthorized" @click="deleteArticle">삭제</button>
      <button v-if="isUserAuthorized" @click="updateView">수정</button>
    </div> 

    <div id="at_box">
      <h3>COMMENT BOX</h3>
      <hr>
      <div>
        <CommentList/>
      </div>
      
    </div>
    
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
      commentContent: "", // 댓글 내용
      isEditing: false,
    };
  },
  created() {
    this.getArticleDetail();
  },
  computed: {
    isUserAuthorized() {
      return (
        this.article && this.article.username === this.$store.state.loginUser.username
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
          this.$router.push({ name: "article_view" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updateView() {
      this.$router.push({
        name: "article_update",
        params: {
          id: this.article.id,
          title: this.article.title,
          content: this.article.content,
        },
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

<style scoped>
#at_box{
  text-align: left;
  border: 2px solid rgb(250, 213, 132);
  margin: 15px;
  padding: 15px;
  border-radius: 20px;
}
#at_box2{
  display: flex;
  justify-content: space-between;
}
#at_box3{
  text-align: right;
}

h3, h2, h4{
  margin: 10px;
}
</style>