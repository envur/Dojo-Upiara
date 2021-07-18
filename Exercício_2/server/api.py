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
    media = 0
    post_data = request.get_json()
    global NUMBERS
    NUMBERS = post_data.get("numbers")

    for p in range(0, len(NUMBERS)):
        if not isinstance(NUMBERS[p], int):
            response_object = {
                'Mensagem': "Existem valores inválidos!"
            }
            return jsonify(response_object)

    soma = 0
    for i in range(0,len(NUMBERS)):
        soma = soma + NUMBERS[i]
    
    if len(NUMBERS) > 0:
        media = soma/len(NUMBERS)

    for j in range(0, len(NUMBERS)):
        if NUMBERS[j] > media:
            NUMBERSMED.append(NUMBERS[j])
    

    for k in range(0, len(NUMBERS)):
        if NUMBERS[k] < 7:
            NUMBERS7.append(NUMBERS[k])

            
    response_object = {
    'amount':len(NUMBERS),
    'sequence':NUMBERS, 
    'reversed':list(reversed(NUMBERS)),
    'sum':soma,
    'average':media,
    'above_average':NUMBERSMED,
    'bellow_seven':NUMBERS7
    }    
    return jsonify(response_object)

NUMBERS = []

if __name__ == '__main__':
    app.run()