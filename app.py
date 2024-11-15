from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite solicitudes desde cualquier origen para pruebas

# Simulación de base de datos
USERS = {"admin": "password123", "user": "pass456"}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in USERS and USERS[username] == password:
        return jsonify({"message": "Login exitoso", "status": "success"}), 200
    return jsonify({"message": "Credenciales incorrectas", "status": "fail"}), 401

if __name__ == "__main__":
    app.run(debug=True)
