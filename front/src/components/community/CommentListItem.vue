<template>
  <div>
    <div v-if="check(comment)">
      <div class='comment_box'>
        <p>No.{{comment.id}}</p>
        
        <div class="c_box">
          <h4>{{ comment?.username }} : {{ comment.content }}</h4>
          <!-- <div class="a_right"> -->
            <div id="c_button1">
              <div id="c_button">
              <form @submit.prevent="editComment(comment)" v-if="isEditing && isUserAuthorized(comment)">
                <v-btn id="btn" type="submit" rounded="sm" block size="x-large" color="#3F51B5">
                  수정
                </v-btn>
              </form>
            </div>

            <div id="c_button">
              <form @submit.prevent="deleteComment(comment)" v-if="isEditing && isUserAuthorized(comment)">
                <v-btn id="btn" type="submit" rounded="sm" block size="x-large" color="#EF5350">
                  삭제
                </v-btn>
              </form>
            </div>
            </div>
         
          <!-- </div> -->
        </div>
      </div>
      <hr />
      <!-- 수정창 -->
      <div class="up_box">
        <form @submit.prevent="submitComment">
          <input id='r_comment' v-model="form.updateContent" type="text"
          v-if="!isEditing && $store.state.loginUser.username === comment.username"
            placeholder="댓글을 입력해주세요">
        </form>

        <form @submit.prevent="updateComment(comment)" v-if="!isEditing && isUserAuthorized(comment)">
          <v-btn id="btn1" type="submit" rounded="sm" block size="x-large" color="#FFF176">
                확인
          </v-btn>
        </form>        
      </div>

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
  created(){
    this.getArticles();
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
          console.log("또가져와")
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
      }

      this.$emit('comment-updated', JSON.stringify(data))
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
          console.log('가져와')
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

<style scoped>
.up_box{
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

div{
  font-family: 'NanumSquareRound';
  font-weight: lighter;
}

.comment_box{
  padding: 10px;
}

.a_right {
  width: 100%;
  display: flex;
  justify-content: end;
}
#c_button{
  width: 100px;
  margin: 5px;
  /* margin: 0px 30px 0px 30px; */
  font-weight: 700;
  align-content: right;
}

#c_button1{
  display: flex;
}

#btn{
  color: white;
}
#btn1{
  color: black;
  margin: 15px
}
.c_box{
  display: flex;
  justify-content:space-between;
}
h4{
  margin: 5px;
}
</style>
