<template>

<div class="container">
    <div v-if="this.questStart===false" class="container my-5">
        <h1>Interrogatório</h1>
        <h2 class="mt-5">Houve um assassinato e você está sendo investigado.
          Por favor, responda as questões a seguir com sinceridade</h2>
        <button
        type="button"
        class="btn btn-success mt-4 btn-lg"
        v-on:click.stop.prevent = startQuest
        >Iniciar</button>
        <h1>{{this.histAnswes}}</h1>
    </div>
    <transition name="fade">
    <div v-if="this.questStart && this.questFinish == false"
    class="container my-5">
        <div class="row">
            <div class="col"></div>
            <div class="col-8">
                <h1>Questão {{this.index + 1}}</h1>
                <h2 class="text-center mt-5">{{questions[index]}}</h2>
                <div class="float-right">
                    <button type="button"
                    class="btn btn-success
                    mt-5 mr-3 btn-lg"
                    v-on:click.stop.prevent = getAnswerYes
                    >Sim</button>
                    <button type="button"
                    class="btn btn-danger
                    mt-5 mr-2 btn-lg"
                    v-on:click.stop.prevent = getAnswerNo
                    >Não</button>
                </div>
            </div>
            <div class="col"></div>
        </div>
    </div>
    </transition>
    <div v-if="this.questFinish" class="container mt-5 text-center">
        <h1>Resultado</h1>
        <h2 class="mt-5">{{result}}</h2>
        <button
        type="button"
        class="btn btn-primary mt-4 btn-lg"
        v-on:click.stop.prevent = resetQuest
        >Reiniciar</button>
    </div>
</div>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      questStart: false,
      questFinish: false,
      questions: ['Telefonou para a vítima?',
        'Esteve no local do Crime?',
        'Mora perto da vítima?',
        'Devia para a vítima?',
        'Já trabalhou com a vítima?'],
      index: 0,
      answers: [],
      result: '',
      histAnswes: [],
    };
  },

  methods: {
    startQuest() {
      this.questStart = true;
    },
    nextQuest() {
      this.index += 1;
      if (this.index === 5) {
        this.questFinished();
      }
    },
    getAnswerYes() {
      this.answers.push('sim');
      console.log(this.answers);
      this.nextQuest();
    },
    getAnswerNo() {
      this.answers.push('nao');
      console.log(this.answers);
      this.nextQuest();
    },
    questFinished() {
      this.questFinish = true;
      this.questResult();
    },
    questResult() {
      const path = 'http://localhost:5000/murder';
      const payload = {
        questions: this.questions,
        answers: this.answers,
      };
      axios.post(path, payload)
        .then((res) => {
          this.result = res.data.result;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    resetQuest() {
      this.questStart = false;
      this.questFinish = false;
      this.index = 0;
      for (let i = this.answers.length; i > 0; i -= 1) {
        this.answers.pop();
      }
    },
    getResults() {
      const path = 'http://localhost:5000/murder';
      axios.get(path)
        .then((res) => {
          this.histAnswes = res.data.result;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getResults();
  },
};
</script>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
