<template>
  <div>
    <div id="at_box">
      <h3>게시물을 작성해주세요</h3>
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
</style>
