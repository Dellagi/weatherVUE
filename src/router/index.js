import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import login from '../views/login.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: login

  },
  {
    path: '/',
    name: 'Home',
    component: Home

  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
router.beforeEach((to, from, next) => {
  const publicPages =['/login'];
  const authRequired=!publicPages.includes(to.path);
  const loggedIn =localStorage.getItem('logininfo');
  if (to.path==='/login' && loggedIn){
    return next('/');
  }else if (authRequired && !loggedIn){
    return next('/login');
  }
  next();
})
export default router
