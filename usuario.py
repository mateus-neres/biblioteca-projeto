class Usuario:
    def __init__(self, nome, identificacao, contato):
        self.nome = nome
        self.identificacao = identificacao
        self.contato = contato
        self.livros_emprestados = []