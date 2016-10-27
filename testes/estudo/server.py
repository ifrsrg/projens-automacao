from werkzeug.utils import secure_filename
import os
import sys
from nota import Nota #negocio
from conexao import * #persistencia
from flask import *
import json
import psycopg2
app = Flask(__name__)
UPLOAD_FOLDER = './static/arquivos/'
# extensoes permitidas
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.secret_key = "\x91XC\x82\x97\x10X\x9e@\xfa\x9b\xf6WO\x18\xdd\nr\xce\xb6r\x96\xfdF"
conexao = Conexao("tabajara")
#conexaoOutroBanco = Conexao("youtube")
notaDAO = NotaDAO(conexao)
lixeiraDAO = LixeiraDAO(conexao)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# tamanho maximo dos arquivos (exemplo - no maximo 1 mb)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def upload_file():
    if request.method == 'POST':
        if 'imagem' not in request.files:
            return None
        file = request.files['imagem']
        if file.filename == '':
            return None

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)            
            print "Depois do Secute:"+filename
            
            # se quiser manter o nome original
            caminho = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(caminho)
            
            # se quiser colocar outro nome no arquivo
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], "igor."+ filename.rsplit('.', 1)[1]))
            print 'Upload realizado com sucesso'
            return caminho
    return caminho



@app.errorhandler(404)
def error404(error):
    return render_template("404.html")

@app.route("/")
def mostra():
    return render_template("formulario.html")

@app.route("/login", methods=["POST"])    
def login():
    session['login'] = request.form['login'] 
    session['senha'] = request.form['senha']
    return redirect(url_for("index"))

@app.route("/index")
def index():
    vetNota = []
    vetNota = notaDAO.listaTodos()
    return render_template("home.html", vetnota = vetNota)

@app.route("/edit",  methods=['POST'])
def mostraform():
    
    return render_template("altera.html", id = request.form["id"])


@app.route("/update", methods =['POST'])
def update():
    if request.method == 'POST':
        imagem = upload_file()
        nota = Nota(request.form["titulo"], request.form["descricao"], request.form["id"], request.form["cor"], imagem)
        notaDAO.alterar(nota)
        return redirect(url_for("index"))
        
@app.route("/move",  methods=['POST'])
def mover():
    id = request.form["id"]
    notaDAO.deletar(id)
    return redirect(url_for('index'))
     
@app.route("/criar")
def criar():
    return render_template("criar.html")

@app.route("/fim", methods=['POST'])
def finalizar():
    if request.method== 'POST':
        imagem = upload_file()
        nota= Nota(request.form["titulo"], request.form["descricao"], 0 , request.form["cor"], imagem)
        notaDAO.inserir(nota)     

        return redirect(url_for("index"))
@app.route("/lixeira")
def lixeira():
    vetNota = []
    vetNota =lixeiraDAO.listaTodos()
    
    return render_template("lixeira.html", vetnota = vetNota)
@app.route("/delete", methods=["POST"])
def deletar(): 
    lixeiraDAO.deletar(request.form["id"])
    
    return redirect(url_for("lixeira"))
    
@app.route("/restaura", methods=["POST"])
def restaurar():
    print "ID BONITINHO: " + str(request.form['id'])
    lixeiraDAO.restaurar(request.form["id"])
    return redirect(url_for("lixeira"))
    
    
@app.route("/duplica", methods=["POST"])
def duplica():
    notaDAO.replica(request.form["id"])
    return redirect(url_for("index"))

@app.route("/testeajax/<titulo>", methods=["GET"])
def pesquisa(titulo):
    print "sdfsdfsd"+str(titulo)
    #notas = notaDAO.ajax(request.args.get("titulo"))
    notas = notaDAO.ajax(titulo)
    if(len(notas)>0):
    	return titulo
	return ""

if __name__ == "__main__":
	app.debug = True
	app.run()