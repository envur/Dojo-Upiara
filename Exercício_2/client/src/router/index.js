import Vue from 'vue';
import VueRouter from 'vue-router';
import numbers from '../components/numbers.vue';

Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [{
    path: '/numbers',
    name: 'Numbers',
    component: numbers,
  }],
});

export default router;
