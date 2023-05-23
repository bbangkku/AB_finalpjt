<template>
  <div>
    <h1>적금 상품</h1>
    <v-col cols="12" sm="4" md="2">
      <router-link to="/deposit" id="link_txt">
        <v-btn block size="x-large" id="btn_style1">
          예금상품 보러가기
        </v-btn>
      </router-link>
    </v-col>

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
        
          <!-- <v-card-text style="width: 300px; height: 70px; align-items: center; margin-bottom: 10px;">
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
          </v-card-text> -->
        <!-- </v-card> -->
      </div>
    </div>
    

    <v-data-table
      :headers="hd"
      :items="products"
      :items-per-page="40"
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
  },
};
</script>
