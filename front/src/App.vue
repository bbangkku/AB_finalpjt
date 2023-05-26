<template>
  <div id="app">
    <img src="@/assets/main.png" style="width:100%">
      <v-card class="custom-card">
        <v-tabs
        fixed-tabs
        bg-color="teal-darken-3"
        slider-color="teal-lighten-3"
        v-model="tab"
        align-tabs="center"
        show-arrows
      >
        <v-tab to="/">Home</v-tab>
        <v-tab to="/deposit">예금/적금 비교</v-tab>
        <v-tab to="/map">은행찾기</v-tab>
        <v-tab to="/exchange">환율계산기</v-tab>
        <v-tab to="/community">게시판</v-tab>
        <v-tab to="/profile">프로필</v-tab>
        <v-tab to="/login" v-if="!isLogin">로그인</v-tab>
        <v-tab @click="logout" v-if="isLogin">로그아웃</v-tab>
      </v-tabs>
      <v-window>
        <router-view :key="$route.fullPath"></router-view>
      </v-window>
    </v-card>

    <div id="with_aris">
      <div id="aris_bb" v-if="isLogin && num !== 3">
        <div class="bubble_box" @click="aris()">
          <div class="speech-bubble">
            <div>
              <h4>{{ message1 }}</h4>
              <h4>{{ message2 }}</h4>
            </div>
          </div>
        </div>
        <div id="aris">
          <img :src="image_url" style="width:380px">
        </div>
      </div>
    </div>
</div>
</template>

<script>
// import { throws } from 'assert';

export default {
  name: 'App',
  data() {
    return {
      tab: '',
      loginUser:{},
      num : 0,
      message1: '',
      message2: '',
      path :'',
      hero : this.$store.state.loginUser.nickname,
      image_url : require('@/assets/a1.png')
    };
  },
  created() {
    // 초기 메시지 설정
    this.updateMessage(this.$route.path);
    this.path = this.$route.path
  },
  computed:{
    isLogin(){
      return this.$store.getters.isLogin
    }
  }
  ,
  watch: {
    $route(to, from){
      this.updateMessage(to.path);
      console.log('응애',to.path.name)
      console.log('출발',from)
      console.log('도착',to)
    }
  },
  methods:{
    // 로그아웃
    logout() {
      this.$store.dispatch("logout");
    },
    aris(){
      console.log('passss',this.path)
      // HOME
      if (this.num === 0 && this.path==='/'){
        this.num += 1
        this.image_url = require('@/assets/a2.png')
        this.message1 =  `${this.hero} 용사님 환영합니다!`
        this.message2 = '개인 맞춤형 추천 상품을 눌러보세요 !'
      } else if (this.num===1 && this.path==='/') {
        this.num = 0
        this.image_url = require('@/assets/a3.png')
        this.message1 = '지금부터 아리스랑 모험을 떠나요'
        this.message2 =  '상단바를 눌러 이동하세요 !'
        
      }
      // 예금 
      else if (this.path ==='/deposit' && this.num === 0){
        this.num = 1
        this.image_url = require('@/assets/a1.png')
        this.message1 = '버튼을 누르면 적금 상품을 볼 수 있어요'
        this.message2 = "적금과 예금 상품을 비교해보세요 !"
      } else if ( this.path ==='/deposit' && this.num ===1){
        this.num = 0
        this.image_url = require('@/assets/a4.png')
        this.message1 = '상단 배너를 클릭하면 대표 상품의'
        this.message2 = "상세 정보를 확인할 수 있어요 !"
      }
      // 적금
      else if (this.path ==='/installment' && this.num === 0){
        this.num = 1
        this.image_url = require('@/assets/a1.png')
        this.message1 = '버튼을 누르면 예금 상품을 볼 수 있어요'
        this.message2 = "적금과 예금 상품을 비교해보세요 !"
      } else if ( this.path ==='/installment' && this.num ===1){
        this.num = 0
        this.image_url = require('@/assets/a2.png')
        this.message1 = '상단 배너를 클릭하면 대표 상품의'
        this.message2 = "상세 정보를 확인할 수 있어요 !"
      }
      // 예금 상세
      else if (this.path ===`/deposit_product/${this.$route.params.productId}` && this.num === 0){
        this.num = 1
        this.image_url = require('@/assets/a3.png')
        this.message1 = '가입한 상품은 프로필에서'
        this.message2 = '확인할 수 있어요 !'
      }
      else if(this.path ===`/deposit_product/${this.$route.params.productId}` && this.num === 1){
        this.num = 0
        this.image_url = require('@/assets/a1.png')
        this.message1 = '이곳은 제품 상세 페이지입니다 !'
        this.message2 = '상품에 가입해보세요!'
      }
      // 적금 상세
      else if (this.path ===`/installment_product/${this.$route.params.productId}` && this.num === 0){
        this.num = 1
        this.image_url = require('@/assets/a2.png')
        this.message1 = '가입한 상품은 프로필에서'
        this.message2 = '확인할 수 있어요 !'
      }
      else if(this.path ===`/installment_product/${this.$route.params.productId}` && this.num === 1){
        this.num = 0
        this.image_url = require('@/assets/a1.png')
        this.message1 = '이곳은 제품 상세 페이지입니다 !'
        this.message2 = '상품에 가입해보세요!'
      }
      // map
      else if (this.path ==='/map' && this.num === 0){
        this.num = 1
        this.image_url = require('@/assets/a1.png')
        this.message1 = '짜잔- 지도 페이지 입니다 !'
        this.message2 = '근처 은행의 위치를 알 수 있습니다 !'
      }
      else if(this.path ==='/map' && this.num === 1){
        this.num = 0
        this.image_url = require('@/assets/a2.png')
        this.message1 = '가고싶은 은행을'
        this.message2 = '검색해보세요 !'
      }
      // 환율계산기
      else if (this.path ==='/exchange' && this.num === 0){
        this.num = 1
        this.image_url = require('@/assets/a3.png')
        this.message1 = '환율을 계산하는 곳입니다 !'
        this.message2 = '매입율과 매도율을 정렬도 할 수 있어요 !!'
      }
      else if(this.path ==='/exchange' && this.num === 1){
        this.num = 0
        this.image_url = require('@/assets/a2.png')
        this.message1 = '아리스는 엔화를 가장 좋아합니다 !'
        this.message2 = '부자가 될거에요 !'
      }
      // 게시판
      else if (this.path ==='/community' && this.num === 0){
        this.num = 1
        this.image_url = require('@/assets/a4.png')
        this.message1 = '사람들과 소통할 수 있는 게시판 입니다 !'
        this.message2 = '다양한 의견을 나눌 수 있어요 !'
      }
      else if(this.path ==='/community' && this.num === 1){
        this.num = 2
        this.image_url = require('@/assets/a3.png')
        this.message1 = '올바른 게시판 문화 형성을 위해'
        this.message2 = '건전한 글만 작성해주세요 !'
      }
      else if(this.path ==='/community' && this.num === 2){
        this.num = 3
      }
      // 프로필
      else if(this.path ==='/profile' && this.num === 0){
        this.num = 1
        this.image_url = require('@/assets/a2.png')
        this.message1 = '수정하기 버튼을 눌러'
        this.message2 = '원하는 내용을 수정할 수 있어요 !'
      }
      else if(this.path ==='/profile' && this.num === 1){
        this.num = 3
      }

    },
    updateMessage(path){
      console.log('num',this.num)
      console.log('path',path)
      // 예금
      if (path==='/deposit'){
        this.num = 0
        this.image_url = require('@/assets/a4.png')
        this.message1 = '이곳은 예금 상품 페이지입니다!'
        this.message2 = '상품명을 클릭해보세요'
        this.path = '/deposit'
      }
      // 적금
      else if (path === '/installment'){
        this.num = 0
        this.image_url = require('@/assets/a1.png')
        this.message1 = '이곳은 적금 상품 페이지입니다!'
        this.message2 = '상품명을 클릭해보세요'
        this.path = '/installment'
      } 
      // home
      else if(path ==='/'){
        this.num = 0
        this.path = '/'
        this.message1 =  `${this.hero} 용사님 환영합니다!`
        this.message2 = '개인 맞춤형 추천 상품을 눌러보세요 !'
      }
      // 예금 상세
      else if(path ===`/deposit_product/${this.$route.params.productId}`){
        this.num = 0
        this.image_url = require('@/assets/a2.png')
        this.message1 = '이곳은 제품 상세 페이지입니다 !'
        this.message2 = '상품에 가입해보세요!'
        this.path = `/deposit_product/${this.$route.params.productId}`
      }
      // 적금 상세
      else if(path ===`/installment_product/${this.$route.params.productId}`){
        this.num = 0
        this.message1 = '이곳은 제품 상세 페이지입니다 !'
        this.message2 = '상품에 가입해보세요!'
        this.path = `/installment_product/${this.$route.params.productId}`
      }
      // 지도
      else if(path ==='/map'){
        this.num = 0
        this.path = '/map'
        this.image_url = require('@/assets/a2.png')
        this.message1 = '짜잔- 지도 페이지 입니다 !'
        this.message2 = '근처 은행의 위치를 알 수 있습니다 !'
      }
      // 환율계산기
      else if(path ==='/exchange'){
        this.num = 0
        this.path = '/exchange'
        this.message1 = '환율을 계산하는 곳입니다 !'
        this.message2 = '매입율과 매도율을 정렬도 할 수 있어요 !!'
      }
      // 게시판
      else if(path ==='/community'){
        this.path = '/community'
        this.image_url = require('@/assets/a4.png')
        this.num = 0
        this.message1 = '사람들과 소통할 수 있는 게시판 입니다 !'
        this.message2 = '다양한 의견을 나눌 수 있어요 !'
      }
      // 프로필
      else if(path ==='/profile'){
        this.num = 0
        this.path = '/profile'
        this.image_url = require('@/assets/a2.png')
        this.message1 = '용사님의 정보를 볼 수 있는 '
        this.message2 = '프로필페이지 입니다 !'
      }
    }
  }
}
</script>


<style>
/* 동글고딕 */
@font-face {
    font-family: 'Cafe24Ssurround';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2105_2@1.0/Cafe24Ssurround.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
/* 써라운드에어 */
@font-face {
    font-family: 'Cafe24SsurroundAir';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2105_2@1.0/Cafe24SsurroundAir.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
/* 나눔바른고딕 */
@font-face {
  font-family: 'NanumBarunGothic';
  font-style: normal;
  font-weight: 700;
  src: url('//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWebBold.eot');
  src: url('//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWebBold.eot?#iefix') format('embedded-opentype'), url('//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWebBold.woff') format('woff'), url('//cdn.jsdelivr.net/font-nanumlight/1.0/NanumBarunGothicWebBold.ttf') format('truetype')
}
/* 모바일고딕 */
@font-face {
    font-family: 'ONE-Mobile-Title';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2105_2@1.0/ONE-Mobile-Title.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
/* 나눔스퀘어라운드 */
@font-face {
    font-family: 'NanumSquareRound';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/NanumSquareRound.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
/* 태백은하수 */
@font-face {
    font-family: 'TAEBAEKmilkyway';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/TAEBAEKmilkyway.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}

h4{
  margin: 4px;
}

#aris {
  width: 450px;
  height: 390px;
  position: fixed;
  bottom:-18%;
  /* top:64%; */
  /* left: 130; */
  right: 0;
  z-index: 100;
  margin: 0;
  padding: 0;
}

#aris_bb{
  position: fixed;
  z-index: 1000000;
  right:100px;
  bottom: 260px;
}
.bubble_box{
  width: 400px;
  height: 140px;
  /* z-index: 1000000; */
  font-family: 'TAEBAEKmilkyway';
  font-weight: bolder;
}

.speech-bubble {
  position: relative;
  /* display: inline-block; */
  width: 300px;
  right:-100px;
  top: 100px;
  bottom: -20px;
  padding: 10px;
  background-color: #c6efff;
  border-radius: 8px;
  /* z-index: 1000000; */

}

.speech-bubble::before {
  content: "";
  position: absolute;
  top: 100%;
  left: 130px;
  border-width: 13px;
  border-style: solid;
  border-color: #c6efff transparent transparent transparent;
  /* border: #0a0a0a; */
}

body {
  display: flex;
  justify-content: center;
  margin-right: 0;
  background-color: #fcf7e8;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 70%;
  align-self: center;
  margin: 0;
}

nav {
  padding: 30px;
  background-color: #fcf7e8;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  background-color: #fcf7e8;
}

/* nav a.router-link-exact-active {
  color: #42b983;
} */
#link_txt {
  text-decoration: none;
  color: rgb(11, 12, 99);
  font-weight: 700;
  
}
#btn_style1 {
  background-color: #fff4b5;
  text-decoration: none;
  color: rgb(74, 74, 75);
  font-weight: 700;
}

#btn_style2 {
  background-color: #fff4b5;
  text-decoration: none;
  color: rgb(74, 74, 75);
  font-weight: 700;
}
.search_bar {
  width: 300px;
  text-align: center;
  /* display: flex; */
  /* justify-content: end; */

}

#box1 {
  display: flex;
  justify-content: space-between;
  align-items: end;

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
h1 {
  margin-top: 30px;
}

.centered-tabs {
  display: flex;
  justify-content: center;
}

</style>
<style scoped>
a {
  background: #fff4b5;
  font-family: 'ONE-Mobile-Title';
  font-weight: bold;
  font-size: 15px;
}
div.v-tab {
  background: #fff4b5;
  font-family: 'ONE-Mobile-Title';
  font-weight: bold;
  font-size: 15px;
}

div.v-tabs v-tabs--fixed-tabs theme--light{
  background: #fff4b5;
}
</style>