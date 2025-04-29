from flask import Flask, request, jsonify
import sqlite3
import os
app = Flask(__name__)

tasks=[]

@app.route("/tasks", methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    conn.row_factory = sqlite3.row
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.commit()
    conn.close()
    return jsonify([dict(row) for row in tasks])


@app.route("/")
def home():
    return "Bienvunue sur notre site"


@app.route("/tasks/<int:task_id>" , methods=['DELETE'])
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?',(task_id,))
    conn.commit()
    conn.close()
    return jsonify({'massage': 'Task deleted'})


# @app.route("/tasks", methods=['POST'])
# def add_tasks():
#     data = request.get_json()
#     tasks.append(data["title"])
#     return jsonify({'message': 'Task added successfully',}), 201


@app.route("/tasks", methods=['POST'])
def add_tasks():
    data = request.get_json()
    title = data.get('title')
    #done = data.get('done',False)
    conn = get_db_connection()
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (data["title"]))
    conn.commit()
    conn.close()
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
