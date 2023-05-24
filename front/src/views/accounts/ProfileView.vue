<template>
  <div>
    <div id="at_box">
      <h1>{{ this.$store.state.loginUser.nickname }}님의 프로필</h1>
      <br>
      <div>
        <h3>성별: {{ this.$store.state.loginUser.gender }}</h3>
        <h3>나이: {{ this.$store.state.loginUser.age }}</h3>
        <h3>가능 금액: {{ this.$store.state.loginUser.money }}</h3>
        <h3>주거래 은행: {{ this.$store.state.loginUser.bank }}</h3>
        <div v-if="this.$store.state.loginUser.financial_products.length !== 0">
          <p>가입상품 : {{ this.$store.state.loginUser.financial_products }} </p>
        </div>
        <div v-if="this.$store.state.loginUser.like_financial_products.length !== 0">
          <p> 좋아하는 상품 : {{ this.$store.state.loginUser.like_financial_products }} </p>
        </div>

      </div>
      
    </div>

    <!-- 추가 정보 및 이미지 등 사용자 프로필에 필요한 항목 표시 -->
    <!-- 프로필 수정 기능을 구현할 수도 있습니다 -->
    <div class="mid">
      <!-- <button @click="checkProfile">프로필 수정하기</button> -->
      <form @submit.prevent="updateUserProfile" v-if="checkProfile">
        <div class="mini">
          <div class="input_box">
            <input type="textr" id="nickname" v-model="updatedProfile.nickname"  required style="margin: 0;">
            <label for="nickname">닉네임</label>
            <span class="span1"></span>
          </div>
        </div>

        <div id="mini">
          <select v-model="updatedProfile.gender" class="pl">
            <option disabled value="">성별</option>
            <option value="M">남성</option>
            <option value="F">여성</option>
          </select>
        </div>

        <div id="mini">
          <select id="age" v-model="updatedProfile.age" class="pl">
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

        <div id="mini">
          <select id="available_amount" v-model="updatedProfile.available_amount" class="pl">
            <option disabled value="">가용 금액</option>
            <option value="0-30M">0 ~ 30,000,000</option>
            <option value="30M-100M">30,000,000 ~ 100,000,000</option>
            <option value="100M-300M">100,000,000 ~ 300,000,000</option>
            <option value="300M-1000M">300,000,000 ~ 1,000,000,000</option>
          </select>
        </div>

        <div id="mini">
          <select id="bank" v-model="updatedProfile.bank" class="pl"> 
            <option disabled value="">주거래 은행</option>
            <option value="KEB하나은행">KEB하나은행</option>
            <option value="SC제일은행">SC제일은행</option>
            <option value="국민은행">국민은행</option>
            <option value="신한은행">신한은행</option>
            <option value="외환은행">외환은행</option>
            <option value="우리은행">우리은행</option>
            <option value="한국시티은행">한국시티은행</option>
            <option value="경남은행">경남은행</option>
            <!-- 주거래 은행 선택 옵션 추가 -->
          </select>
        </div>
        <button type="submit">프로필 수정</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Swal from 'sweetalert2'
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "ProfileView",
  data() {
    return {
      loginUser : {},
      updatedProfile: {
        nickname: "",
        gender: "",
        age: "",
        money: "",
        bank: "",
        check: ""
      },
    };
  },
  created() {
    this.check = false
    this.getProfile()

  },
  methods: {
    checkProfile() {
      this.check = true;
    },
    // 프로필 가져오기
    getProfile() {
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


    // getProfile() {
    //   console.log('asdasdsada',this.$store.state.loginUser)
    //   if (Object.keys(this.$store.state.loginUser).length === 0) {
    //     alert("로그인이 필요한 페이지입니다...");
    //     this.$router.push({ name: "login" });
    //   }
    // },

    // 프로필 업뎃하기
    updateUserProfile() {
      // Send updated profile data to the API for update
      console.log('업데이트하자')
      axios({
        method: "patch",
        url: `${API_URL}/accounts/signup`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: this.updatedProfile,
      })
        .then((res) => {
          console.log(res);
          // Update the local profile data with the updated values
          this.profile = res.data;
          // Reset the updatedProfile object
          this.updatedProfile = {
            nickname: "",
            gender: "",
            age: "",
            available_amount: "",
            bank: "",
          };
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
#at_box{
  border: 2px solid rgb(250, 213, 132);
  margin: 30px;
  padding: 20px;
  border-radius: 20px;
  text-align: left;
}
h1{
  margin: 0;
}
h3{
  margin: 10px;
}
</style>