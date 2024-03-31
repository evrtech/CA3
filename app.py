from flask import Flask, jsonify
from calculator import Calculator  # Assuming your Calculator class is in a separate file named calculator.py

app = Flask(__name__)
calculator = Calculator()

@app.route('/calc/add/<int:x>/<int:y>')
def add(x, y):
    result = calculator.add(x, y)
    return jsonify({'operation': 'add', 'result': result})

@app.route('/calc/multi/<int:x>/<int:y>')
def multi(x, y):
    result = calculator.multi(x, y)
    return jsonify({'operation': 'multi', 'result': result})

@app.route('/calc/divide/<int:x>/<int:y>')
def divide(x, y):
    try:
        result = calculator.divide(x, y)
        return jsonify({'operation': 'divide', 'result': result})
    except ValueError as e:
        return jsonify({'error': str(e)})

@app.route('/calc/subtract/<int:x>/<int:y>')
def subtract(x, y):
    result = calculator.subtract(x, y)
    return jsonify({'operation': 'subtract', 'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)