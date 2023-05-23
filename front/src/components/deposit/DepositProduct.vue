<template>
  <div>
    <h1>예금 상품</h1>
    <v-col cols="12" sm="4" md="2">
      <router-link to="/installment" id="link_txt">
        <v-btn block size="x-large" id="btn_style1">
          적금상품 보러가기
        </v-btn>
      </router-link>
    </v-col>
    <div id="box1">
      <h5 style="padding:0px 10px 10px 10px; color: grey;">※ 상품명 클릭 시 상세페이지로 이동합니다.</h5>
      <div class="search_bar">
        <!-- <v-card class="mx-auto" color="grey-lighten-3" max-width="500" style="width: 300px; height: 70px; align-items: center;"> -->
          <v-card-text style="width: 300px; height: 70px; align-items: center; margin-bottom: 10px;">
            <v-text-field
              v-model="search"
              :loading="loading"
              density="compact"
              variant="solo"
              label="은행 검색"
              append-icon="mdi-magnify"
              single-line
              hide-details
              @click:append-inner="onClick"
            ></v-text-field>
          </v-card-text>
        <!-- </v-card> -->
      </div>
    </div>
    
    <!-- {{ products }} -->

    <v-data-table
      :headers="headers"
      :items="products"
      :items-per-page="40"
      :search="search"
      multi-sort
      class="elevation-1"
    >
      <template slot="item.product" slot-scope="{ item }">
        <!-- 상세 페이지로 -->
        <router-link :to="{ name: 'd_product_detail', params: { productId: item.id } }" id="link_txt">
          {{ item.product }}
        </router-link>
      </template>
    </v-data-table>
  </div>
</template>

<script>
export default {
  name: 'DepositProduct',
  data() {
    return {
      search: '',
      loaded: false,
      loading: false,
    };
  },
  created() {
    this.$store.dispatch('getDeposit');
  },
  computed: {
    deposit() {
      return this.$store.state.deposit;
    },
    headers() {
      return [
        { text: '은행', align: 'start', sortable: false, value: 'bank' },
        // { text: 'ID', value: 'id' },
        { text: '상품', value: 'product' },
        { text: '6개월', value: '6개월' },
        { text: '12개월', value: '12개월' },
        { text: '24개월', value: '24개월' },
        { text: '36개월', value: '36개월' },
      ];
    },
    products() {
      if (this.deposit && this.deposit.response) {
        return this.deposit.response.map((item) => ({
          ...item,
          productId: item.id,
        }));
      }
      return [];
    },
  },
  methods: {
    onClick() {
      this.loading = true;

      setTimeout(() => {
        this.loading = false;
        this.loaded = true;
      }, 2000);
    },
  },
};
</script>

<style>
/* 필요한 스타일링 작성 */
</style>
<style scoped>

</style>
