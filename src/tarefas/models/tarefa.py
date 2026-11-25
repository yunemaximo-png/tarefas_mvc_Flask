from datetime import datetime
 
from tarefas.models.database import Database
 
 
class Tarefa:
    """Provê métodos para armazenar, recuperar e processar os dados
    das tarefas criadas a partir do formulário principal.
    """
    def __init__(self, titulo, id = None, data_conclusao = None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao
 
 
    def salvarTarefa(self):
        """Salvar a tarefa no banco de dados."""
 
        sql = 'INSERT INTO tarefa (titulo_tarefa, data_conclusao) VALUES (%s, %s);'
        params = (self.titulo, self.data_conclusao) # Protege contra SQL Injection
 

        with Database() as db:
            db.executar(sql, params)

    @staticmethod
    def listarTarefas():
        """Retorna uma lista com todas as tarefas cadastradas."""


        sql = '''
        SELECT id_tarefa, titulo_tarefa, data_conclusao FROM tarefa 
        LIMIT 100;'''
        with Database() as db:
            tarefas_banco = db.executar(sql)

        return tarefas_banco if tarefas_banco else []

    @staticmethod
    def apagarTarefa(id):
        sql = 'DELETE FROM tarefa WHERE id_tarefa = %s;'
        params = (id,)
        with Database() as db:
            db.executar(sql, params)

    @staticmethod
    def atualizarTarefa(id, titulo, data):
        sql = 'UPDATE tarefa SET titulo_tarefa = %s, data_conclusao = %s WHERE id_tarefa = %s;'
        params = (titulo, data, id)
        with Database() as db:
            db.executar(sql, params)
   
