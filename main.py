from flask import Flask,jsonify,request
import os
 
app = Flask(__name__)
livros=[{"id":1,"nome":"antonio"},{"id":2,"nome":"antonio2"}]
        
@app.route('/livros/')
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:document>',methods=['GET'])
def consulta_livros_id(document):
    for livro in livros:
        if livro.get('document')==document:
            return jsonify(livro)

@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livros_id(id):    
    livro_novo=request.get_json()
    for indece, livro in enumerate(livros):
        if livro.get('id')==id:
            livros[indece].update(livro_novo)
            return jsonify(livros[indece]) 
        
@app.route('/livros/<int:id>',methods=['DELETE'])
def delete_livros_id(id):    
    livro_novo=request.get_json()
    for indece, livro in enumerate(livros):
        if livro.get('id')==id:
            del livros[indece]
            return jsonify(livros) 

@app.route('/livros',methods=['POST'])
def criar_livros_id():    
    livro_novo=request.get_json()
    livros.append(livro_novo) 
    return jsonify(livros) 
            

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
