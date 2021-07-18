from flask import Flask, jsonify, request
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/taxes', methods=['POST'])
def taxes():
    post_data = request.get_json()
    global SALARY
    global WORKING_HOURS
    SALARY = post_data.get("salary")
    WORKING_HOURS = post_data.get("workingHours")

    GROSS_SALARY = SALARY * WORKING_HOURS

    INSS = GROSS_SALARY * 0.08
    imposto_de_renda = GROSS_SALARY * 0.11
    sindicato = GROSS_SALARY * 0.05
    total_taxes = INSS + imposto_de_renda + sindicato

    salario_liquido = GROSS_SALARY - total_taxes
            
    response_object = {
        'gross': GROSS_SALARY,
        'inss': INSS,
        'renda': imposto_de_renda,
        'sindicato': sindicato,
        'liquid': salario_liquido
    }
    return jsonify(response_object)

SALARY = 0
WORKING_HOURS = 0

if __name__ == '__main__':
    app.run()