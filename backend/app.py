from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = ["Ranger ma chambre", "Preparer à manger", "acheter le pain"]


@app.route("/")
def get_tasks():
    return tasks


@app.route("/tasks", methods=['POST'])
def add_tasks():
    data = request.get_json()
    tasks.append(data['title'])
    return jsonify({'message': 'Task added successfully'}), 201


if __name__ == '__main__':
    app.run(debug=True)
