from livro import Livro
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = input("Ano de publicação: ")
        copias = int(input("Número de cópias: "))
        self.livros.append(Livro(titulo, autor, ano, copias))
        print("Livro cadastrado com sucesso!")

    def cadastrar_usuario(self):
        nome = input("Nome: ")
        identificacao = input("Número de identificação: ")
        contato = input("Contato: ")
        self.usuarios.append(Usuario(nome, identificacao, contato))
        print("Usuário cadastrado com sucesso!")

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def buscar_usuario(self, identificacao):
        for usuario in self.usuarios:
            if usuario.identificacao == identificacao:
                return usuario
        return None

    def emprestar_livro(self):
        titulo = input("Título do livro: ")
        identificacao = input("Identificação do usuário: ")

        livro = self.buscar_livro(titulo)
        usuario = self.buscar_usuario(identificacao)

        if livro is None:
            print("Livro não encontrado.")
        elif usuario is None:
            print("Usuário não encontrado.")
        elif livro.copias <= 0:
            print("Livro indisponível para empréstimo.")
        else:
            livro.copias -= 1
            livro.emprestados += 1
            usuario.livros_emprestados.append(livro.titulo)
            print("Empréstimo realizado com sucesso!")

    def devolver_livro(self):
        titulo = input("Título do livro: ")
        identificacao = input("Identificação do usuário: ")

        livro = self.buscar_livro(titulo)
        usuario = self.buscar_usuario(identificacao)

        if livro is None:
            print("Livro não encontrado.")
        elif usuario is None:
            print("Usuário não encontrado.")
        elif titulo not in usuario.livros_emprestados:
            print("Este usuário não possui esse livro emprestado.")
        else:
            livro.copias += 1
            livro.emprestados -= 1
            usuario.livros_emprestados.remove(titulo)
            print("Devolução realizada com sucesso!")

    def consultar_livros(self):
        termo = input("Digite título, autor ou ano: ").lower()
        encontrados = []

        for livro in self.livros:
            if termo in livro.titulo.lower() or termo in livro.autor.lower() or termo == livro.ano:
                encontrados.append(livro)

        if not encontrados:
            print("Nenhum livro encontrado.")
        else:
            for livro in encontrados:
                print(f"Título: {livro.titulo} | Autor: {livro.autor} | Ano: {livro.ano} | Disponíveis: {livro.copias}")

    def relatorios(self):
        print("\n--- LIVROS DISPONÍVEIS ---")
        for livro in self.livros:
            if livro.copias > 0:
                print(f"{livro.titulo} - {livro.copias} cópias disponíveis")

        print("\n--- LIVROS EMPRESTADOS ---")
        for livro in self.livros:
            if livro.emprestados > 0:
                print(f"{livro.titulo} - {livro.emprestados} emprestado(s)")

        print("\n--- USUÁRIOS CADASTRADOS ---")
        for usuario in self.usuarios:
            print(f"{usuario.nome} | ID: {usuario.identificacao} | Contato: {usuario.contato}")
