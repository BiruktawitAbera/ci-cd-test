from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the API to handle calculation
@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is not None and num2 is not None:
        result = num1 + num2  # Example calculation (can be any logic)
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
