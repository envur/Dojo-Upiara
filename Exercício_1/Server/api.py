from logging import DEBUG
from flask import Flask, request, jsonify, Response
from flask_cors import CORS


#Configuração
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/murder', methods=['POST'])
def responder():     
    post_data = request.get_json()
    ANSWERS = post_data.get('answers')
    print(ANSWERS)
    sim = 0
    nao = 0
    for i in range(5):
        if ANSWERS[i] == "sim":
            sim = sim + 1
        elif ANSWERS[i] == "não":
            nao = nao + 1
    
    if sim == 5:
        response_object = {'result': 'Assassino'}  
    elif sim == 4 or sim == 3:
        response_object = {'result': 'Cúmplice'}  
    elif sim == 2:
        response_object = {'result': 'Supeito'}  
    else:
        response_object = {'result': 'Inocente'}  

    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
