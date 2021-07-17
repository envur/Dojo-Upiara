<template>
    <div class="container">
        <h1>Dojo Upiara - Exercício 2</h1><hr><br>
        <h3>Insira os números a seguir e confirme para receber os resultados,<br>
            ou clique em "Menos 1!" para cancelar.</h3>
        <br><br>
        <div>
          <input class="form-control form-control-md"
                 placeholder="Insira um número inteiro positivo"
                 v-model="number">
        </div>
        <div class="col-lg-12" style="text-align: center"><br><br>
          <button class="btn btn-primary btn-lg" @click="newNumber">Novo número</button><br><br>
          <button class="btn btn-success btn-lg" @click="sendNumbers">Resultados</button>
          <button class="btn btn-secondary btn-lg">Menos 1!</button>
        </div>
        <b-modal ref="ResultsModal"
                 id="results-modal"
                 title="Resultados"
                 hide-footer>
                 <template>

                 </template>

        </b-modal>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'numbers',
  data() {
    return {
      number: null,
      numbers: [],
    };
  },
  methods: {
    newNumber() {
      this.numbers.push(this.number);
      this.number = null;
    },
    sendNumbers() {
      const path = 'http://localhost:5000/numbers';
      const payload = {
        numbers: this.numbers,
      };
      axios.post(path, payload)
        .then((res) => {
          this.result = res.data.result;
          console.log('teste');
          this.$bvModal.show('results-modal');
          console.log('teste2');
          this.numbers = [];
          console.log('teste3');
        });
    },
  },
  created() {
    this.newNumber();
  },
};
</script>
