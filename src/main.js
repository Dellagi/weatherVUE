import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import Chart from 'chart.js';
import Chartkick from 'vue-chartkick';
Vue.use(Chartkick.use(Chart))

Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
