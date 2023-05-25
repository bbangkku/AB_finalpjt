<template>
  <div>
          <v-btn @click="updateUserProfile" id="btn" type="submit" rounded="sm" block size="x-large" color="#3F51B5">
            추천상품보기~~
          </v-btn>
          <div>{{recommend}}</div>
    <!-- <SlideView @imageClick="handleImageClick" /> -->
  </div>
</template>

<script>
// import SlideView from '@/views/slide/SlideView.vue';
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: 'HomeView',
    data () {
      return {
        recommend: "",
      }
    },
    components: {
    // SlideView,
  },
  methods: {
    updateUserProfile() {
      console.log()
      axios({
        method: "get",
        url: `${API_URL}/dj-rest-auth/user/${this.$store.state.loginUser.id}/recommend/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        }
      })
        .then((res) => {
          console.log('submit',res);
          this.recommend = res.data
        })
        .catch((err) => {
          console.log(err);
        });
  },
  }
}
</script>
