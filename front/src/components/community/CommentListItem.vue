<template>
  <div></div>
  <!-- <li>
    <div>{{ comment.user }}</div>
    <div>{{ comment.content }}</div>
    <div>{{ comment.created_at }}</div>
    <button v-if="isUserAuthorized" @click="deleteComment">삭제</button>
    <button v-if="isUserAuthorized" @click="updateComment">수정</button>

  </li> -->
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommentListItem",
  data() {
    return {
      form: {
        content: "",
      },
      commentId: "",
    };
  },
  props: {
    comment: {
      type: Object,
    },
  },
  computed: {
    isUserAuthorized() {
      console.log("커멘트", this.comment.id);
      console.log("상태", this.$store.state);

      return this.comment && this.comment.user === this.$store.state.userid;
    },
  },
  methods: {
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
    deleteComment() {
      console.log(this.$route.params.id);
      console.log(this.comment.id);
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/${this.comment.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res);
          this.getComments(); // 댓글 목록을 다시 가져옴
          location.reload();
          this.$router.replace({
            name: "ArticleDetailView",
            params: { id: this.$route.params.id },
          });
        })

        .catch((err) => {
          console.log(err);
        });
    },
    updateComment(commentId) {
      this.$router.push({
        name: "UpdateComment",
        params: {
          articleid: this.article.id,
          commendId: commentId,
        },
      });
    },
  },
};
</script>

<style></style>
