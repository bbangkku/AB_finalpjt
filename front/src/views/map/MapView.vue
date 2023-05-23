<template>
  <div>
    <h1>map c</h1>
    <!-- <div class="controll">
      <button @click="zoom(-1)"><span id="button1" class="material-symbols-outlined">add_box</span></button>
      <button @click="zoom(1)"><span class="material-symbols-outlined" id="button1">indeterminate_check_box</span></button>
    </div> -->

    <div class="big_map">
      <MapComponent class="kmap" :options="mapOption" ref="mapComponent" />
      <div class="searchbox">
        <v-text-field
          :loading="loading"
          density="compact"
          variant="solo"
          label="은행 검색"
          append-icon="mdi-magnify"
          single-line
          hide-details
          @keyup.enter="searchBank"
        ></v-text-field>
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
      const imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png';
      const imageSize = new window.kakao.maps.Size(24, 35);
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
  z-index: 10000;
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
  background-color: rgb(251, 228, 232);
}

h4 {
  margin: 0;
}

.kmap {
  flex: 1 1 auto;
  height: 600px;
}

.big_map {
  display: flex;
}
</style>