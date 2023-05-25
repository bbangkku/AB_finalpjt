<template>
  <div class="ex">
    <h3>주변 은행을 검색해보세요 ! </h3>
    <div id='at_box'>
      <div class="big_map">
        <MapComponent class="kmap" :options="mapOption" ref="mapComponent" />
        <div class="searchbox">
          <div class="search_bar">
            <div class="input_box">
                <input type="text"
                :loading="loading"
                  density="compact"
                  variant="solo"
                  label="은행 검색"
                  single-line
                  hide-details
                  append-icon="mdi-map-marker"
                  required style="margin: 0;"
                  @keyup.enter="searchBank">
                <label for="search_bank">&nbsp; &nbsp;&nbsp;은행검색  🔍</label>
                <span class="span1"></span>
              </div>
          </div>

          <div class="results">
            <div class="place" v-for="rs in search.result" :key="rs.id" @click="showPlace(rs)">
              <h4>{{ rs.place_name }}</h4>
              <div class="addr">
                {{ rs.road_address_name }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MapComponent from '@/components/map/MapComponent.vue';

export default {
  name: 'MapView',
  data() {
    return {
      loaded: false,
      loading: false,
      mapOption: {
        center: {
          lat: 37.501281,
          lng: 127.039598
        },
        level: 5
      },
      search: {
        keyword: null,
        pgn: null,
        result: null,
      },
      mapInstance: null, // Add this line
      markers: [], // Add this line
    };
  },
  components: {
    MapComponent
  },
  mounted() {
    this.$nextTick(() => {
      this.mapInstance = this.$refs.mapComponent.mapInstance; // Update the reference
    });
  },
  methods: {
    // 화면 줌
    zoom(num) {
      const level = Math.max(3, this.mapOption.level + num);
      this.mapOption.level = level;
    },
    // 은행 검색
    searchBank(bank) {
      const keyword = bank.target.value.trim();
      if (keyword.length === 0) {
        return;
      }

      const ps = new window.kakao.maps.services.Places();
      ps.keywordSearch(keyword, (data, status, pgn) => {
        this.search.keyword = keyword;
        this.search.pgn = pgn;
        this.search.result = data;
        console.log(data);
        console.log('result', this.search.result);
        this.clearMarkers(); // Clear previous markers
        this.addMarkers(data); // Add new markers
      });
    },
    showPlace(place) {
      const position = new window.kakao.maps.LatLng(place.y, place.x);
      this.mapInstance.setCenter(position);
    },
    addMarkers(data) {
      const markers = [];
      const imageSrc = 'https://i.ibb.co/t3BjQRQ/bk.png';
      const imageSize = new window.kakao.maps.Size(45, 45);
      const imageOption = { offset: new window.kakao.maps.Point(12, 35) };

      for (let i = 0; i < data.length; i++) {
        const markerPosition = new window.kakao.maps.LatLng(data[i].y, data[i].x);
        const marker = new window.kakao.maps.Marker({
          position: markerPosition,
          image: new window.kakao.maps.MarkerImage(imageSrc, imageSize, imageOption),
        });

        markers.push(marker);
      }

      this.markers = markers; // Update markers array
      this.showMarkers(); // Display markers on the map
    },
    clearMarkers() {
      for (let i = 0; i < this.markers.length; i++) {
        this.markers[i].setMap(null);
      }

      this.markers = [];
    },
    showMarkers() {
      for (let i = 0; i < this.markers.length; i++) {
        this.markers[i].setMap(this.mapInstance);
      }
    },
  }
}
</script>

<style scoped>
#at_box{
  /* text-align: left; */
  width: 90%;
  border: 2px solid rgb(250, 213, 132);
  margin: 20px;
  padding: 35px;
  border-radius: 20px;
  font-family: 'NanumSquareRound';
  font-weight: lighter;
}

.material-symbols-outlined {
  font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 48;
}

#button1 {
  color: rgb(255, 160, 200);
  font-size: 30px;
}

#button1:hover {
  color: rgb(245, 98, 159);
}

#button1:active {
  color: rgb(255, 208, 227);
}

/* 지도 / 검색창 */
.map-area {
  display: flex;
  position: relative;
}

.searchbox {
  position: relative;
  top: 0;
  left: 0;
  height: 600px;
  /* z-index: 10000; */
  background-color: #ffffffaa;
  width: 300px;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

.results {
  flex: 1 1 auto;
  overflow-y: auto;
}

.place {
  padding: 8px;
  cursor: pointer;
}

.place:hover {
  background-color: rgb(251, 242, 224);
}

h4 {
  margin: 0;
}

h3 {
  padding:20px 10px 0px 10px;
  color: rgb(90, 90, 90);
  font-family: 'NanumSquareRound';
  /* font-weight: lighter; */
}

.kmap {
  flex: 1 1 auto;
  height: 600px;
}

.big_map {
  display: flex;
  justify-content: space-between;
}


/* 검색창 */
.input_box {
  position: relative;
  width: 300px;
  margin-top: 30px;
}

input {
  font-size: 15px;
  color: #222222;
  width: 200px;
  border: none;
  border-bottom: solid #aaaaaa 1px;
  padding-bottom: 10px;
  text-align: center;
  position: relative;
  background: none;
  z-index: 5;
}

input::placeholder { color: #aaaaaa; }
input:focus { outline: none; }

.span1 {
  display: block;
  position: absolute;
  bottom: 0;
  left: 50%; 
  background-color: #666;
  width: 0;
  height: 2px;
  border-radius: 2px;
  transform: translateX(-50%);
  transition: 0.3s;
}

label {
position: absolute;
color: #878787;
left: 50%;
transform: translateX(-50%);
font-size: 14px;
bottom: 8px;
transition: all .2s;
}

input:focus ~ label, input:valid ~ label {
font-size: 15px;
bottom: 40px;
color: #666;
font-weight: bold;
}

input:focus ~ span, input:valid ~ span {
width: 100%;
}

.ex {
  display: grid;
  justify-items: center;
  grid-template-columns: 1fr;
}


</style>