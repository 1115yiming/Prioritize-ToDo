from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')

def calculate_priority_scores(tasks, a, b):
    priority_scores = {task: (urgency * a + importance * b) for task, (urgency, importance) in tasks.items()}
    return sorted(priority_scores.items(), key=lambda x: x[1], reverse=True)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    tasks = data.get('tasks')
    a = data.get('a', 0.5)
    b = data.get('b', 0.5)

    if not tasks or a + b != 1:
        return jsonify({"error": "Invalid input"}), 400

    priority_scores_sorted = calculate_priority_scores(tasks, a, b)
    return jsonify(priority_scores_sorted)

if __name__ == '__main__':
    app.run(debug=True)
