<template>
    <div class="container">
        <button type="button" class="btn btn-danger btn-lg">{{ msg }}</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'numbers',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getResults() {
      const path = 'http://localhost:5000/numbers';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        });
    },
  },
  created() {
    this.getResults();
  },
};
</script>
