<template>
  <div>
    <div id="at_box">
    <h3>게시물을 수정해주세요</h3>
    <div class="a_right">
      <div id="c_button">
        <router-link :to="{ name: 'article_detail', params: { id: articleId } }" style="text-decoration: none;">
        <v-btn id="btn" type="submit" rounded="sm" block size="x-large" color="#2962FF" >
            뒤로가기
        </v-btn></router-link>
      </div>
    </div>


    <form @submit.prevent="updateArticle">
      <input type="text" id="r_content" v-model="form.title"
        placeholder="제목을 입력해주세요" /><br />
      <br />
      <textarea id="r_content" cols="30" rows="10" v-model="form.content"
      placeholder="내용을 입력해주세요"></textarea>

      <div>
        <v-btn rounded="sm" color="#FFF176">
          <button type="submit">UPDATE</button>
        </v-btn>
      </div>
    </form>

  </div>
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
          this.$router.push({ name: "article_detail", params: { id: this.articleId } });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
#at_box{
  /* text-align: left; */
  border: 2px solid rgb(250, 213, 132);
  margin: 15px;
  padding: 15px;
  border-radius: 20px;
  font-family: 'NanumSquareRound';
}


#r_content{
  width: 60%;
  height: 70%;
  text-align: left;
  border: 2px solid rgb(250, 213, 132);
  margin: 5px;
  padding: 15px;
  border-radius: 10px;
}
div{
  font-family: 'NanumSquareRound';
}
h3{
  margin: 10px;
  color: rgb(68, 68, 68);
}

#c_button{
  width:90px;
  color: white;
}

#btn{
  color: white;
}

.a_right {
  width: 100%;
  display: flex;
  justify-content: end;
  padding:10px
}
</style>