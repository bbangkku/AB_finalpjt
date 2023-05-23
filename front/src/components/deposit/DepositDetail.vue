<template>
  <div>
    <h1>Deposit 상세 페이지</h1>
    <!-- <p>Product Name: {{ productId }}</p> -->
    <!-- {{ product }} -->
    <v-list lines="one">
    <v-list-item>
    <p>은행명 : {{ product.kor_co_nm }}</p>
    </v-list-item>
    </v-list>
    <p>상품명 : {{ product.fin_prdt_nm }}</p>
    
    <p>기타 유의사항 : {{ product.etc_note }}</p>
    <p>가입대상 : {{ product.join_member }}</p>
    <p>가입방법 : {{ product.join_way }}</p>
    <p>우대조건 : {{ product.spcl_cnd }}</p>
    <p>가입조건 : {{ product.join_deny }}</p>
    <p>1-제한없음 / 2-서민전용 / 3-일부제한</p>
    
    
    <!-- 나머지 컴포넌트 내용 -->
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'DepositDetail',
  data() {
    return {
      product: {},
    };
  },
  created() {
    this.productId = this.$route.params.productId;
    this.fetchProductName(this.productId);
  },
  methods: {
    fetchProductName(productId) {
      console.log(productId)
      axios
        .get(`http://127.0.0.1:8000/bank_api/d_detail/${productId}/`)
        .then((response) => {
          console.log(response);
          this.product = response.data.product
          // productId 대한 조회 결과를 사용하여 컴포넌트에 필요한 데이터를 설정하세요.
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
