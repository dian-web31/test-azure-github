from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/echo', methods=['POST'])
def echo():
    # Obtener el mensaje enviado por el cliente
    data = request.json
    user_message = data.get("message", "")
    # Responder con el mismo mensaje
    return jsonify({"response": f"Eco: {user_message}"})

if __name__ == '__main__':
    app.run(debug=True)