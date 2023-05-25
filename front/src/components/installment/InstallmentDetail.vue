<template>
  <div class="details">
    <h1>{{ product.fin_prdt_nm }} 상세 페이지</h1>
    <div id="at_box">
      <div class="markbox">
        <div v-if="product.kor_co_nm === '우리은행'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwq5WBSGnSWppqxcMqooBDcbt36mu9C8jXKB0_3cB67Qad5H6c3lBB-b6lE2vqROpq_TYfeY-cke98TuzU1cjUBCu6QjKA2_-sRiUr0DfbLcMvqME6ILVLzY_qgWD0yX5ez-G-ZsDLWbq4MumkSOh37Nk.svg"
            alt=""
            height="200px"
            width="600px"
            cover
          />
        </div>

        <div v-if="product.kor_co_nm === '한국스탠다드차타드은행'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwq-lgKg2ExvxGyOiE-5TrRdUg6d_1AJNUaexaFhhKPNNAlLBCNy_IJpVJ2ldDlsg6dh78DeyGMNXe0GTqwqXUfilJWlikgQoF217fdMf51crZNHFfH3e-q1E72TdatqhufFl5a4IbXCRQS_mwyLwIryY.svg"
            alt=""
            height="200px"
            cover
          />
        </div>

        <div v-if="product.kor_co_nm === '부산은행'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwq_gF4HAKuvUMHiPFd40zIzoFHO82GKGn7jwIHrYTpQ2kaTVBIlmdMctEvhzscWR3bEDsCsHV-xWtRO3U9zzWomZdqh4tdEBWodc-Xlin3dMK1mwSUsmS4rGDD0npgcLh3vh5xV50AY5jZKtQJ5bMmGk.svg"
            alt=""
            width="600px"
            cover
          />
        </div>

        <div v-if="product.kor_co_nm === '광주은행'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwq8ERBc322w__bKX32FDbydDaE0dyWZDBt7jTRAXkWFdi8YaaoJ7U5FGtNspL1T7mxMJIZtyCxnofzbNazrIT5TH2pgZKqeuDaf6C-r1s3eEjVRTiZYsug0qnH7lQd3jdtCnDoronUL1FGmIFdPfJKns.svg"
            alt=""
            width="600px"
            cover
          />
        </div>

        <div v-if="product.kor_co_nm === '제주은행'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwqwER07Y-4y2hTP2aIjf2U06xlB1ETcbePPmh-FgOkhLF0jsiNBlQRqPjN8tSTfwqTU2dHYvGSf1mNP6auj3Zr1ugZhcoacs2q61h-pDPSbvswa_KgPT3vHo9os795xEsnVn_D7YTXvfIk0vV-oRwmYk.svg"
            alt=""
            width="600px"
            cover
          />
        </div>

        <div v-if="product.kor_co_nm === '전북은행'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwq5kDyFXczsV2LFQZnOFqb8Tzc2Vr5I15JpwHD38ZvIMbyEsrqEa8zz2NlfMmpzamgDIwwwDOcqrB0QygtofKBIfoLwAGURr0wimLAphrHZfTDFMZdJ-QFiE4YP0iD6nJWvVAOXu0xvvMwWvkBbL8iPw.svg"
            alt=""
            width="600px"
            cover
          />
        </div>

        <div v-if="product.kor_co_nm === '경남은행'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwq9bqNzAeRDigVQUfAXBRaF2T339t6hc0ekQ1PwdZTKNZ4AEiIic2wpKLOOv1XSyxhXpQtV-I8wkZRrkmOd4dFIXehLG1I3P8tzHFh8-sRZVmFG7-gY7yfomffrFFRVwtAIDq3TRkoWEDGXBT26soZTg.svg"
            alt=""
            width="600px"
            cover
          />
        </div>

        <div class="mark" v-if="product.kor_co_nm === '중소기업은행'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwq14OYRp2TBRz0CEETadyklzqSEV-HLe0SOATqJaLGVrorvqER5ysU-V7of_mIfidWtqgZGHM3cXZ7fyM9aahK_Lc0f4LGqzHr4fAskxKnhW38AoDLMti0byIskuvkAST8gzwwvCuq2vVyCMrQbY2dKU.svg"
            alt=""
            width="600px"
            cover
          />
        </div>

        <div class="mark" v-if="product.kor_co_nm === '한국산업은행'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwq8hmlTOofXvglaXcCyWQwdioqK-lp8XgpvIMvFmzVnNWRuLJPA9AtxBzJPZTRkuLbsUoiV_52046ve4y4HoxgCu8tpmfsteInP442IfTZerfJudavpW8xGUUdXlKghNusqrJidfkEe1nGHik-q5CPbc.svg"
            alt=""
            width="600px"
            cover
          />
        </div>

        <div class="mark" v-if="product.kor_co_nm === '국민은행'">
          <img
            src="data:image/png;base64,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"
            alt=""
            width="500px"
            heigt="200px"
            cover
          />
        </div>

        <div class="mark" v-if="product.kor_co_nm === '신한은행'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwq9L9D4v95BSTuZJtWwfdNlik1wM28gIsOIyOmD5E22YoocJ9oS4etISW_gvG6ayX8WnT4GJ9oxpWjFE3r3J3NZaTCSJN_b9fSwT0mk1dS31HFUiZZDR6zeG8mfc_xeqpWA0FYFCFDn6z_mM4YG81nYo.svg"
            alt=""
            width="600px"
            cover
          />
        </div>

        <div class="mark" v-if="product.kor_co_nm === '농협은행주식회사'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwq1xMbhKiGenzo47m5-fPUqI0n77XemqJwdeOLs1AV3SiGeKmULuLLeZuH2AFZCR4tzt4eQnrZlDrosXH-4FdGhpT4xcsicLgY4HfDWJGYohVu0exekQaQpKCiK5RK1ybxRBeOO2XsQNofAKbYxRVcLE.svg"
            alt=""
            width="600px"
            cover
          />
        </div>

        <div class="mark" v-if="product.kor_co_nm === '하나은행'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwq4p99Va2qwhRF9t46lrkfg7v510LxQiACgAqHnDys8MZGwKLcQbXXOz64ADjxCZegUaKE0j_gV5amBNfFw-Z09PszhKSRc_g9CPenClzyKsMWh-BM_W5BVT3u-QkTSxuqOBBPVPctHwY3K7uMvOnzyU.svg"
            alt=""
            width="600px"
            cover
          />
        </div>

        <div class="mark" v-if="product.kor_co_nm === '수협은행'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwq2nX57ATjKyYM4jkqdmPJTA2Orkb3zcK-PweVQLhI2LJb9db5U7-C348vUx-tMY2vJ8R1oTSG4f9L5sd7DdQOvEoRvILDAe5OzIgdrn40WHxRG-EnSM3xBedbbUPfRXBcT-bzYn1tx53N9RJqH2AQsg.svg"
            alt=""
            width="600px"
            cover
          />
        </div>

        <div class="mark" v-if="product.kor_co_nm === '주식회사 카카오뱅크'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwqx_jrArKbk_rRT41b9KXUlZ7xVArp3VgSTqLQGqNORjY2Tuzd2CcXRMQue7ICn4_uATE6cFj9eXlKCuv6Tjf1IM1koje7Am9anzeiJYyvkJdWdXgqzg_97izi0QgQwZE7xvNz8XBHxJ-9_eR1aIkDHw.svg"
            alt=""
            width="600px"
            cover
          />
        </div>

        <div class="mark" v-if="product.kor_co_nm === '토스뱅크 주식회사'">
          <img
            src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbqux6i%2FbtrYdjBtlRg%2Fsri12tRO3Pz8b3nC0kjtVk%2Fimg.jpg"
            alt=""
            width="600px"
            cover
          />
        </div>

        <div class="mark" v-if="product.kor_co_nm === '주식회사 케이뱅크'">
          <img
            src="https://i.namu.wiki/i/ze8Asys7bFONN62QXdFwq2lIO6GnKIAftM6uRzDDZlpGOPiQ2HoDC_zjRHusb0OVO4sqpRbSYO0g0M8EyZg0tZxCLFLpxhHfU93gwH3mY_xH4ydtZLOeB-uXR7k74G5yRNkw0DO3j1Ttmgh6gzYf9PKfr1e-BSKl1WItPWlns_Q.svg"
            alt=""
            width="600px"
            cover
          />
        </div>
      </div>
      <hr />
      <br />

      <div class="btngrid">
        <div style="content-align: right; width: 200px; margin-right: 20px">
          <router-link to="/installment" id="link_txt">
            <v-btn block size="x-large" id="btn_style2"> 돌아가기 </v-btn>
          </router-link>
        </div>
      </div>

      <v-card-subtitle style="text-align: left">
        <h3>은행명 : {{ product.kor_co_nm }}</h3>
        <h3>가입대상 : {{ product.join_member }}</h3>
        <h3>가입방법 : {{ product.join_way }}</h3>
        <h3>우대조건 : {{ product.spcl_cnd }}</h3>
        <div v-if="product.join_deny === 1">
          <h3>가입조건 : 제한없음</h3>
        </div>
        <div v-if="product.join_deny === 2">
          <h3>가입조건 : 서민전용</h3>
        </div>
        <div v-if="product.join_deny === 3">
          <h3>가입조건 : 일부제한</h3>
        </div>
        <h3>만기 후 이자율 : {{ product.mtrt_int }}</h3>
        <h3>※ 기타 유의사항 ※</h3>
        <h3>{{ product.etc_note }}</h3>
      </v-card-subtitle>

      <v-btn
        v-if="btn"
        color="orange-lighten-2"
        variant="text"
        @click="addProduct"
      >
        해지하기
      </v-btn>
      <v-btn v-else color="orange-lighten-2" variant="text" @click="addProduct">
        가입하기
      </v-btn>

      <v-spacer></v-spacer>
    </div>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "InstallmentDetail",
  data() {
    return {
      product: {},
      reveal: false,
      show: false,
      pro: "",
    };
  },
  computed: {
    btn() {
      return this.$store.state.loginUser.financial_products.includes(
        this.product.fin_prdt_nm
      );
    },
  },
  created() {
    this.productId = this.$route.params.productId;
    this.fetchProductName(this.productId);
    // this.$router.go(0)
  },
  methods: {
    isProductIn(bl) {
      this.btn = bl;
    },
    fetchProductName(productId) {
      console.log(productId);
      axios
        .get(`http://127.0.0.1:8000/bank_api/i_detail/${productId}/`)

        .then((response) => {
          console.log("응ㅇ애");
          console.log(response);
          this.product = response.data.product;
          // productId 대한 조회 결과를 사용하여 컴포넌트에 필요한 데이터를 설정하세요.
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addProduct() {
      const updatedProducts = this.$store.state.loginUser.financial_products;
      const productIndex = updatedProducts.indexOf(this.product.fin_prdt_nm);
      this.isProductIn(updatedProducts.includes(this.product.fin_prdt_nm));
      console.log(this.product.fin_prdt_nm);
      if (productIndex !== -1) {
        // 이미 해당 상품이 있으면 삭제
        updatedProducts.splice(productIndex, 1);
      } else {
        // 해당 상품이 없으면 추가
        updatedProducts.push(this.product.fin_prdt_nm);
        this.$store.commit("ADDPRODUCT", updatedProducts);
      }
      const requestData = {
        updatedProducts: updatedProducts,
        pro: "i",
      };
      axios({
        method: "post",
        url: `${API_URL}/bank_api/addproduct/${this.$store.state.loginUser.id}/${this.productId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: requestData,
      })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
#at_box {
  /* text-align: left; */
  width: 90%;
  border: 2px solid rgb(250, 213, 132);
  margin: 20px;
  padding: 35px;
  border-radius: 20px;
  font-family: "NanumSquareRound";
  font-weight: lighter;
}
div {
  font-family: "NanumSquareRound";
  font-weight: lighter;
}
.v-card--reveal {
  bottom: 0;
  opacity: 1 !important;
  position: absolute;
  width: 100%;
}

.mark {
  padding: 20px;
}

.markbox {
  padding: 20px;
}

h3 {
  margin: 5px;
}
.btngrid {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr;
  justify-items: end;
}
.details {
  display: grid;
  justify-items: center;
}
</style>
