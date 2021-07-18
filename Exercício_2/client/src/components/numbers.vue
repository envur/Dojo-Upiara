<template>
    <div class="container">
        <h1>Dojo Upiara - Exercício 2</h1><hr><br>
        <h3>Insira os números a seguir e confirme para receber os resultados,<br>
            ou clique em "Menos 1!" para apagar os números já inseridos.</h3>
        <br><br>
        <div>
          <input class="form-control form-control-md"
                 placeholder="Insira um número inteiro positivo"
                 v-model.number="number">
        </div>
        <div class="col-lg-12" style="text-align: center"><br><br>
          <button class="btn btn-primary btn-lg" @click="newNumber">Novo número</button><br><br>
          <button class="btn btn-success btn-lg" @click="sendNumbers">Resultados</button>
          <button class="btn btn-secondary btn-lg" @click="clearNumbers">Menos 1!</button>
        </div>
        <b-modal ref="ResultsModal"
                 id="results-modal"
                 title="Resultados"
                 hide-footer>
                 <template>
                   Qtd. Números Inseridos: {{ amount }} <br>
                   Números Inseridos em Ordem: {{ sequence }} <br>
                   Ordem Inversa: {{ reverse }} <br>
                   Soma dos Números: {{ sum }} <br>
                   Média dos Números: {{average}} <br>
                   Números Acima da Média: {{ aboveAverage }} <br>
                   Números Abaixo de 7: {{ bellowSeven }}</template>
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'numbers',
  data() {
    return {
      number: '',
      numbers: [],
      sequence: '',
      reverse: '',
      amount: '',
      sum: '',
      average: '',
      aboveAverage: '',
      bellowSeven: '',
    };
  },
  methods: {
    clearNumbers() {
      this.numbers = [];
    },
    newNumber() {
      if (this.number > 0) {
        this.numbers.push(this.number);
        this.number = null;
      }
    },
    sendNumbers() {
      const path = 'http://localhost:5000/numbers';
      const payload = {
        numbers: this.numbers,
      };
      if (this.numbers.length > 0) {
        axios.post(path, payload)
          .then((res) => {
            this.amount = res.data.amount;
            this.sequence = res.data.sequence;
            this.reverse = res.data.reversed;
            this.sum = res.data.sum;
            this.average = res.data.average;
            this.aboveAverage = res.data.above_average;
            this.bellowSeven = res.data.bellow_seven;
            this.$bvModal.show('results-modal');
            this.numbers = [];
          });
      }
    },
  },
};
</script>
