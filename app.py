from datetime import datetime
import json
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for

app = Flask(__name__)

projetos = [
    {
        "id": 1,
        "nome": "Aula 01 - Anotações e Avaliação",
        "data": "09/10/2024",
        "descricao": "Introdução ao curso, critérios de avaliação e requisitos para o projeto final. Configuração do ambiente Python e boas práticas.",
        "link": "#",
        "showButton": False
        
    },
    {
        "id": 2,
        "nome": "Aula 02 - Grupos e Temas",
        "data": "16/10/2024",
        "descricao": "Divisão dos grupos e sorteio dos temas dos trabalhos: chamada por câmera, análise de emoções e scanner para PDFs.",
        "link": "#",
        "showButton": False
    },
    {
        "id": 3,
        "nome": "Aula 03 - Ambiente Virtual",
        "data": "23/10/2024",
        "descricao": "Criação do ambiente virtual em Python, instalação de dependências (Flask, SQLAlchemy, NumPy) e estruturação do projeto.",
        'link': '#',
        "showButton": False
    },
    {
        "id": 4,
        "nome": "Aula 04 - Desenvolvimento com Flask",
        "data": "30/10/2024",
        "descricao": "Criação de rotas no Flask, manipulação de requisições HTTP e desenvolvimento inicial da aplicação web.",
        'link': '/l1index',
        "showButton": True
    },
    {
        "id": 5,
        "nome": "Aula 05 - Passagem de Parâmetros",
        "data": "06/11/2024",
        "descricao": "Uso do render_template para passar parâmetros ao HTML e segunda lista de atividades com autenticação e templates dinâmicos.",
        'link': '/l2index',
        "showButton": True
    },
    {
        "id": 6,
        "nome": "Aula 06 - Regras de Desenvolvimento",
        "data": "13/11/2024",
        "descricao": "Boas práticas para requisições web, validação de dados, tratamento de exceções e uso do SQLite.",
        'link': '/l3form',
        "showButton": True
    },
    {
        "id": 7,
        "nome": "Aula 07 - Desenvolvimento de Atividades",
        "data": "20/11/2024",
        "descricao": "Tempo dedicado para desenvolver atividades e aprimorar os projetos em sala.",
        'link': '#',
        "showButton": False
    },
    {
        "id": 8,
        "nome": "Aula 08 - Protótipos do Projeto Final",
        "data": "27/11/2024",
        "descricao": "Apresentação dos primeiros protótipos e objetivos dos projetos finais.",
        'link': '#',
        "showButton": False
    },
    {
        "id": 9,
        "nome": "Aula 09 - Desenvolvimento do Projeto",
        "data": "04/12/2024",
        "descricao": "Continuação do desenvolvimento dos projetos finais em sala.",
        'link': '#',
        "showButton": False
    },
    {
        "id": 10,
        "nome": "Aula 10 - Definição da Prova e Orquestra",
        "data": "11/12/2024",
        "descricao": "Discussão sobre o formato da prova e apreciação de apresentação musical no campus.",
        'link': '#',
        "showButton": False
    },
    {
        "id": 11,
        "nome": "Aula 11 - Atividades Pré-Prova",
        "data": "18/12/2023",
        "descricao": "Atividades práticas: mini-blog, autenticação básica e upload de fotos para revisar conceitos antes da prova.",
        'link': '/l4blog',
        "showButton": True
    },
    {
        "id": 12,
        "nome": "Aula 12 a 14 - Prova Prática",
        "data": "08/01/2025-22/01/2025",
        "descricao": "Aplicação da prova prática dividida em grupos, abordando os conceitos aprendidos ao longo do curso.",
        'link': '#',
        "showButton": False
    },
    {
        "id": 13,
        "nome": "Aula 15 - Feedback da Prova",
        "data": "29/01/2025",
        "descricao": "Correção e divulgação das notas da prova final pelo professor Alex.",
        'link': '#',
        "showButton": False
    },
]


@app.route("/")
def index():
    return render_template("index.html", projetos=projetos)


@app.route("/l1table")
def table():
    return render_template("l1tableInfo.html")


@app.route("/l1index")
def start():
    return render_template("l1index.html")


@app.route("/l1contact")
def contato():
    return render_template("l1contact.html")


@app.route("/l1moveimg")
def moveimg():
    return render_template("l1moveimg.html")


@app.route("/l1webcam")
def webcam():
    return render_template("l1webcam.html")


developers = {
    "nicholas": {
        "name": "Nicholas Ricardo Silva Araujo",
        "photo": "nicholas.jpeg",
        "title": "Fullstack Developer",
        "github": "https://github.com/nicholasss0",
        "stacks": [
            "Python",
            "React",
            "Django",
            "Flask",
            "Vite",
            "Next.js",
            "Data Analysis",
        ],
    },
    "patrick": {
        "name": "Patrick Cauã Gonçalves Dias",
        "photo": "patrick.jpeg",
        "title": "Backend Developer",
        "github": "https://github.com/Patrick510",
        "stacks": ["Python", "React", "Java", "SpringBoot"],
    },
    "pedro": {
        "name": "Pedro Samuel Soares Simão",
        "photo": "pedro.jpeg",
        "title": "Fullstack Developer",
        "github": "https://github.com/PsSave",
        "stacks": ["Typescript", "Node", "Python"],
    },
    "kauan": {
        "name": "Kauan Olival Lopes",
        "photo": "kauan.png",
        "title": "Fullstack Developer",
        "github": "https://github.com/kauan345developer",
        "stacks": ["Python", "React", "Node", "Javascript"],
    },
    "felipe": {
        "name": "Felipe Flamarini",
        "photo": "felipe.jpeg",
        "title": "Backend Developer",
        "github": "https://github.com/FelipeFlamarini",
        "stacks": ["Node", "Javascript", "Docker", "Linux", "Python"],
    },
    "nathan": {
        "name": "Nathan Brito",
        "photo": "nathan.png",
        "title": "Fullstack Developer",
        "github": "https://github.com/nathanbrito",
        "stacks": ["Node", "Javascript", "Python"],
    },
}



@app.route("/l1resume/<dev_name>")
def l1resume(dev_name):
    

    if dev_name.lower() in developers:
        return render_template("l1resume.html", dev=developers[dev_name.lower()])
    return "Developer not found", 404


@app.route("/l1allresumes")
def curriculos():
    return render_template("l1allResume.html", developers=developers)


@app.route("/l2index")
def l2start():
    return render_template("l2index.html")

app.secret_key = "supersecretkey"

MOCK_USER = {"username": "admin", "password": "1234"}


USUARIO = "admin"
SENHA = "1234"

tentativas = 0

@app.route('/l2login', methods=['GET', 'POST'])
def l2login():
    global tentativas


    
    if tentativas >= 2:
        return render_template('l2login.html', bloqueado=True)

    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        
        if usuario == USUARIO and senha == SENHA:
            
            hora_atual = datetime.now().hour
            if 6 <= hora_atual < 12:
                saudacao = "Bom dia!"
            elif 12 <= hora_atual < 18:
                saudacao = "Boa tarde!"
            else:
                saudacao = "Boa noite!"

            return render_template('l2login.html', saudacao=saudacao,bloqueado=False)
        else:
            tentativas += 1
            flash("Login inválido. Tente novamente.")
            return redirect(url_for('l2login'))

    return render_template('l2login.html')


FIELDS_JSON = '[{"name": "name", "type": "text", "placeholder": "Nome"}, {"name": "surname", "type": "text", "placeholder": "Sobrenome"}, {"name": "email", "type": "email", "placeholder": "Email"}, {"name": "password", "type": "password", "placeholder": "Senha"}]'


def generate_form_fields(fields_json):
    fields = json.loads(fields_json)
    return "\n".join(
        f'<input type="{field["type"]}" name="{field["name"]}" placeholder="{field["placeholder"]}" required class="w-full p-2 border border-gray-300 rounded">'
        for field in fields
    )


@app.route("/l2form", methods=["GET", "POST"])
def home():
    form_fields = generate_form_fields(FIELDS_JSON)
    if request.method == "POST":
        data = request.form.to_dict()
        return render_template("l2form.html", form_fields=form_fields, data=data)
    return render_template("l2form.html", form_fields=form_fields)


class Usuario:
    def __init__(self, nome, email, senha, idade, endereco):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.idade = idade
        self.endereco = endereco

    def validar_senha(self, senha):
        return self.senha == senha


usuarios_db = [
    Usuario("João Silva", "admin@x.com", "1234", 25, "Rua A, 123"),
    Usuario("Maria Oliveira", "maria@example.com", "senha456", 30, "Rua B, 456")
]

def autenticar_usuario(email, senha):
    for usuario in usuarios_db:
        if usuario.email == email and usuario.validar_senha(senha):
            return usuario
    return None


@app.route('/l2clogin', methods=['GET', 'POST'])
def l2clogin():
    if 'usuario_logado' in session:
        return redirect(url_for('l2cbem_vindo'))

    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = autenticar_usuario(email, senha)

        if usuario:
            session['usuario_logado'] = usuario.email  
            return redirect(url_for('l2cbem_vindo'))
        else:
            flash("Credenciais inválidas. Tente novamente.")
            return redirect(url_for('l2clogin'))

    return render_template('l2clogin.html')

@app.route('/l2cbem-vindo')
def l2cbem_vindo():
    if 'usuario_logado' not in session:
        return redirect(url_for('l2clogin'))
    
    usuario_logado = next((u for u in usuarios_db if u.email == session['usuario_logado']), None)
    return render_template('l2cbem_vindo.html', usuario=usuario_logado)

@app.route('/l2clogout')
def l2clogout():
    session.pop('usuario_logado', None)  
    return redirect(url_for('l2clogin'))


@app.route("/l3form")
def l3form():
    return render_template("l3form.html")


USER_DATA = {"nome": "admin", "senha": "1234"}


@app.route("/l3auth", methods=["POST"])
def l3authenticate():
    if "attempts" not in session:
        session["attempts"] = 0

    if session["attempts"] >= 2:
        return (
            jsonify(
                {
                    "error": "Número máximo de tentativas excedido. Tente novamente mais tarde."
                }
            ),
            403,
        )

    data = request.get_json()
    nome = data.get("nome")
    senha = data.get("senha")

    if not nome or not senha:
        return jsonify({"error": "Nome e senha são obrigatórios."}), 400

    if nome == USER_DATA["nome"] and senha == USER_DATA["senha"]:
        session.pop("attempts", None)  
        return jsonify({"message": "Autenticação bem-sucedida!"}), 200

    session["attempts"] += 1
    return jsonify({"error": "Credenciais inválidas. Tente novamente."}), 401


posts = []


@app.route("/l4blog", methods=["GET", "POST"])
def l4blog():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        conteudo = request.form.get("conteudo")

        if not titulo or not conteudo:
            return "Preencha todos os campos!", 400

        novo_post = {
            "titulo": titulo,
            "conteudo": conteudo,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        }
        posts.insert(0, novo_post)  

        return redirect(url_for("l4blog"))

    return render_template("l4blog.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
