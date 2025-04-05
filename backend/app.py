from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
tasks = ["acheter du pain"]


@app.route("/tasks", methods=['GET'])
def get_tasks():
    return tasks

@app.route("/",methods=['GET'])
def home():
    return"Bienvenue sur la page d'accueil"


@app.route("/tasks/<task>", methods=['PUT'])
def del_task(task):
    return f" je vais supprimer, {task}"



@app.route("/tasks", methods=['POST'])
def add_tasks():
    data = request.get_json()
    tasks.append(data['title'])
    return jsonify({'message': 'Task added successfully'}), 201


 
if __name__ == '__main__':
        app.run(debug=True)
