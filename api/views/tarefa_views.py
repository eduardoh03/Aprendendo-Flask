from flask_restful import Resource
from api import api
from ..schemas import tarefa_schemas
from flask import request, make_response, jsonify
from ..entidades import tarefa
from ..services import tarefa_service, projeto_service
from ..pagination import paginate
from ..models.tarefa_model import Tarefa

# A view está responsável por tratar os dados das requisições

class TarefaList(Resource):  # List é adicionado em metodos que não necessitao de parametros GET e POST

    def get(self):
        # tarefas = tarefa_service.listar_tarefas()
        # many é necessario porque várias tarefas vão ser passadas pelo Schema
        ts = tarefa_schemas.TarefaSchema(many=True)
        return paginate(Tarefa, ts)

    def post(self):
        ts = tarefa_schemas.TarefaSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            data_expiracao = request.json["data_expiracao"]
            projeto = request.json["projeto"]
            projeto_tarefa = projeto_service.listar_projeto_id(projeto)
            if projeto_tarefa is None:
                return make_response(jsonify("Projeto nao encontrado."), 404)
            tarefa_nova = tarefa.Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao,projeto=projeto_tarefa)
            result = tarefa_service.cadastrar_tarefa(tarefa_nova)
            return make_response(ts.jsonify(result), 201)


class TarefaDetail(Resource):  # Detail é adicionado em metodos que necessitao de parametros PUT e DELETE

    def get(self, id):
        tarefa = tarefa_service.listar_tarefa_id(id)
        if tarefa is None:
            return make_response(jsonify("Tarefa nao encontrada."), 404)
        else:
            ts = tarefa_schemas.TarefaSchema()
            return make_response(ts.jsonify(tarefa), 200)

    def put(self, id):
        tarefa_db = tarefa_service.listar_tarefa_id(id)
        if tarefa_db is None:
            return make_response(jsonify("Tarefa nao encontrada."), 404)

        ts = tarefa_schemas.TarefaSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            data_expiracao = request.json["data_expiracao"]
            projeto = request.json["projeto"]
            projeto_tarefa = projeto_service.listar_projeto_id(projeto)
            if projeto_tarefa is None:
                return make_response(jsonify("Projeto nao encontrado."), 404)
            tarefa_nova = tarefa.Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, projeto=projeto_tarefa)
            result = tarefa_service.editar_tarefa(tarefa_db, tarefa_nova)
            tarefa_atualizada = tarefa_service.listar_tarefa_id(id)
            return make_response(ts.jsonify(tarefa_atualizada), 200)

    def delete(self, id):
        tarefa = tarefa_service.listar_tarefa_id(id)
        if tarefa is None:
            return make_response(jsonify("Tarefa nao encontrada."), 404)
        tarefa_service.remover_tarefa(tarefa)
        return make_response(jsonify(""), 204)


# CRIADO A ROTA
api.add_resource(TarefaList, '/tarefas')
api.add_resource(TarefaDetail, '/tarefa/<int:id>')