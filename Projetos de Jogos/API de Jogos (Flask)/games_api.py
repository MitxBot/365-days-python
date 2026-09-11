from flask import Flask,request,jsonify

app = Flask(__name__)

jogos = []

@app.route("/jogos",methods=["GET"])
def listar_jogos():
    return jsonify(jogos)

@app.route("/jogos",methods=["POST"])
def adicionar_jogo():
    data = request.json
    jogos.append(data)
    return jsonify({"msg": "Jogo adicionado!"})

@app.route("/jogos/<init:id>",methods=["DELETE"])
def deletar_jogo(id):
    if id < len(jogos):
        jogos.pop(id)
        return jsonify({"msg": "Removido"})
    return jsonify({"erro" : "ID inválido!"})

app.run(debug=True)