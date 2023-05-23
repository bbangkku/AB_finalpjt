<template>
  <div>
    <SlideView @imageClick="handleImageClick" />
    <v-toolbar>
      <v-toolbar-title>가을 병국 . .</v-toolbar-title>

      <v-spacer></v-spacer>
      <v-toolbar-title>LOGIN</v-toolbar-title>
      <v-toolbar-title>LOGOUT</v-toolbar-title>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
    </v-toolbar>

    <v-app id="inspire">
      <v-navigation-drawer
        v-model="drawer"
        :mini-variant.sync="mini"
        permanent
      >
        <v-list-item class="px-2">
          <v-list-item-avatar>
            <v-icon icon='mdi-chevron-double-right'>mdi-chevron-double-right</v-icon>
          </v-list-item-avatar>
  
          <v-list-item-title>MENU</v-list-item-title>
  
          <v-btn
            icon
            @click.stop="mini = !mini"
          >
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
        </v-list-item>
  
        <v-divider></v-divider>
  
        <v-list dense>
          <v-list-item
            v-for="item in items"
            :key="item.title"
            link
          >
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
  
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </v-app>
  <!-- </v-card> -->
  </div>
</template>

<script>
import SlideView from './SlideView.vue';

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
    SlideView,
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
