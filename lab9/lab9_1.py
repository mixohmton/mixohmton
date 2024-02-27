from flask import Flask
app = Flask(__name__)
@app.route('/<opt>/<int:a>/<int:b>')
def calculate(opt, a, b):
    if opt == '+':
        result = a + b
    elif opt == '-':
        result = a - b
    elif opt == '*':
        result = a * b
    elif opt == '|':
        if b != 0:
            result = a / b
        else:
            return "Error: Division by zero!"
    return f"ผลลัพธ์ของ {a} {opt} {b} คือ {result}"
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
