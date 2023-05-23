<template>
  <div>
    <h2>회원가입</h2>
    <div class="mid">
    <form @submit.prevent="signup">

      <div class="mini">
        <div class="input_box">
          <input type="textr" id="username" v-model="username"  required style="margin: 0;">
          <label for="username">ID</label>
          <span class="span1"></span>
        </div>
      </div>

      <div class="mini">
        <div class="input_box">
          <input type="textr" id="nickname" v-model="nickname"  required style="margin: 0;">
          <label for="nickname">닉네임</label>
          <span class="span1"></span>
        </div>
      </div>

      <div class="mini">
        <div class="input_box">
          <input type="password" id="password1" v-model="password1"  required style="margin: 0;">
          <label for="password1">비밀번호</label>
          <span class="span1"></span>
        </div>
      </div>

      <div class="mini">
        <div class="input_box">
          <input type="password2" id="password2" v-model="password2"  required style="margin: 0;">
          <label for="password2">비밀번호 확인</label>
          <span class="span1"></span>
        </div>
      </div>

      <div id="mini">
        <select id="gender" v-model="gender" required class="pl">
          <option disabled value="">성별</option>
          <option value="M">남성</option>
          <option value="F">여성</option>
        </select>
      </div>

      <div id="mini">
        <select id="age" v-model="age" required class="pl">
          <option disabled value="">나이</option>
          <option value="0-10">0세 ~ 10세</option>
          <option value="10-20">10세 ~ 20세</option>
          <option value="20-30">20세 ~ 30세</option>
          <option value="30-40">30세 ~ 40세</option>
          <option value="40-50">40세 ~ 50세</option>
          <option value="50-60">50세 ~ 60세</option>
          <option value="60-70">60세 ~ 70세</option>
          <option value="70-80">70세 ~ 80세</option>
          <option value="80 up">80세 이상</option>
        </select>
      </div>

      <div id="mini">
        <select id="money" v-model="money" required class="pl">
          <option disabled value="">가용 금액</option>
          <option value="0-30M">0 ~ 3,000만원</option>
          <option value="30M-100M">3,000만원 ~ 1억</option>
          <option value="100M-300M">1억 ~ 3억</option>
          <option value="300M-1000M">3억 ~ 10억</option>
          <option value="1000M UP">10억 이상</option>
        </select>
      </div>

      <div class="mini">
        <div class="input_box">
          <input type="salary" id="salary" v-model="salary"  required style="margin: 0;">
          <label for="salary">연봉</label>
          <span class="span1"></span>
        </div>
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
          <option value="광주은행">광주은행</option>
          <option value="부산은행">부산은행</option>
          <option value="전북은행">전북은행</option>
          <option value="제주은행">제주은행</option>
          <option value="기업은행">기업은행</option>
          <option value="농협">농협</option>
          <option value="수협">SC제일은행</option>
          <option value="한국산업은행">한국산업은행</option>
          <option value="한국수출입은행">한국수출입은행</option>
          <option value="null">없음</option>
        </select>
      </div>
      <div>
        <button type="submit">가입하기</button>
      </div>
      
    </form>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      username: '',
      nickname: '',
      password1: '',
      password2: '',
      money: '',
      gender: '',
      age: '',
      salary: '',
      bank:'',
      like_product:{},
      product:{},
    };
  },
  methods: {
    signup() {
      if (this.password1 !== this.password2) {
        alert('비밀번호가 일치하지 않습니다.');
        return;
      }
      const payload = {
        username: this.username,
        password1: this.password1,
        password2: this.password2,
        nickname: this.nickname,
        gender: this.gender,
        age: this.age,
        money: this.money,
        salary: this.salary,
        bank: this.bank,
        like_product: this.like_product,
        product: this.product,
      };
        this.$store.dispatch('signUp', payload)
        .then(() => {
          alert('회원가입이 완료되었습니다.');
          this.$router.push('/accounts/login');
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

<style>
/* label {
position: absolute;
color: #878787;
left: 50%;
transform: translateX(-50%);
font-size: 14px;
bottom: 8px;
transition: all .2s;
} */

</style>