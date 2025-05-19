from flask import Flask, request, jsonify
import sqlite3
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
DATABASE = 'database.db'
tasks = []


@app.route("/api/test")
def home():
    return "Bienvenue sur la page d'accueil"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_db():
    # Vérifie si le fichier SQLite existe déjà
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
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


 
@app.route("/tasks", methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.commit()
    conn.close()
    return jsonify([dict(row) for row in tasks])

@app.route('/tasks', methods=['POST'])     
def add_tasks():
    data = request.get_json()
    conn = get_db_connection()
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (data["title"],))
    conn.commit()
    conn.close()
    return jsonify({"message": "La tâche à bien été ajouter"}), 201
 
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Task deleted'})
 
 
 
if __name__ == "__main__":
    initialize_db()
    app.run()
     