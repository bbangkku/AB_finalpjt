<template>
  <div>
    <div v-if="check(comment)">
      <!-- {{ comment.article }} -->
      <p>{{comment.id}}번댓글</p>
      <p>{{ comment.content.content }}</p>
      <p>유저 : {{ comment?.username }}</p>
      <br>
      <form @submit.prevent="editComment(comment)" v-if="isEditing && isUserAuthorized(comment)">
        <button type="submit">수정</button>
      </form>
      <form @submit.prevent="deleteComment(comment)" v-if="isEditing && isUserAuthorized(comment)">
        <button type="submit">삭제</button>
      </form>
<br>
      <hr />
      <input
        type="text"
        v-model="form.updateContent"
        v-if="!isEditing && $store.state.loginUser.username === comment.username"
      />

      <form @submit.prevent="updateComment(comment)" v-if="!isEditing && isUserAuthorized(comment)">
        <button type="submit" >확인</button>
      </form>
      </div>
    </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommentListItem",
  
  data() {
    return {
      form: {
        commentContent: "", // 댓글 내용
        content: "",
        updateContent:""
      },
      isEditing: true,
    };
  },
  props: {
    comment: Object
  },
  computed: {

  },
  methods: {
    check(comment) {
      // console.log(comment.id, "asdasdas");
      // console.log(this.$route.params.id, "asdasd");
      return comment.article == this.$route.params.id ? true : false;
    },
    isUserAuthorized(comment) {
      return comment.username === this.$store.state.loginUser.username;
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
          this.comments = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
   editComment(comment) {
      this.isEditing = false;
      this.form.updateContent = comment.content;

      // this.$set(comment, "isEditing", true);
    },
    updateComment(comment) {
      const data = {
        content: this.form.updateContent,
        username: comment.username,
        id: comment.id
      };
      this.$emit('comment-updated', data)
      axios({
        method: "put",
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/${comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: data,
      })
        .then(() => {
          this.isEditing = true;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteComment(comment) {
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/${comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log("댓글삭제", res);
          this.getComments();
          // 스토어에있는거지우거나, getcomments를하거나
          // this.$router.go(this.$router.currentRoute);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style></style>
