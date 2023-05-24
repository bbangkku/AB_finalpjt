<template>
  <div>
    <div id="at_box">
      <h1>{{ this.$store.state.loginUser.nickname }}님의 프로필 😘</h1>
      
      <hr />
      <div>
        <h3>성별: {{ this.$store.state.loginUser.gender }}</h3>
        <h3>나이: {{ this.$store.state.loginUser.age }}</h3>
        <h3>연봉: {{ this.$store.state.loginUser.salary }} 만원</h3>
        <h3>가용 금액: {{ this.$store.state.loginUser.money }}</h3>
        <h3>주거래 은행: {{ this.$store.state.loginUser.bank }}</h3>
        <div v-if="this.$store.state.loginUser.financial_products.length !== 0">
          <h3>가입상품 : {{ this.$store.state.loginUser.financial_products }}</h3>
        </div>
        <div
          v-if="
            this.$store.state.loginUser.like_financial_products.length !== 0
          "
        >
          <p>
            좋아하는 상품 :
            {{ this.$store.state.loginUser.like_financial_products }}
          </p>
        </div>
      </div>
      <div class="a_right">
        <div class="b_box">
          <v-btn @click="updateProfile" id="btn" type="submit" rounded="sm" block size="x-large" color="#3F51B5">
            수정하기
          </v-btn>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
import Swal from "sweetalert2";
// const API_URL = "http://127.0.0.1:8000";

export default {
  name: "ProfileView",
  data() {
    return {
      loginUser: {},
      updatedProfile: {
        nickname: "",
        gender: "",
        age: "",
        money: "",
        bank: "",
        check: "",
      },
    };
  },
  created() {
    this.check = false;
    this.getProfile();
  },
  methods: {
    checkProfile() {
      this.check = true;
    },
    // 프로필 가져오기
    getProfile() {
      console.log(this.$store.state.loginUser);
      if (Object.keys(this.$store.state.loginUser).length === 0) {
        Swal.fire({
          title: "로그인이 필요한 페이지입니다",
          icon: "error",
          confirmButtonText: "확인",
        }).then(() => {
          this.$router.push({ name: "login" });
        });
      } else {
        // 프로필 가져오기 로직
      }
    },
    updateProfile() {
      this.$router.push({
        name: "profile_update",
        params: {
          nickname: this.$store.state.loginUser.nickname,
          gender: this.$store.state.loginUser.gender,
          age: this.$store.state.loginUser.age,
          money: this.$store.state.loginUser.money,
          salary: this.$store.state.loginUser.salary,
          bank: this.$store.state.loginUser.bank,
        },
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
}

#at_box {
  border: 2px solid rgb(250, 213, 132);
  margin: 30px;
  padding: 20px;
  border-radius: 20px;
  text-align: left;
}
h1 {
  margin: 10px;
}
h3 {
  margin: 10px;
}
div{
  font-family: 'NanumSquareRound';
}
#btn{
  color: white;
}

#b_box{
  width: 100px;
}
</style>
