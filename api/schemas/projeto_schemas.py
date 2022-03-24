from api import ma
from ..models import projeto_model
from marshmallow import fields

#funciona como o Forms do Django
class ProjetoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = projeto_model.Projeto
        fields = ("id", "nome", "descricao", "tarefas")
        # load_instance = True

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    tarefas = fields.List(fields.String)