from biblioteca import Biblioteca
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n===== SISTEMA DE BIBLIOTECA =====")
        print("1 - Cadastrar livro")
        print("2 - Cadastrar usuário")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("5 - Consultar livros")
        print("6 - Relatórios")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                biblioteca.cadastrar_livro()
            elif opcao == "2":
                biblioteca.cadastrar_usuario()
            elif opcao == "3":
                biblioteca.emprestar_livro()
            elif opcao == "4":
                biblioteca.devolver_livro()
            elif opcao == "5":
                biblioteca.consultar_livros()
            elif opcao == "6":
                biblioteca.relatorios()
            elif opcao == "0":
                print("Sistema encerrado.")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Erro: digite um valor válido.")


menu()