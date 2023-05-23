ArticleView.vue

<template>
  <div>
    <h1>커뮤니티</h1>
    {{ user }}님 안녕하세요
    <br/>
    <router-link class="nav-link" @click.native="logout" to="#"
      >로그아웃</router-link
    >
    <hr />
    <div>
      <router-link :to="{ name: 'article_create' }">[CREATE]</router-link>
      <ArticleList />
    </div>
    
    <hr />
  </div>
</template>

<script>
import ArticleList from "@/components/community/ArticleList.vue";
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
    // 게시글 가져오기
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch("getArticles");
      } else {
        alert("로그인이 필요한 페이지입니다...");
        this.$router.push({ name: "login" });
      }
    },
    // 로그아웃
    logout() {
      this.$store.dispatch("logout");
    },
  },
};
</script>

<style></style>
