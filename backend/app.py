from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = {
    "Samir":"Apprendre Flask",
    "Mehdi":"Partir au USA en Août 2025",
    "Lily":"Ranger sa chambre"
    }

# tasks=["Apprendre Flask","Partir au USA en Août 2025",]


@app.route("/tasks", methods=['GET'])
def get_tasks():
    return jsonify({"tasks":tasks})


@app.route("/tasks/<task>", methods=['DELETE'])
def del_task(task):
    tasks.remove(task)
    return f" La tâche  {task} à été supprimer"



@app.route("/tasks", methods=['POST'])
def add_tasks():
    data = request.get_json()
    tasks.append(data["title"])
    return jsonify({'message': 'Task added successfully',}), 201


 
if __name__ == '__main__':
        app.run(debug=True)
