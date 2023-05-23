<template>
  <div>
    <DepositProduct/>
  </div>
</template>
<script>
import axios from 'axios'
import DepositProduct from '@/components/deposit/DepositProduct.vue';

export default {
  name: 'DepositView',
  components:{
    DepositProduct
  },
  created() {
    const BACKEND_URL = 'http://localhost:8000/bank_api/deposit/'
    axios.get(BACKEND_URL)
    .then((responese) => {
      console.log(responese)
    })
    .catch((error) => {
      console.log(error)
    })
  },
  data() {
    return{}
  }
  
}
</script>
<style lang="">
  
</style>