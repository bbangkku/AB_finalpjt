<template>
  <div>
    <h3>회원정보 수정</h3>
    <div class="mid">
      <form @submit.prevent="updateUserProfile">
        <div class="mini">
          <div class="input_box">
            <input
              type="text"
              id="nickname"
              v-model="nickname"
              required
              style="margin: 0"
            />
            <label for="nickname">닉네임</label>
            <span class="span1"></span>
          </div>
        </div>

        <div id="mini">
          <select v-model="gender" class="pl">
            <option disabled value="">성별</option>
            <option value="M">남</option>
            <option value="F">여</option>
          </select>
        </div>

        <div id="mini">
          <select id="age" v-model="age" class="pl">
            <option disabled value="">나이</option>
            <option value="0-10">0 ~ 10</option>
            <option value="10-20">10 ~ 20</option>
            <option value="20-30">20 ~ 30</option>
            <option value="30-40">30 ~ 40</option>
            <option value="40-50">40 ~ 50</option>
            <option value="50-60">50 ~ 60</option>
            <option value="60-70">60 ~ 70</option>
            <option value="70-80">70 ~ 80</option>
          </select>
        </div>
        <div>
          <input
            id="r_comment"
            v-model="salary"
            type="number"
            placeholder="SALARY"
          />
        </div>

        <div id="mini">
          <select id="money" v-model="money" class="pl">
            <option disabled value="">가용 금액</option>
            <option value="0-30M">0 ~ 30,000,000</option>
            <option value="30M-100M">30,000,000 ~ 100,000,000</option>
            <option value="100M-300M">100,000,000 ~ 300,000,000</option>
            <option value="300M-1000M">300,000,000 ~ 1,000,000,000</option>
          </select>
        </div>

        <div id="mini">
          <select id="bank" v-model="bank" class="pl">
            <option disabled value="">주거래 은행</option>
            <option value="KEB하나은행">KEB하나은행</option>
            <option value="SC제일은행">SC제일은행</option>
            <option value="국민은행">국민은행</option>
            <option value="신한은행">신한은행</option>
            <option value="외환은행">외환은행</option>
            <option value="우리은행">우리은행</option>
            <option value="한국시티은행">한국시티은행</option>
            <option value="경남은행">경남은행</option>
          </select>
        </div>
        <button type="submit">프로필 수정</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
// import Swal from 'sweetalert2'
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "ProfileUpdateView",
  data() {
    return {
      nickname: this.$store.state.loginUser.nickname,
      gender: this.$store.state.loginUser.gender,
      age: this.$store.state.loginUser.age,
      money: this.$store.state.loginUser.money,
      bank: this.$store.state.loginUser.bank,
      salary: this.$store.state.loginUser.salary,
    };
  },
  created() {},
  methods: {
    // 프로필 업뎃하기
    updateUserProfile() {
      const nickname = this.nickname;
      const gender = this.gender;
      const age = this.age;
      const money = this.money;
      const bank = this.bank;
      const salary = this.salary;
      axios({
        method: "put",
        url: `${API_URL}/dj-rest-auth/user/change/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: {
          nickname,
          gender,
          age,
          money,
          bank,
          salary,
        },
      })
        .then((res) => {
          console.log(res);
          this.$store.state.loginUser.nickname = this.nickname;
          this.$store.state.loginUser.gender = this.gender;
          this.$store.state.loginUser.age = this.age;
          this.$store.state.loginUser.money = this.money;
          this.$store.state.loginUser.bank = this.bank;
          this.$store.state.loginUser.salary = this.salary;
          this.$router.push({ name: "profile" });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
#at_box {
  border: 2px solid rgb(250, 213, 132);
  margin: 30px;
  padding: 20px;
  border-radius: 20px;
  text-align: left;
}
h1 {
  margin: 0;
}
h3 {
  margin: 10px;
}
</style>
