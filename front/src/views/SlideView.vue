<template>
  <div>
    <div class="splide" ref="splide">
      <div class="splide__track">
        <ul class="splide__list">
          <li v-for="(image, index) in images" :key="index" class="splide__slide" @click="getId(index)">
            <router-link :to="{ name: 'i_product_detail', params: { productId: getProductById(index) } }" id="link_txt">
              <img :src="image" alt="Slide Image" style="max-width: 100%; height: auto;" />
             
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import '@splidejs/splide/dist/css/themes/splide-skyblue.min.css';

export default {
  name: 'SlideView',
  data() {
    return {
      options: {
        type: 'fade',
        rewind: true,
        perPage: 1,
        autoplay: true,
        pauseOnHover: false,
        arrows: false,
        pagination: true,
        interval: 2000,
      },
      images: [
        require('@/assets/bank/kakao.png'),
        require('@/assets/bank/toss.png'),
        require('@/assets/bank/hana.png'),
        require('@/assets/bank/kb.png'),
        require('@/assets/bank/sh.png'),
      ],
    };
  },
  methods: {
      getId(index) {
  const productId = this.getProductById(index);
  console.log(productId); // productId 값 확인

  if (productId && this.isDifferentRoute(productId)) {
    this.$router.push({ name: 'i_product_detail', params: { productId: productId } });
  }
},

    getProductById(index) {
      if (index === 0) {
        return '10-01-30-355-0002'; // 카카오
      } else if (index === 1) {
        return '1001303001001'; // 토스
      } else if (index === 2) {
        return '53'; // 하나
      } else if (index === 3) {
        return '010200100092'; // 국민
      } else if (index === 4) {
        return '230-0118-07'; // 신한
      }
      return null;
    },
    isDifferentRoute(productId) {
      const currentRoute = this.$router.currentRoute;
      return currentRoute.name !== 'i_product_detail' || currentRoute.params.productId !== productId;
    },
  },
  mounted() {
    const Splide = require('@splidejs/splide').default;
    new Splide(this.$refs.splide, this.options).mount();
  },
};
</script>

<style>
/* 스타일은 생략했습니다. */
</style>