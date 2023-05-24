<template>
  <div>
    <div class="splide" ref="splide">
      <div class="splide__track">
        <ul class="splide__list">
          <li v-for="(image, index) in images" :key="index" class="splide__slide" @click="getId(index)">
            <router-link :to="{ name: 'd_product_detail', params: { productId: getProductById(index) } }" id="link_txt">
              <img :src="image" alt="Slide Image" style="max-width: 100%; height:auto;" />
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import '@splidejs/splide/dist/css/themes/splide-default.min.css';

export default {
  name: 'D_SlideView',
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
        require('@/assets/installment/국민1.png'),
        require('@/assets/installment/기업1.png'),
        require('@/assets/installment/농협1.png'),
        require('@/assets/installment/신한1.png'),
        require('@/assets/installment/카카오1.png'),
      ],
    };
  },
  methods: {
      getId(index) {
      const productId = this.getProductById(index);
      console.log(productId); // productId 값 확인
      if (productId && this.isDifferentRoute(productId)) {
        this.$router.push({ name: 'd_product_detail', params: { productId: productId } });
      }
    },

    getProductById(index) {
      if (index === 0) {
        return '010300100335'; // 국민
      } else if (index === 1) {
        return '01211310121'; // 국민
      } else if (index === 2) {
        return '10-003-1384-0001'; // 농협
      } else if (index === 3) {
        return 'WR0001B'; // 신한
      } else if (index === 4) {
        return '10-01-20-388-0002'; // 카카오
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