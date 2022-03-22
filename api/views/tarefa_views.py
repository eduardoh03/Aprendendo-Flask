from flask_restful import Resource
from api import api
from ..schemas import tarefa_schemas
from flask import request, make_response, jsonify
from ..entidades import tarefa
from ..services import tarefa_service
#A view está responsável por tratar os dados das requisições

class TarefaList(Resource):# List é adicionado em metodos que não necessitao de parametros GET e POST

    def get(self):
        tarefas = tarefa_service.listar_tarefas()
        #many é necessario porque várias tarefas vão ser passadas pelo Schema
        ts = tarefa_schemas.TarefaSchema(many=True)
        return make_response(ts.jsonify(tarefas), 200)

    def post(self):
        ts = tarefa_schemas.TarefaSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            data_expiracao = request.json["data_expiracao"]
            tarefa_nova = tarefa.Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao)
            result = tarefa_service.cadastrar_tarefa(tarefa_nova)
            return make_response(ts.jsonify(result), 201)
api.add_resource(TarefaList, '/tarefas')

# class TarefaDetail(Resource):# Detail é adicionado em metodos que necessitao de parametros PUT e DELETE