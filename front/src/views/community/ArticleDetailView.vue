<template>
  <div>
    <div id="at_box">
      <div id="at_box2">
        <div>
          <h4>Number : {{ article?.id }}</h4>
          <h2>TITLE : {{ article?.title }}</h2>
          <h2>작성자 : {{article?.nickname}}</h2>
        </div>
        <div id="c_button">
          <router-link :to="{ name: 'article_view' }" style="text-decoration: none;">
          <v-btn id="btn1" type="submit" rounded="sm" block size="x-large" color="#FFF176" >
              뒤로가기
          </v-btn></router-link>
        </div>
      </div>
      
      <hr>
      <h3>CONTENT </h3>
      <h4>{{ article?.content }}</h4>
      <div id="at_box3">
        <h5>WRITE TIME : {{ article?.created_at }}</h5>
        <h5>UPDATE TIME : {{ article?.updated_at }}</h5>
      </div>
      
      <div class="c_box">
          <div class="a_right">
            <div id="c_button">
                <v-btn id="btn" 
                  v-if="isUserAuthorized" @click="updateView"
                  type="submit" rounded="sm" block size="x-large" color="#3F51B5">
                  수정
                </v-btn>
            </div>

            <div id="c_button">
                <v-btn id="btn" 
                v-if="isUserAuthorized" @click="deleteArticle"
                type="submit" rounded="sm" block size="x-large" color="#EF5350">
                  삭제
                </v-btn>
            </div>
          </div>
        </div>
      
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
  font-family: 'NanumSquareRound';
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

#btn{
  color: rgb(248, 248, 248);
  font-weight: 700;
  text-decoration: none;
}

#btn1{
  color: rgb(58, 57, 57);
  font-weight: 700;
  text-decoration: none;
}

.a_right {
  width: 100%;
  display: flex;
  justify-content: end;
}

#c_button{
  width: 100px;
  margin: 5px;
  margin-top:10px;
  /* margin: 0px 30px 0px 30px; */
  font-weight: 700;
  align-content: right;
}
</style>