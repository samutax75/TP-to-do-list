from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = {
    "nom": "samir",
    "tache": "aller au match de basket"
}


@app.route("/tasks", methods=['GET'])
def get_tasks():
    return jsonify({"tasks":tasks})


@app.route("/")
def home():
    return "Bienvunue sur notre site"


@app.route("/tasks/<nom>", methods=['DELETE'])
def del_task(nom):
    if nom in tasks:
        tasks.pop(nom)
        return jsonify({"message": f" La tâche de {nom} à été supprimer"}), 200
    else:
        return jsonify({"error": f" aucune tâche trouvée pour {nom}"}), 404


# @app.route("/tasks", methods=['POST'])
# def add_tasks():
#     data = request.get_json()
#     tasks.append(data["title"])
#     return jsonify({'message': 'Task added successfully',}), 201


@app.route("/tasks", methods=['POST'])
def add_tasks():
    data = request.get_json()
    nom = data.get("nom")
    tache = data.get("tache")
    if not nom or not tache:
        return jsonify({"error": "champs nom et tache requis"})
    tasks[nom] = tache
    return jsonify({nom: tache}), 201
 
if __name__ == '__main__':
        app.run(debug=True)
