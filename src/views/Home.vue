<template>
  <div class="home">



    <v-app-bar
      app
      color="rgb(64, 128, 191)"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://openweathermap.org/themes/openweathermap/assets/img/logo_white_cropped.png"
          transition="scale-transition"
          width="80"
        />
      </div>
      <v-btn
        @click="page=1"
        text
      >
        <span class="mr-2">Search for city</span>
      </v-btn>

      <v-btn
        @click="page=2"
        text
      >
        <span class="mr-2">Your favorite cities</span>
      </v-btn>





      <v-spacer></v-spacer>

      <v-btn
        @click="logOut"
        text
      >
        <span class="mr-2">Log Out</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>









<div v-if="page==2">
<favorite />
</div>


<div v-if="page==1">
<minute v-bind:country="country" />
</div>





  </div>
</template>

<script>
// @ is an alias to /src
import minute from './minute.vue'
import favorite from './favorite.vue'


export default {
  name: 'Home',
  components:{minute,favorite},
  data: () => ({
    page:1
  }),
  methods:{
    async logOut(){
      try{
        localStorage.removeItem('logininfo'); 
        await this.$router.push('/login')
        }catch (error) {
        throw new Error(`Error: ${error}`);
      }
  }
  },



  

}
</script>
