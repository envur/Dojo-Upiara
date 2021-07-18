import Vue from 'vue';
import VueRouter from 'vue-router';
import Taxes from '../components/Taxes.vue';

Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [{
    path: '/taxes',
    name: 'Taxes',
    component: Taxes,
  }],
});

export default router;
