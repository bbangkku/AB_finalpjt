<template>
  <div>
    <h1>로그인</h1>

    <div class="mid">
      <div class="mini">
        <div class="input_box">
          <input type="text"
            id="username"
            v-model="username"
            label="ID를 입력하세요" 
            required
            style="margin: 0;">
          <label for="username">username: </label>
          <span class="span1"></span>
        </div>
      </div>

      <div class="mini">
        <div class="input_box">
          <input type="password"
            id="password"
            v-model="password"
            label="비밀번호를 입력하세요" 
            required
            style="margin: 0;">
          <label for="password">password: </label>
          <span class="span1"></span>
        </div>
      </div>
    </div>

    <div>
      <button @click="login">로그인</button>
    </div>

    <div>
      <a href="#">아이디/비밀번호 찾기 | </a>
      <a class="bold">
        <router-link :to="{ name: 'signup' }">회원가입</router-link>
      </a>
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

<style>
.mid{
  display: flex;
  justify-content: center;
}
</style>