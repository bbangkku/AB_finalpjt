<template>
  <div>
    <div id="at_box">
      <h3>게시물을 작성해주세요</h3>
      <div class="a_right">
        <div id="c_button">
          <router-link :to="{ name: 'article_view' }" style="text-decoration: none;">
          <v-btn id="btn" type="submit" rounded="sm" block size="x-large" color="#2962FF" >
              뒤로가기
          </v-btn></router-link>
        </div>
      </div>
      
      <form @submit.prevent="createArticle">
        <input type="text" id="r_content" v-model.trim="title"
          placeholder="제목을 입력해주세요" /><br />
        <br />
        <textarea id="r_content" cols="30" rows="10" v-model="content"
        placeholder="내용을 입력해주세요"></textarea>

        <div>
          <v-btn rounded="sm" color="#FFF176">
            <button type="submit">CREATE</button>
          </v-btn>
        </div>
      </form>
      </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CreateView",
  data() {
    return {
      title: null,
      content: null,
    };
  },
  methods: {
    createArticle() {
      const title = this.title;
      const content = this.content;
      if (!title) {
        alert("제목 입력해주세요");
        return;
      } else if (!content) {
        alert("내용 입력해주세요");
        return;
      }
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/api/v1/articles/`,
        data: { title, content },
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
  },
};
</script>

<style scoped>
.a_right {
  width: 100%;
  display: flex;
  justify-content: end;
  padding:10px
}

h3{
  margin: 10px;
  color: rgb(68, 68, 68);
}

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

#c_button{
  width:90px;
  color: white;
}

#btn{
  color: white;
}
</style>
