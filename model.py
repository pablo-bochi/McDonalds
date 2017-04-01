class Funcionario(object):
    def __init__(self, nome, senha, foto):
        self.nome = nome
        self.senha = senha
        self.foto = foto


class Cliente(object):
    def __init__(self, id, nome, sexo, cpf, foto):
        self.id = id
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.foto = foto


class Bebida(object):
    def __init__(self, id, nome, preco, foto):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.foto = foto


class Lanche(object):
    def __init__(self, id, nome, ingredientes, preco, foto):
        self.id = id
        self.nome = nome
        self.ingredientes = ingredientes
        self.preco = preco
        self.foto = foto


class Pedido(object):
    def __init__(self, id, preco_total, descricao, situacao, pagamento, observacoes, idCliente, idFuncionario):
        self.id = id
        self.preco_total = preco_total
        self.descricao = descricao
        self.situacao = situacao
        self.pagamento= pagamento
        self.observacoes = observacoes
        self.idCliente = idCliente
        self.idFuncionario = idFuncionario


class Combo(object):
    def __init__(self, id, nome, tam_batata, foto, idLanche, idBebida):
        self.id = id
        self.nome = nome
        self.tam_batata = tam_batata
        self.foto = foto
        self.idLanche = idLanche
        self.idBebida = idBebida
