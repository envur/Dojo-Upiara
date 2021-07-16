import Vue from 'vue';
import Router from 'vue-router';
import Questions from '../components/Questions.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Questions',
      component: Questions,
    },
  ],
});
