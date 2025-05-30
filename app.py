from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Conexión a MongoDB (revisa que la URI tenga tu DB correcta)
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://admin:acer@cluster0.wdbuqoa.mongodb.net/personal_medico?retryWrites=true&w=majority")
client = MongoClient(MONGO_URI)
db = client.get_default_database()   


# Ruta principal (carga plantilla HTML)
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/health', methods=['GET'])
def health_check():
    # Aquí puedes agregar lógica para verificar la salud de tu app
    # Por ejemplo, verificar si puedes conectar a una base de datos
    try:
        # Ejemplo: Simula una verificación (puedes agregar más lógica)
        # Si todo está bien, devuelve un 200
        return "OK", 200
    except Exception as e:
        # Si hay un error, devuelve un código de error (por ejemplo, 500)
        return f"Error: {str(e)}", 500

# Ruta para insertar datos
@app.route("/insertar", methods=["POST"])
def insertar():
    data = request.json

    # Aquí puedes validar o transformar data si quieres
    # Por ejemplo, convertir fecha_ingreso a datetime.date si necesitas

    result = db.usuarios.insert_one(data)
    return jsonify({"inserted_id": str(result.inserted_id)})


# Ruta para listar datos
@app.route("/listar", methods=["GET"])
def listar():
    documentos = list(db.usuarios.find({}, {"_id": 0}))
    return jsonify(documentos)

if __name__ == "__main__":
    app.run(debug=True)
