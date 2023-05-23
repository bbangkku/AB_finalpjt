<template>
  <div id="app">
      <!-- <v-tabs show-arrows v-model="tab" color="deep-purple-accent-4" align-tabs="center"> -->
        <v-card class="custom-card">
      <v-tabs
      fixed-tabs
      bg-color="teal-darken-3"
      slider-color="teal-lighten-3"
      v-model="tab"
      align-tabs="center"
      show-arrows
    >
        <v-tab to="/">Home</v-tab>
        <v-tab to="/deposit">예금/적금 비교</v-tab>
        <v-tab to="/map">은행찾기</v-tab>
        <v-tab to="/exchange">환율계산기</v-tab>
        <v-tab to="/community">게시판</v-tab>
        <v-tab to="/profile">프로필</v-tab>
        <v-tab to="/login" v-if="!isLogin">로그인</v-tab>
        <v-tab @click="logout" v-if="isLogin">로그아웃</v-tab>
      </v-tabs>
      <v-window>
        <router-view :key="$route.fullPath"></router-view>
      </v-window>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      tab: '',
      loginUser:{},
    };
  },
  computed:{
    isLogin(){
      return this.$store.getters.isLogin
    }
  }
  ,
  components: {

  },
  methods:{
    // 로그아웃
    logout() {
      this.$store.dispatch("logout");
    },
  }   
}
</script>


<style>
body {
  display: flex;
  justify-content: center;
  margin-right: 0;
  background-color: #fcf7e8;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 80%;
  align-self: center;
  margin: 0;
}

nav {
  padding: 30px;
  background-color: #fcf7e8;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  background-color: #fcf7e8;
}

/* nav a.router-link-exact-active {
  color: #42b983;
} */
#link_txt {
  text-decoration: none;
  color: rgb(68, 90, 187);
  font-weight: 700;
  
}
#btn_style1 {
  background-color: #d0dafb;
  text-decoration: none;
  color: rgb(68, 90, 187);
  font-weight: 700;
}

#btn_style2 {
  background-color: #d2e0fc;
  text-decoration: none;
  color: rgb(57, 67, 154);
  font-weight: 700;
}
.search_bar {
  width: 300px;
  text-align: center;
  /* display: flex; */
  /* justify-content: end; */

}

#box1 {
  display: flex;
  justify-content: space-between;
  align-items: end;

}


#mini {
  height: 40px;
  margin: 10px;
  display: grid;
  grid-template-columns: 1fr;
  
}

.header-cell-text {
  display: inline-block;
}

.pl{
    width: 200px;
    border: 1px solid #C4C4C4;
    box-sizing: border-box;
    border-radius: 10px;
    padding: 12px 13px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 16px;
}

.pl:focus{
    /* border: 1px solid #e0bc51; */
    box-sizing: border-box;
    border-radius: 10px;
    outline: 4px solid #fff4b5;
    border-radius: 10px;
}
h1 {
  margin-top: 30px;
}

.centered-tabs {
  display: flex;
  justify-content: center;
}

</style>
<style scoped>

a {
  background: #fff4b5;
}
</style>