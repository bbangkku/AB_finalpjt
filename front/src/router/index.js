import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
// accounts view 추가
import SignupView from "@/views/accounts/SignupView";
import LoginView from "@/views/accounts/LoginView";
import ProfileView from "@/views/accounts/ProfileView";
import ProfileUpdateView from "@/views/accounts/ProfileUpdateView";
// community
import ArticleView from "@/views/community/ArticleView";
import CreateView from "@/views/community/CreateView";
import UpdateView from "@/views/community/UpdateView";
import ArticleDetailView from "@/views/community/ArticleDetailView";
// bank_api
import DepositView from '@/views/bank_api/DepositView.vue'
import InstallmentView from '@/views/bank_api/InstallmentView.vue'
import DepositDetail from '../components/deposit/DepositDetail.vue'
import InstallmentDetail from '../components/installment/InstallmentDetail.vue'
// exchange
import ExchangeView from '../views/exchange/ExchangeView.vue'
// map
import MapView from '../views/map/MapView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
// acccounts
  {
    path: "/signup",
    name: "signup",
    component: SignupView
  },

  {
    path: "/login",
    name: "login",
    component: LoginView,
  },

  {
    path: "/profile",
    name: "profile",
    component: ProfileView,
  },
  {
    path: "/profile/update",
    name: "profile_update",
    component: ProfileUpdateView,
  },
  // community
  {
    path: "/community",
    name: "article_view",
    component: ArticleView,
  },

  {
    path: "/community/create",
    name: "article_create",
    component: CreateView,
  },

  {
    path: "/community/:id",
    name: "article_detail",
    component: ArticleDetailView,
  },
  {
    path: "/community/:id/update",
    name: "article_update",
    component: UpdateView,
  },
  // bank_api
  {
    path: '/deposit',
    name: 'deposit',
    component: DepositView
  },
  {
    path: '/installment',
    name: 'installment',
    component: InstallmentView
  },
  // 상세페이지
  {
    path: '/deposit_product/:productId',
    name: 'd_product_detail',
    component: DepositDetail,
  },
  {
    path: '/installment_product/:productId',
    name: 'i_product_detail',
    component: InstallmentDetail,
  },
   // 환율
   {
    path: '/exchange',
    name: 'exchange',
    component: ExchangeView ,
  },
   // 지도
   {
    path: '/map',
    name: 'map',
    component: MapView,
  },
  ]

  const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })

export default router
