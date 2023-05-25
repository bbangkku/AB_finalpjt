<template>
  <div class="comment-list">
    <ul>
    <!-- {{comments}} -->
      <CommentListItem
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"
        @comment-updated="updateCommentContent"
      />
    </ul>
    <form @submit.prevent="submitComment">
      <div id="a">
        <input id='r_comment' v-model="commentContent" type="text"
        placeholder="댓글을 입력해주세요">
        <div id="c_button">
          <v-btn id="btn1" type="submit" rounded="sm" block size="x-large" color="#FFF176" >
              댓글 작성
        </v-btn>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import CommentListItem from "@/components/community/CommentListItem";
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
    CommentListItem
  },
  created() {
    this.getArticleDetail()
    this.getComments()
  },

  methods: {
    check(comment) {
      // console.log(comment.id, "asdasdas");
      // console.log(this.$route.params.id, "asdasd");
      return comment.article == this.$route.params.id ? true : false;
    },
    isUserAuthorized(comment) {
      // console.log(comment)
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
          this.comments = res.data;
          console.log(this.comments,'comments')
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
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: commentData,
      })
        .then((res) => {
          console.log('submit',res);
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
    updateCommentContent(updatedContent) {
      const index = this.comments.findIndex(comment => comment.id===updatedContent.id)
      if(index !== -1){
        this.comments[index].content = updatedContent
      }
    }
    ,
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

#a{
  display: flex;

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

#c_button{
  width: 100px;
  margin: 5px;
  margin-top:15px;
  /* margin: 0px 30px 0px 30px; */
  font-weight: 700;
  align-content: right;
}
</style>
