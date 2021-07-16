from flask import Flask, jsonify, request
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/numbers', methods=['POST'])
def post_numbers():
    NUMBERSMED = []
    NUMBERS7 = []
    post_data = request.get_json()
    global NUMBERS
    NUMBERS = post_data.get("numbers")

    soma = 0
    for i in range(0,len(NUMBERS)):
        soma = soma + NUMBERS[i]
    
    media = soma/len(NUMBERS)

    for j in range(0, len(NUMBERS)):
        if NUMBERS[j] > media:
            NUMBERSMED.append(NUMBERS[j])
    

    for k in range(0, len(NUMBERS)):
        if NUMBERS[k] < 7:
            NUMBERS7.append(NUMBERS[k])

            
    response_object = {
    'Qtd. Números':len(NUMBERS),
    'Ordem':NUMBERS, 
    'Ordem Inversa':list(reversed(NUMBERS)),
    'Soma dos Números':soma,
    'Média dos Números':media,
    'Valores Acima da Média':NUMBERSMED,
    'Valores Abaixo de 7':NUMBERS7
    }    
    return jsonify(response_object)

NUMBERS = []

if __name__ == '__main__':
    app.run()