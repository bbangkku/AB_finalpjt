<template>
  <div id="total">
    <SlideView @imageClick="handleImageClick" />
    <div class="a_right">
      <v-col cols="12" sm="4" md="2">
        <router-link to="/deposit" id="link_txt">
          <v-btn block size="x-large" id="btn_style1">
            예금상품 보러가기
          </v-btn>
        </router-link>
      </v-col>
    </div>

    <div id="box1">
      <h5 style="padding:0px 10px 10px 10px; color: grey;">※ 상품명 클릭 시 상세페이지로 이동합니다.</h5>
      
      <div class="search_bar">
        <div class="input_box">
            <input type="text"
              v-model="search"
              label=" &nbsp;&nbsp;은행검색" 
              id="search_bank"
              append-icon="mdi-map-marker"
              required style="margin: 0;">
            <label for="search_bank">&nbsp; &nbsp;&nbsp;은행검색  🔍</label>
            <span class="span1"></span>
          </div>
      </div>
    </div>
    

    <v-data-table
      :headers="hd"
      :items="products"
      :items-per-page="10"
      :search="search"
      multi-sort
      class="elevation-1"
    >
      <template slot="item.product" slot-scope="{ item }">
        <!-- 상세 페이지로 -->
        <router-link :to="{ name: 'i_product_detail', params: { productId: item.id1 } }" id="link_txt">
          {{ item.product }}
        </router-link>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import SlideView from '@/views/slide/SlideView.vue';
export default {
  name: 'InstallmentProduct',
  created() {
    this.$store.dispatch('getInstallment');
  },
  computed: {
    installment() {
      return this.$store.state.installment;
    },
    products() {
      if (this.installment && this.installment.response) {
        return this.installment.response.map((item) => ({
          ...item,
          productId: item.id1,
        }));
      }
      return [];
    },
  },
  components:{
    SlideView
  },
  data() {
    return {
      search: '',
      loaded: false,
      loading: false,
      hd: [
        { text: 'Bank', align: 'start', sortable: false, value: 'bank' },
        { text: 'product', value: 'product' },
        { text: '이자방식', value: 'intr_rate_type_nm' },
        { text: 'type', value: 'type' },
        { text: '6개월', value: '6개월' },
        { text: '12개월', value: '12개월' },
        { text: '24개월', value: '24개월' },
        { text: '36개월', value: '36개월' },
      ],
    };
  },
  methods: {
    onClick() {
      this.loading = true;

      setTimeout(() => {
        this.loading = false;
        this.loaded = true;
      }, 2000);
    },
    handleImageClick(path) {
      if (this.$route.path === path) {
        // 현재 URL과 새로운 URL이 동일한 경우, 강제로 페이지 이동
        this.$router.push({ path: '/empty' }).then(() => {
          this.$nextTick(() => {
            this.$router.replace(path);
          });
        });
      } else {
        // URL이 변경된 경우, 페이지 이동
        this.$router.push(path);
      }
    },
  },
};
</script>

<style scoped>
#total{
  height: 1200px;
}
div {
  font-family: 'NanumSquareRound';
}

#box1{
  padding:10px;
  margin-bottom:10px;
}
.a_right {
  width: 93%;
  display: flex;
  justify-content: end;
}

/* 검색창 */
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
</style>