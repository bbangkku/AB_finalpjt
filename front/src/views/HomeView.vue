<template>
   <div>
    <div v-if="hero === 'BG'">
      <img src="@/assets/thx.png" style="width:90%">
    </div> 
  <div v-if="!isLogin">
    <img src="@/assets/home.png" style="width:90%">
  </div>
  <div id="at_box" v-if="isLogin && hero !== 'BG'">
    <h3>추천 상품 목록</h3>
    <br>
    <hr>
    <br>
    <div v-for="re in recommend" :key="re.id">
      <router-link :to="{ name: 'd_product_detail', params: { productId: re.id } }" id="link_txt">
        <h3>{{ re.product }}</h3>
      </router-link>
    </div>
  </div>
</div>
</template>

<script>
// import SlideView from '@/views/slide/SlideView.vue';
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: 'HomeView',
  data() {
    return {
      recommend: "",
      hero : this.$store.state.loginUser.nickname,
    }
  },
  computed:{
    isLogin(){
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.updateUserProfile(); // 컴포넌트가 생성될 때 updateUserProfile 함수 호출
  },
  methods: {
    updateUserProfile() {
      axios({
        method: "get",
        url: `${API_URL}/dj-rest-auth/user/${this.$store.state.loginUser.id}/recommend/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.recommend = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getProductDetailLink(productId) {
      const depositProduct = this.$store.state.deposit.find(product => product.id === productId);
      
      if (depositProduct) {
        console.log('d',productId)
        return { name: 'd_product_detail', params: { productId: productId } };
      } else {
        console.log('i',productId)
        return { name: 'i_product_detail', params: { productId: productId } };
      }
    },
  },
}

</script>

<style scoped>
div{
  font-family: "NanumSquareRound";
}

#at_box {
  border: 2px solid rgb(250, 213, 132);
  margin: 15px;
  padding: 20px;
  border-radius: 20px;
  font-family: "NanumSquareRound";
}

</style>