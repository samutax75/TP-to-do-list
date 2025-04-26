from flask import Flask, request, jsonify
import sqlite3
import os
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


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def initialize_db():
    # Vérifie si le fichier SQLite existe déjà
    if not os.path.exists('database.db'):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        print("Base de données créée")
    else:
        print("Base de données déjà existante")


if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)
