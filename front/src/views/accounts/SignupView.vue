<template>
  <div id="at_box">
    <h2>회원가입</h2>
    <br>
    <!-- <h5 style="padding:0px 10px 10px 10px; color: grey;">
            ★ 표시된 항목은 필수로 입력해야합니다.</h5> -->
    
    <form @submit.prevent="signup">
      <div class="mid">
        <div id="box1">
          <!-- ID -->
          <div>
            <input class="pl" v-model="username" type="text"
            required
            placeholder="ID">
          </div>
          <!-- 닉네임 -->
          <div>
            <input class="pl" v-model="nickname" type="text"
            required
            placeholder="NICKNAME">
          </div>
          <!-- 비밀번호1 -->
          <div>
            <input class="pl" v-model="password1" type="password"
            required
            placeholder="PASSWORD">
          </div>
          <!-- 비밀번호2 -->
          <div>
            <input class="pl" v-model="password2" type="password"
            required
            placeholder="PASSWORD CHECK">
          </div>
           <!-- 연봉 -->
           <div>
            <input class="pl" v-model="salary" type="number"
            required
            placeholder="SALARY">
          </div>
        </div>
        
        <div id="box1">
          
          <!-- 성별 -->
          <div>
            <select id="gender" v-model="gender" required class="pl">
              <option disabled value="">성별</option>
              <option value="M">남성</option>
              <option value="F">여성</option>
            </select>
          </div>
          <!-- 나이 -->
          <div>
              <input
                v-model="age"
                type="number"
                required
                placeholder="나이"
                class="pl"
              />
            </div>
          
          <!-- 가용금액 -->
          <div>
              <input
                v-model="money"
                type="number"
                required
                placeholder="가용 금액"
                class="pl"
              />
            </div>
          <!-- 주거래은행 -->
          <div>
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
            <v-btn id="btn" color="#FFF176">
              <button type="submit">가입하기</button>
            </v-btn>
          </div>
          
        </div>
      </div>
      
    </form>
  </div>
</template>


<script>
export default {
  data() {
    return {
      username: "",
      nickname: "",
      password1: "",
      password2: "",
      money: "",
      gender: "",
      age: "",
      salary: "",
      bank: "",
      like_product: {},
      product: {},
    };
  },
  methods: {
    signup() {
      if (this.password1 !== this.password2) {
        alert("비밀번호가 일치하지 않습니다.");
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
      this.$store
        .dispatch("signUp", payload)
        .then(() => {
          alert("회원가입이 완료되었습니다.");
          const loginpayload = {
            username: this.username,
            password: this.password1,
          };
          console.log(payload);
          this.$store.dispatch("login", loginpayload);
          // this.$router.push('/accounts/login');
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>
.mid{
  display: flex;
  margin: 15px;
}
#box1{
  display: flex;
  flex-direction:column;
  width: 90%;
  margin-right: 30px;
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
  width: 100%;
  height: 40px;
  text-align: left;
  border: 2px solid rgb(250, 213, 132);
  margin: 15px;
  padding: 15px;
  border-radius: 10px;
}

#check{
  display: grid;
  flex-direction: row;
  justify-items: center;
}
/* 
#mini{
  display: flex;
  flex-direction: row;
  justify-content: center;
} */

.pl{
    width: 300px;
    height: 40px;
    margin-bottom: 15px;
    border: 2px solid rgb(250, 213, 132);
    box-sizing: border-box;
    border-radius: 10px;
    padding: 5px 10px;
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

#btn{
  width: 200px;
  height: 45px;
  border-radius: 20;
  margin: 5px;
  margin-right: 50px;
  padding: 5px;
}
</style>