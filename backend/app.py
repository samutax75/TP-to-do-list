from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = [
    {
        "id": 0,
        "task": "Aller au match de basket",
    },
    {
        "id": 1,
        "task": "Ranger la maison"
    }
]


@app.route("/tasks", methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})


@app.route("/")
def home():
    return "Bienvunue sur notre site"


@app.route("/tasks/<id_to_remove>", methods=['DELETE'])
def del_task(id_to_remove):
    global tasks
    new_tasks = []
    for task in tasks:
        if task["id"] != int(id_to_remove):
            new_tasks.append(task)

    tasks = new_tasks

    return jsonify({"message": f" La tâche '{task["task"]}' à été supprimer"}), 200



# @app.route("/tasks", methods=['POST'])
# def add_tasks():
#     data = request.get_json()
#     tasks.append(data["title"])
#     return jsonify({'message': 'Task added successfully',}), 201


@app.route("/tasks", methods=['POST'])
def add_tasks():
    task = request.get_json()
    tasks.append(task)
    return jsonify({"message": "La tâche à bien été ajouter"}), 201


if __name__ == '__main__':
    app.run(debug=True)
