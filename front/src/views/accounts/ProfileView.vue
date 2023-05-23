<template>
  <div>
    <h1>{{ this.$store.state.loginUser.nickname }}의 프로필</h1>
    <!-- {{ this.$store.state.loginUser }} -->
    <p>성별: {{ this.$store.state.loginUser.gender }}</p>
    <p>나이: {{ this.$store.state.loginUser.age }}</p>
    <p>가능 금액: {{ this.$store.state.loginUser.money }}</p>
    <p>주거래 은행: {{ this.$store.state.loginUser.bank }}</p>
    <p>가입상품 : {{ this.$store.state.loginUser.financial_products }} </p>
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
      console.log('asdasdsada',this.$store.state.loginUser)
      if (Object.keys(this.$store.state.loginUser).length === 0) {
        alert("로그인이 필요한 페이지입니다...");
        this.$router.push({ name: "LogInView" });
      }
    },
    // 프로필 업뎃하기
    updateUserProfile() {
      // Send updated profile data to the API for update
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

<style>
label {
position: absolute;
color: #878787;
left: 50%;
transform: translateX(-50%);
font-size: 14px;
bottom: 8px;
transition: all .2s;
}

#box1 {
  margin: 5px;
}
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 8px;
  text-align: center;
  border-bottom: 1px solid #ddd;
  cursor: pointer;
}

#exchange {
  margin: 10px;
  display: grid;
  grid-template-columns: 1fr;
  height: 200px;
  justify-items: center;
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

.list{
    border: none;
    background-color: #FFFFFF;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 16px;
    padding: 7px 10px;
    margin: 5px 7px;
    box-sizing: border-box;
}

.list:focus{
    background: #F8E4FF;
    width: 184px;
    border-radius: 8px;
    box-sizing: border-box;
    text-align: left;
}


/* * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
} */

.input_box {
  position: relative;
  width: 300px;
  margin-top: 30px;
}

input {
  font-size: 15px;
  color: #222222;
  width: 200px;
  border: none;
  border-bottom: solid #aaaaaa 1px;
  padding-bottom: 10px;
  text-align: center;
  position: relative;
  background: none;
  z-index: 5;
}

input::placeholder { color: #aaaaaa; }
input:focus { outline: none; }

.span1 {
  display: block;
  position: absolute;
  bottom: 0;
  left: 50%; 
  background-color: #666;
  width: 0;
  height: 2px;
  border-radius: 2px;
  transform: translateX(-50%);
  transition: 0.3s;
}

label {
position: absolute;
color: #878787;
left: 50%;
transform: translateX(-50%);
font-size: 14px;
bottom: 8px;
transition: all .2s;
}

input:focus ~ label, input:valid ~ label {
font-size: 15px;
bottom: 40px;
color: #666;
font-weight: bold;
}

input:focus ~ span, input:valid ~ span {
width: 100%;
}

.mid{
  display: flex;
  justify-content: center;
}
</style>