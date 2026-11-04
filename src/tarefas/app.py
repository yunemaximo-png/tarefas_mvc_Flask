from flask import Flask, render_template

from src.tarefas.models.database import init_db

app = Flask(__name__)

with app.app_context():
    init_db()

@app.route('/test')
def test():
    return 'Servidor Online!'

@app.route('/')
def home():
    return render_template('base.html', titulo='Lista de Tarefas')

if __name__ == '__main__':
    app.run()

