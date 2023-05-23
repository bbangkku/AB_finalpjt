<template>
  <div id="at_box">
    <h2>회원가입</h2>
    <br>
    <h5 style="padding:0px 10px 10px 10px; color: grey;">
            ★ 표시된 항목은 필수로 입력해야합니다.</h5>
    <div class="mid">
    <form @submit.prevent="signup">

      <div>
        <input id='r_comment' v-model="username" type="text"
        required
        placeholder="ID">
      </div>

      <div>
        <input id='r_comment' v-model="nickname" type="text"
        required
        placeholder="NICKNAME">
      </div>

      <div>
        <input id='r_comment' v-model="password1" type="password"
        required
        placeholder="PASSWORD">
      </div>

      <div>
        <input id='r_comment' v-model="password2" type="password"
        required
        placeholder="PASSWORD CHECK">
      </div>

      <div>
        <input id='r_comment' v-model="salary" type="number"
        required
        placeholder="SALARY">
      </div>

      <div id="check">
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
      </div>

      <div>
        <v-btn rounded="sm" color="#FFF176">
          <button type="submit">가입하기</button>
        </v-btn>
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

#check{
  display: flex;
  flex-direction: column;
  justify-content: center;
}

#mini{
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.pl{
    width: 200px;
    border: 2px solid rgb(250, 213, 132);
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
</style>