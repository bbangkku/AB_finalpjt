<template>
  <div>
    <h1>LOGIN</h1>
    <div id="at_box">
      <div>
        <input id='r_comment' v-model="username" type="text"
        placeholder="ID">
      </div>
      <input id='r_comment' v-model="password" type="password"
        placeholder="PASSWORD">

      <div>
        <v-btn rounded="sm" color="#FFF176">
          <button @click="login">LOGIN</button>
        </v-btn>
        <a class="bold">
        <router-link :to="{ name: 'signup' }">
          <v-btn rounded="sm" color="#FFF176">회원가입</v-btn>
        </router-link>
      </a>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "LogInView",
  data() {
    return {
      username: null,
      password: null,
    };
  },
  methods: {
    login() {
      const username = this.username;
      const password = this.password;
      // username, password 들고 store로 감
      const payload = {
        username,
        password,
      };
      // console.log(payload)
      this.$store.dispatch("login", payload)
      // this.$store.dispatch("getUser", payload)

    }
  }
}
</script>

<style scoped>
#at_box{
  /* text-align: left; */
  border: 2px solid rgb(250, 213, 132);
  margin: 15px;
  padding: 15px;
  border-radius: 20px;
}

#r_comment{
  width: 40%;
  height: 40px;
  text-align: left;
  border: 2px solid rgb(250, 213, 132);
  margin: 15px;
  padding: 15px;
  border-radius: 20px;
}
</style>