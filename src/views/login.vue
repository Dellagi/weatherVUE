<template>
    <loginPage v-on:log="login" :connected='connected'/>
</template>

<script>
// @ is an alias to /src
import loginPage from '@/components/loginPage.vue'
import axios from 'axios';
import qs from 'qs';

export default {
  name: 'login',
  data:()=>({
    connected:0
  }),
  components: {
    loginPage
  },
  methods:{
    login(inf){
      const{name,pass}=inf;
      axios.post('http://localhost:5000/login',qs.stringify({
      name,
      passw:pass
    }))
      .then(res =>{ if (res.data=='oki'){localStorage.setItem('logininfo',res.data);this.$router.push('/');this.connected=0;} else{this.connected=1}})
      .catch(err => console.log(err))
  }
  }
}
</script>
