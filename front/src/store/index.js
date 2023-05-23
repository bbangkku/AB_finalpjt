import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import createPersistedState from "vuex-persistedstate";
import router from "../router";
// import jwtDecode from "jwt-decode"; // 이거 해석해보자

const API_URL = "http://127.0.0.1:8000";
const DEPOSIT_PRODUCT_URL = API_URL + "/bank_api/deposit/";
const INSTALLMENT_PRODUCT_URL = API_URL + "/bank_api/installment/";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    token: "", // 게시글쓰려면 토큰있어야지!
    articles: [],
    loginUser: {},
    deposit: [],
    installment: [],
    depositLoaded: false, // deposit 데이터 로드 상태를 저장하는 변수
    installmentLoaded: false, // installment 데이터 로드 상태를 저장하는 변수
    // 환율
    exchange: null,
  },
  getters: {
    isLogin(state) {
      return Object.keys(state.loginUser).length === 0 ? false : true;
    },
    getToken(state) {
      return state.token;
    },
    getProfile(state) {
      return state.loginUser;
    },
    likeProducts(state) {
      return state.likeProducts;
    },
  },
  mutations: {
    // 로그인과 토큰 저장
    SAVE_TOKEN(state, token) {
      state.token = token;
      axios({
        method: "get",
        url: `${API_URL}/dj-rest-auth/user/`,
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then((res) => {
          console.log(res);
          state.username = res.data.username;
          state.userid = res.data.pk;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // 로그아웃
    LOGOUT(state) {
      state.loginUser = {};
    },

    // 게시글 가져오기
    GET_ARTICLES(state, articles) {
      state.articles = articles;
    },
    GETEXCHANGE(state, data) {
      state.exchange = data;
    },
    GO_LOGIN(state, data) {
      state.loginUser = data;
    },
    SET_DEPOSIT(state, deposit) {
      state.deposit = deposit;
    },
    SET_INSTALLMENT(state, installment) {
      state.installment = installment;
    },
    SET_DEPOSIT_LOADED(state, loaded) {
      state.depositLoaded = loaded; // 데이터 로드 상태 업데이트
      console.log("d업뎃");
    },
    SET_INSTALLMENT_LOADED(state, loaded) {
      state.installmentLoaded = loaded; // 데이터 로드 상태 업데이트
      console.log("i업뎃");
    },
    // 환율
    GET_EXCHANGE(state, data) {
      state.exchange = data;
    },
  },
  actions: {
    // 회원가입
    signUp(context, payload) {
      const username = payload.username;
      const password1 = payload.password1;
      const password2 = payload.password2;
      const gender = payload.gender;
      const age = payload.age;
      const salary = payload.salary;
      const nickname = payload.nickname;
      const money = payload.money;
      const bank = payload.bank;
      axios({
        method: "post",
        url: `${API_URL}/dj-rest-auth/registration/`,
        data: {
          username,
          nickname,
          password1,
          password2,
          gender,
          age,
          salary,
          money,
          bank,
        },
      })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    // 로그인 & 토큰얻기
    login({ dispatch, commit }, payload) {
      const username = payload.username;
      const password = payload.password;
      axios({
        method: "post",
        url: `${API_URL}/dj-rest-auth/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          localStorage.setItem("Token", res.data.key);
          dispatch("getUser");
          commit("SAVE_TOKEN", res.data.key);
          router.push({ name: "ArticleView" });
        })
        .catch((err) => {
          console.log(err);
          alert("아이디 또는 비밀번호가 잘못되었습니다.");
        });
    },
    getUser(context) {
      axios({
        method: "get",
        url: `${API_URL}/dj-rest-auth/user/`,
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then((res) => {
          console.log("이거야 제발", res);
          context.commit("GO_LOGIN", res.data);
          console.log("sssssssssssssss", JSON.stringify(res.data));
          localStorage.setItem("login-user", JSON.stringify(res.data));
        })
        .catch((err) => {
          console.log(err);
        });
    },

    // 로그아웃
    logout({ commit }) {
      localStorage.removeItem("Token");
      localStorage.removeItem("login-user");
      commit("LOGOUT");
      router.push({ name: "LogInView" });
    },

    // 게시글 가져오기
    getArticles(context) {
      console.log("getArticles옴");
      const token = context.state.token;
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${token}`,
        },
        params: {
        },
      })
        .then((res) => context.commit("GET_ARTICLES", res.data))
        .catch((err) => console.log(err));
    },
    getDeposit(context) {
      if (!context.state.depositLoaded) {
        axios
        console.log(DEPOSIT_PRODUCT_URL)
          .get(DEPOSIT_PRODUCT_URL)
          .then((response) => {
            context.commit("SET_DEPOSIT", response.data);
            context.commit("SET_DEPOSIT_LOADED", true); // 데이터 로드 상태 업데이트
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    getInstallment(context) {
      if (!context.state.installmentLoaded) {
        axios
          .get(INSTALLMENT_PRODUCT_URL)
          .then((response) => {
            context.commit("SET_INSTALLMENT", response.data);
            context.commit("SET_INSTALLMENT_LOADED", true); // 데이터 로드 상태 업데이트
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    // 환율
    getExch(context) {
      if (!this.state.exchange) {
        axios({
          method: "get",
          url: `${API_URL}/exchange/`,
        }).then((res) => {
          console.log(res, context);
          context.commit("GET_EXCHANGE", res.data);
        });
      }
    },
  },
});