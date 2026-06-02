from ninja import Schema


class IngredienteSchema(Schema):
    nome: str


class UtilizadorSchema(Schema):
    nome: str
    email: str


class ReceitaSchema(Schema):
    titulo: str
    descricao: str
    tempo_preparacao: int
    utilizador_id: int
    ingredientes_ids: list[int]

    @staticmethod
    def resolve_ingredientes_ids(receita):
        return list(receita.ingredientes.values_list("id", flat=True))
