from flask import Flask, request, jsonify
import sqlite3
import datetime

app = Flask(__name__)
tasks = ["acheter du pain","aller au basket"]


@app.route("/tasks", methods=['GET'])
def get_tasks():
    return tasks


@app.route("/",methods=['GET'])
def home():
    return"Bienvenue sur la page d'accueil"

@app.route("/heure")
def heure():
    date_heure=datetime.datetime.now()
    h=date_heure.hour
    m=date_heure.minute
    s=date_heure.second
    heure_formattee=f"{h:02d}:{m:02d}:{s:02d}"
    return f"L'heure acteuelle est :{heure_formattee}"

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
