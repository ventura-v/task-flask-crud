from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/about')
def about():
    return 'Página sobre'

# quando o arquivo é executado manualmente, o parâmetro __name__ = "__main__"
# garante que quando apenas o arquivo for executado manualmente, o app irá rodar em modo debug (recomendável apenas para desenvolvimento)
if __name__ == "__main__":
    app.run(debug=True)