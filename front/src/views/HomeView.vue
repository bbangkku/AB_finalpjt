<template>
  <div>
    
    <!-- <SlideView @imageClick="handleImageClick" /> -->
  </div>
</template>

<script>
// import SlideView from '@/views/slide/SlideView.vue';

export default {
  name: 'HomeView',
    data () {
      return {
        drawer: true,
        tab: null,
        items: [
          { title: 'Home', icon: 'mdi-home-city' },
          { title: 'My Account', icon: 'mdi-account' },
          { title: 'Community', icon: 'mdi-account-group-outline' },
          { title: '환율계산기', icon : 'mdi-currency-cny'},
          { title : '예금/적금', icon: 'mdi-database-plus'},
          { title: '은행찾기', icon: 'mdi-google-maps'},
        ],
        mini: true,
      }
    },
    components: {
    // SlideView,
  },
  methods: {
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
  }
</script>
