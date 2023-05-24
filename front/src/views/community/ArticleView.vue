<template>
  <div>
    <h1>COMMUNITY</h1>
    <div class="a_right">
      <div id="c_button">
        <v-btn rounded="sm" block size="x-large" color="#FFF176">
          <router-link id="r_btn" :to="{ name: 'article_create' }" style="text-decoration: none;">CREATE</router-link>
        </v-btn>
      </div>
    </div>

    <div>
      <ArticleList />
    </div>
    <hr />
  </div>
</template>

<script>
import ArticleList from "@/components/community/ArticleList.vue";
import Swal from 'sweetalert2'

export default {
  name: "ArticleView",
  components: {
    ArticleList,
  },
  data() {
    return {
      user: this.$store.state.loginUser.nickname,
    };
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin; // 로그인 여부
    },
  },
  created() {
    this.getArticles();
  },
  methods: {
  getArticles() {
    if (this.isLogin) {
      this.$store.dispatch("getArticles");
    } else {
      Swal.fire({
        title: "로그인이 필요한 페이지입니다",
        icon: "error",
        confirmButtonText: "확인",
      }).then(() => {
        this.$router.push({ name: "login" });
      });
    }
  },
}
};
</script>

<style scoped>
.a_right {
  width: 100%;
  display: flex;
  justify-content: end;
}
#c_button{
  width: 100px;
  margin: 0px 30px 0px 30px;
  font-weight: 700;
  align-content: right;
}

#r_btn{
  color: black
}

div{
  font-family: 'NanumSquareRound';
}
</style>
