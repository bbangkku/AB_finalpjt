<template>
  <!-- <div></div> -->
  <div ref="map"></div>
</template>

<script>
export default {
  name : 'MapComponent',
  props: ['options'],
  data(){
    return {
      mapInstance: null
    }
  },
  mounted(){
    let kakao = window.kakao;
    console.log(this.$refs.map)
    // 지도를 찍어보자!
    var container = this.$refs.map;
    // var options = {
    //   center: new window.kakao.maps.LatLng(37.501281, 127.039598),
    //   level: 3,
    // };
    const {center, level} = this.options
    this.mapInstance = new kakao.maps.Map(container, {
      center : new kakao.maps.LatLng(center.lat, center.lng),
      level,
    });
    // console.log(this.mapInstance)
  },
  watch: {
    'options.level'(cur, prev) {
      console.log(`[LEVEL CHANGED] ${prev} => ${cur}`)
      this.mapInstance.setLevel(cur)
    }
  }
}
</script>

<style>

</style>