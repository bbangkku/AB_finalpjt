<template>
  <div class="comment-list">
    <!-- <ul>
      <CommentListItem
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"
      />
    </ul> -->
    <!-- {{comments}} -->
    <div v-for="comment in comments" :key="comment.id">
      <!-- 커멘트에 유저아이디 갖고오는거구현, -->
      <p>{{ comment.content }}</p>
      <p>유저 : {{ comment.username }}</p>

      <form @submit.prevent="editComment(comment)" v-if="isEditing && isUserAuthorized(comment)">
        <button type="submit">수정</button>
      </form>
      <form @submit.prevent="deleteComment(comment)" v-if="isEditing && isUserAuthorized(comment)">
        <button type="submit">삭제</button>
      </form>

      <hr />
      <input
        type="text"
        v-model="comment.updateContent"
        v-if="!isEditing && $store.state.loginUser.username === comment.username"
      />

      <form @submit.prevent="updateComment(comment)" v-if="!isEditing && isUserAuthorized(comment)">
        <button type="submit">확인</button>
      </form>

    </div>
    
    <form @submit.prevent="submitComment">
      <input id='r_comment' v-model="commentContent" type="text"
        placeholder="댓글을 입력해주세요">
      <button type="submit">댓글 작성</button>
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
      comments: [], // 댓글 목록
      commentContent: "", // 댓글 내용
      isEditing: true,
    };
  },
  computed: {

  },
  components: {
    // CommentListItem,
  },
  created() {
    this.getArticleDetail()
    this.getComments()
  },

  methods: {
    isUserAuthorized(comment) {
      console.log(comment)
      return (
        comment.username === this.$store.state.loginUser.username
      );
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
          const comments = res.data;
          console.log(comments)
          // console.log("rasdsadad", res.data);
          // const commentss = comments.map((comment) => {return false} );
          // console.log(commentss)
        })


        .catch((err) => {
          console.log(err);
          
          this.comments = [];
        });
    },
    submitComment() {
      const commentData = {
        username: this.$store.state.loginUser.username,
        article: this.article.id,
        nickname: this.$store.state.loginUser.nickname,
        content: this.commentContent,
        userid: this.$store.state.userid,
      };
      axios({
        method: "post",
        url: `${API_URL}/api/v1/articles/${this.article.id}/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: commentData,
      })
        .then((res) => {
          console.log(res);
          this.commentContent = '';
          this.getComments();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    editComment(comment) {
      console.log('111112222')
      this.isEditing = false;
      comment.updateContent = comment.content;
      // this.$set(comment, "isEditing", true);
    },
    updateComment(comment) {
      const data = {
        content: comment.updateContent,
        username: comment.username
      };
      axios({
        method: "put",
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/${comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: data,
      })
        .then(() => {
          comment.content = comment.updateContent;
          this.isEditing = true;
          console.log(comment,'이게커멘튼데')
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
          console.log('댓글삭제',res);
          this.getComments();
          // 스토어에있는거지우거나, getcomments를하거나
          // this.$router.go(this.$router.currentRoute);
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

<style scoped>
.article-list {
  text-align: start;
}

#r_comment{
  width: 60%;
  height: 40px;
  text-align: left;
  border: 2px solid rgb(250, 213, 132);
  margin: 15px;
  padding: 15px;
  border-radius: 20px;
}
</style>
