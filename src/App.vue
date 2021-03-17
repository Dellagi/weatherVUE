<template>
  <v-app >
    <v-main>
      <router-view/>
      
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    page:null
  })


}
</script>
<style scoped>
main {
  background-color: rgb(51, 102, 153);
  background-size:100% 100%;
}
</style>