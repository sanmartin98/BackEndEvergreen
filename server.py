from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.ProyectoAnalitica import ProyectoAnalitica

app = Flask(__name__)
CORS(app)

@app.route("/proyectosAnalitica", methods=['GET'])
def getAll():
    return (ProyectoAnalitica.list())

@app.route("/proyectosAnalitica", methods=['POST'])
def postOne():
    body = request.json
    return (ProyectoAnalitica.create(body))

@app.route("/proyectosAnalitica", methods=['DELETE'])
def deleteOne():
    body = request.json
    return (ProyectoAnalitica.delete(body))

@app.route("/proyectosAnalitica", methods=['PUT'])
def updateOne():
    body = request.json
    return (ProyectoAnalitica.update(body))