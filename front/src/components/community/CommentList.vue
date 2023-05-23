<template>
  <div class="comment-list">
    <!-- <ul>
      <CommentListItem
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"
      />
    </ul> -->
    <div v-for="comment in comments" :key="comment.id">
      <!-- 커멘트에 유저아이디 갖고오는거구현, -->
      {{ comment }}
      <p>{{ comment.content }}</p>
      <p>유저 : {{ comment.username }}</p>
      <button
        @click="editComment(comment)"
        v-if="isEditing && $store.state.loginUser.username === comment.username"
      >
        수정
      </button>
      <p v-if="isUserAuthorized">유저권한있</p>
      <hr />
      <input
        type="text"
        v-model="comment.updateContent"
        v-if="comment.isEditing"
      />
      <button @click="updateComment(comment)" v-if="comment.isEditing">
        확인
      </button>
    </div>
    <h3>댓글 작성</h3>
    <form>
      <textarea v-model="commentContent" rows="4" cols="50"></textarea>
      <button type="submit" @click="submitComment()">댓글 작성</button>
      <!-- 댓글수정 -->
    </form>
  </div>
</template>

<script>
// import CommentListItem from "@/components/community/CommentListItem";
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
  name: "CommentList",
  data() {
    return {
      article: null,
      // comment: [], // 댓글 목록
      commentContent: "", // 댓글 내용
      isEditing: true,
    };
  },
  computed: {
    isUserAuthorized() {
      return (
        this.comment && this.comment.data.user === this.$store.state.userid
      );
    },
  },
  components: {
    // CommentListItem,
  },
  created() {
    this.getArticleDetail();
  },
  props: {
    comments: {
      type: Array,
    },
  },
  methods: {
    submitComment() {
      event.preventDefault(); // 기본동작막기
      const commentData = {
        username: this.$store.state.loginUser.username,
        article: this.article.id,
        nickname: this.$store.state.loginUser.nickname,
        content: this.commentContent,
        userid: this.$store.state.userid,
      };
      console.log(this.$store.state.loginUser.nickname);
      axios({
        method: "post",
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: commentData,
      })
        .then((res) => {
          console.log(res);
          this.$router.go(this.$router.currentRoute);
          // location.reload()
        })
        .catch((err) => {
          console.log(err);
        });
    },
    editComment(comment) {
      this.isEditing = false;
      comment.updateContent = comment.content;
      // this.$set(comment, "isEditing", true);
    },
    updateComment(comment) {
      const data = {
        content: comment.updateContent,
      };
      console.log("asdas", data);
      axios({
        method: "put",
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/${comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: data,
      })
        .then((res) => {
          console.log(res);
          comment.content = comment.updateContent;
          comment.isEditing = false;
        })
        .catch((err) => {
          console.log(err);
        });
    },
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
          console.log("11111", this.article);
          console.log("222222", this.$store.state);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
.article-list {
  text-align: start;
}
</style>
