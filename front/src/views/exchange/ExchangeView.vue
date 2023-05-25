<template>
  <div class="ex">
    <h2>환율 계산기</h2>
    <h5 style="padding:0px 10px 10px 10px; color: grey;">
            ※ 사용 가능 시간 : 11:00 AM ~ 6:00 PM</h5>
    <div id="at_box">
    <div id="exchange">
      
      <!-- 거래 유형 선택 -->
      <div id="mini">
        <select v-model="transactionType" class="pl">
          
          <option disabled value="">거래 유형을 선택하세요</option>
          <option class="list" value="구입"><p id="optioncolor">구입</p></option>
          <option value="판매">판매</option>
        </select>
      </div>

      <!-- 화폐 선택 -->
      <div id="mini">
        <select v-model="cur" class="pl">
          <option disabled value="">화폐를 선택하세요 💵</option>
          
          <option v-for="er in exchangedata" :key="er.cur_unit" :value="er.cur_unit">
            {{ er.cur_nm }} ({{ er.cur_unit }})
          </option>
        </select>
      </div>
      
      <!-- 환전할 금액 입력 -->
      <!-- <input type="number" v-model="amount" placeholder="환전할 금액을 입력하세요" /> -->
      
      <div class="mini">
        <div class="input_box">
          <input type="number" v-model="amount" required style="margin: 0;">
          <label>금액 입력</label>
          <span class="span1"></span>
        </div>

        <!-- 구입 영역 -->
        <div v-if="transactionType === '구입'">
          <div id="at_box2" v-if="selectedExchRate1 && amount">
            선택한 국가 환율: {{ parseFloat(selectedExchRate1.replace(/,/g, '')).toFixed(2) }}
            <br>
            환전 결과: {{ (parseFloat(selectedExchRate1.replace(/,/g, '')) * amount).toFixed(2)}} 원
            <br>
          </div>
        </div>
      
        <!-- 판매 영역 -->
        <div v-if="transactionType === '판매'">
          <div id="at_box2" v-if="selectedExchRate2 && amount">
            선택한 국가 환율: {{ parseFloat(selectedExchRate2.replace(/,/g, '')).toFixed(2) }}
            <br>
            환전 결과: {{ (parseFloat(selectedExchRate2.replace(/,/g, '')) * amount).toFixed(2) }} 원
            <br>
            <br>
          </div>
        </div>
      </div>

      
    </div>
    <br>
    <br>
    <!-- 표 -->
    <div>
      <table id="table1">
        <thead>
          <tr>
            <!-- 매입율 컬럼 정렬 -->
            <th v-on:click="sortBy('ttb')">
              <span class="header-cell-text">통화</span>
            </th>
            <th v-on:click="sortBy('ttb')">
              <span class="header-cell-text">매입율</span>
            </th>
            <!-- 매도율 컬럼 정렬 -->
            <th v-on:click="sortBy('tts')">
              <span class="header-cell-text">매도율</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="ed in exchangedata" :key="ed.cur_nm">
            <td>{{ ed.cur_nm }}</td>
            <td>{{ parseFloat(ed.ttb.replace(/,/g, '')).toFixed(2) }}</td>
            <td>{{ parseFloat(ed.tts.replace(/,/g, '')).toFixed(2) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    
  </div>
  </div>
</template>

<script>
export default {
  name: "ExchangeRate",
  data() {
    return {
      transactionType: "", // 구입 또는 판매 선택
      cur: "",
      amount: null,
      sortByColumn: "", // 정렬할 컬럼
      sortOrder: 1, // 정렬 순서 (1: 오름차순, -1: 내림차순)
    };
  },
  computed: {
    exchangedata() {
      return this.$store.state.exchange || [];
    },
    selectedExchRate1() {
      const selectedCurrency = this.exchangedata.find(
        (er) => er.cur_unit === this.cur
      );
      return selectedCurrency ? selectedCurrency.ttb : null;
    },
    selectedExchRate2() {
      const selectedCurrency = this.exchangedata.find(
        (er) => er.cur_unit === this.cur
      );
      return selectedCurrency ? selectedCurrency.tts : null;
    },
  },
  created() {
    this.getExch();
  },
  methods: {
    getExch() {
      this.$store.dispatch("getExch");
    },
    sortBy(column) {
      // 클릭한 컬럼과 정렬 순서를 설정합니다.
      this.sortByColumn = column;
      this.sortOrder *= -1;

      // 배열을 정렬합니다.
      this.exchangedata.sort((a, b) => {
        const valueA = parseFloat(a[column].replace(/,/g, ''));
        const valueB = parseFloat(b[column].replace(/,/g, ''));

        if (valueA < valueB) {
          return -1 * this.sortOrder;
        }
        if (valueA > valueB) {
          return 1 * this.sortOrder;
        }
        return 0;
      });
    },
  },
};
</script>

<style scoped>
#table1{
  position: relative;
}
#at_box{
  width: 90%;
  /* text-align: left; */
  border: 2px solid rgb(250, 213, 132);
  margin: 20px;
  padding: 35px;
  border-radius: 20px;
  font-family: 'NanumSquareRound';
}

#at_box2{
  width: 100%;
  height: 75px;
  /* text-align: left; */
  border: 2px solid rgb(250, 213, 132);
  margin-top: 10px;
  padding: 10px;
  border-radius: 20px;
  font-family: 'NanumSquareRound';
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
  /* margin: 10px; */
  display: grid;
  grid-template-columns: 1fr;
  height: auto;
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
.ex {
  display: grid;
  justify-items: center;
  grid-template-columns: 1fr;
}


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

h2 {
  padding:10px;
  color: rgb(90, 90, 90);
  margin: 10px;
  font-family: 'NanumSquareRound';
  font-weight:bold;
}
/* #table_div {
  margin-top: 130px;
} */

</style>
