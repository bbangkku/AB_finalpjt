<template>
  <div id="at_box">
    <h3>회원정보 수정</h3>
    <br>
    <form @submit.prevent="updateUserProfile">
      <div class="mid">
        <!-- nickname -->
        <div class="mini">
            <h3>NICKNAME</h3>
            <input 
              class="pl"
              v-model="nickname" type="text"
              required
              placeholder="NICKNAME">
        </div>

        <!-- gender -->
        <div id="mini">
          <h3>성별&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h3>
          <select v-model="gender" class="pl">
            <option disabled value="">성별</option>
            <option value="M">남</option>
            <option value="F">여</option>
          </select>
        </div>

        <!-- age -->
        <div id="mini">
          <h3>나이&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h3>
          <div>
            <input class="pl" v-model="age" type="number"
            required
            placeholder="나이">
          </div>
        </div>

        <!-- salary -->
        <div id="mini">
          <h3>연봉&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</h3>
          <input
            class="pl"
            v-model="salary"
            type="number"
            placeholder="SALARY"/>
        </div>

        <!-- 가용금액 -->
        <div id="mini">
          <h3>가용금액&nbsp;&nbsp;&nbsp;&nbsp;</h3>
            <input class="pl" v-model="money" type="number"
            required
            placeholder="가용 금액">
        </div>

        <div id="mini">
          <h3>주거래 은행&nbsp;</h3>
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
        <br>
        <v-btn rounded="sm" color="#FFF176">
          <button type="submit">프로필 수정</button>
      </v-btn>
      </div>
    </form>
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
.mini{
  display: flex;
  align-content: center;
  margin: 10px;
  /* flex-direction: row;
  justify-content: center; */
}

.mid{
  display: grid;
  flex-direction: row;
  justify-items: center;
}
.mid1{
  display: flex;
  align-content: space-around;
}

#box1{
  display: flex;
  flex-direction:column;
  width: 90%;
  margin: 0;
}
#at_box{
  /* text-align: left; */
  border: 2px solid rgb(250, 213, 132);
  margin: 15px;
  padding: 15px;
  border-radius: 20px;
  font-family: 'NanumSquareRound';
  font-weight: lighter;
}

#r_comment{
  width: 300px;
  height: 40px;
  text-align: left;
  border: 2px solid rgb(250, 213, 132);
  margin: 10px;
  padding: 15px;
  border-radius: 10px;
}

#check{
  display: grid;
  flex-direction: row;
  justify-items: center;
}

#mini{
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.pl{
    width: 300px;
    border: 2px solid rgb(250, 213, 132);
    box-sizing: border-box;
    border-radius: 10px;
    padding: 10px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 16px;
    text-align: left;
}

.pl:focus{
    /* border: 1px solid #e0bc51; */
    box-sizing: border-box;
    border-radius: 10px;
    outline: 4px solid #fff4b5;
    border-radius: 10px;
}

h3{
  margin: 8px;
}
</style>
