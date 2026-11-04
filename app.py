from flask import Flask, request, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB = Path("cupcakes_vagner.db")

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS pedidos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            telefone TEXT NOT NULL,
            endereco TEXT NOT NULL,
            pagamento TEXT NOT NULL,
            entrega TEXT NOT NULL,
            total REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pedido recebido'
        )""")

@app.route("/api/pedidos", methods=["POST"])
def criar_pedido():
    init_db()
    dados = request.get_json(force=True)
    obrigatorios = ["cliente","telefone","endereco","pagamento","entrega","total"]
    faltando = [x for x in obrigatorios if not dados.get(x)]
    if faltando:
        return jsonify({"erro":"Campos obrigatórios ausentes","campos":faltando}),400

    with sqlite3.connect(DB) as conn:
        cur = conn.execute(
            "INSERT INTO pedidos(cliente,telefone,endereco,pagamento,entrega,total) VALUES(?,?,?,?,?,?)",
            (dados["cliente"],dados["telefone"],dados["endereco"],dados["pagamento"],dados["entrega"],float(dados["total"]))
        )
        pedido_id = cur.lastrowid
    return jsonify({"pedido_id":pedido_id,"status":"Pedido recebido"}),201

@app.route("/api/pedidos/<int:pedido_id>", methods=["GET"])
def consultar_pedido(pedido_id):
    init_db()
    with sqlite3.connect(DB) as conn:
        conn.row_factory = sqlite3.Row
        pedido = conn.execute("SELECT * FROM pedidos WHERE id=?", (pedido_id,)).fetchone()
    if not pedido:
        return jsonify({"erro":"Pedido não encontrado"}),404
    return jsonify(dict(pedido))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
