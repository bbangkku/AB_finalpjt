<template>
  <div>
    <h1>COMMUNITY</h1>
    <!-- {{ $store.state.loginUser.nickname }}님 안녕하세요 -->
    <div id="c_button">
      <v-btn rounded="sm" block size="x-large" color="#FFF176">
        <router-link :to="{ name: 'article_create' }">CREATE</router-link>
      </v-btn>
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

<style>
#c_button{
  width: 100px;
  display: inline-block;
  align-content: right;
  text-align: right;
  align-self: right;
  /* float: right; */
}
</style>
