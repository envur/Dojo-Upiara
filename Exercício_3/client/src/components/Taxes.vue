<template>
    <div class="container">
        <h1>Dojo Upiara - Exercício 3</h1><hr><br>
        <h4>Insira o quanto você ganha por hora e quantas horas você trabalhou no mês.<br>
            Caso tenha inserido um valor errado, clique em limpar.<br>
            Quando terminar, clique em resultados.</h4>
        <br>
        <b-alert
        :show="dismissCountDown"
        dismissible
        variant="danger"
        @dismissed="dismissCountDown=0"
        @dismiss-count-down="countDownChanged">
        <p> {{ msg }} </p>
        <b-progress
          variant="danger"
          :max="dismissSecs"
          :value="dismissCountDown"
          height="2px">
        </b-progress>
    </b-alert>
        <div>
          <input class="form-control form-control-md"
                 placeholder="Insira o quanto você ganha por hora"
                 v-model.number="salary"><br>
        </div>
        <div>
          <br><input class="form-control form-control-md"
                 placeholder="Insira as horas trabalhadas"
                 v-model.number="workingHours"><br>
        </div>
        <div class="col-lg-12" style="text-align: center"><br><br><br><br>
          <button class="btn btn-success btn-lg" @click="sendValues">Resultados</button>
          <button class="btn btn-secondary btn-lg" @click="clearValues">Limpar</button>
        </div>
        <b-modal ref="ResultsModal"
                 id="results-modal"
                 title="Resultados"
                 hide-footer>
                 <template>
                   Salário Bruto: {{ grossSalary }} <br>
                   Valor pago ao INSS: {{ inss }} <br>
                   Valor pago de imposto de renda: {{ renda }} <br>
                   Valor pago ao sindicato: {{ sindicato }} <br>
                   Salário Líquido: {{ liquidSalary }} <br>
                   </template>
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Taxes',
  data() {
    return {
      salary: '',
      workingHours: '',
      grossSalary: '',
      inss: '',
      renda: '',
      sindicato: '',
      liquidSalary: '',
      msg: '',
      dismissSecs: 10,
      dismissCountDown: 0,
    };
  },
  methods: {
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    clearValues() {
      this.salary = null;
      this.workingHours = null;
    },
    sendValues() {
      const path = 'http://localhost:5000/taxes';
      const payload = {
        salary: this.salary,
        workingHours: this.workingHours,
      };
      if (this.salary > 0 || this.workingHours > 0) {
        axios.post(path, payload)
          .then((res) => {
            this.grossSalary = res.data.gross;
            this.inss = res.data.inss;
            this.renda = res.data.renda;
            this.sindicato = res.data.sindicato;
            this.liquidSalary = res.data.liquid;
            this.$bvModal.show('results-modal');
            this.salary = '';
            this.workingHours = '';
          });
      }
      if (this.salary === '' || this.workingHours === '') {
        this.dismissCountDown = this.dismissSecs;
        this.msg = 'Você não preencheu algum dos campos obrigatórios!';
      }
    },
  },
};
</script>
