<template>
    <div class="container">
        <h1>Dojo Upiara - Exercício 3</h1><hr><br>
        <h4>Insira o quanto você ganha por hora e quantas horas você trabalhou no mês.<br>
            Caso tenha inserido um valor errado, clique em limpar.<br>
            Quando terminar, clique em resultados.</h4>
        <br><br>
        <div>
          <input class="form-control form-control-md"
                 placeholder="Insira o quanto você ganha por hora"
                 v-model.number="valueSalary"><br>
          <button class="btn btn-primary btn-lg" @click="addSalary">Adicionar Salário</button>
        </div>
        <div>
          <br><input class="form-control form-control-md"
                 placeholder="Insira as horas trabalhadas"
                 v-model.number="valueHours"><br>
          <button class="btn btn-primary btn-lg"
                  @click="addHours">Adicionar Horas Trabalhadas</button>
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
      valueSalary: '',
      valueHours: '',
      salary: '',
      workingHours: '',
      grossSalary: '',
      inss: '',
      renda: '',
      sindicato: '',
      liquidSalary: '',
    };
  },
  methods: {
    clearValues() {
      this.salary = null;
      this.workingHours = null;
    },
    addSalary() {
      if (this.valueSalary > 0) {
        this.salary = this.valueSalary;
        this.valueSalary = null;
      }
    },
    addHours() {
      if (this.valueHours > 0) {
        this.workingHours = this.valueHours;
        this.valueHours = '';
      }
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
    },
  },
};
</script>
