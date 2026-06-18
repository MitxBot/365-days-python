class Livro:

    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} - {self.autor} ({status})"
    
class Biblioteca:
    
    def __init__(self):
        self.livros = []

    def adicionar_livro(self):
        titulo = input("Título: ")
        autor = input("Autor: ")

        livro = Livro(titulo,autor)
        self.livros.append(livro)

        print("\nLivro cadastrado com sucesso!\n")
        return
    
    def listar_livros(self):
        if not self.livros:
            print("\nNenhum livro cadastrado.\n")
            return
        
        print("\n=== Livros ===")

        for i, livro in enumerate(self.livros, start=1):
            print(f"{i}. {livro}")

        print()

    def emprestar_livro(self):
        self.listar_livros()

        if not self.livros:
            return
        
        try:
            indice = int(input("Número do livro: ")) - 1

            livro = self.livros[indice]

            if livro.disponivel:
                livro.disponivel = False
                print("\nLivro emprestado com sucesso!\n")
            else:
                print("\nLivro já está emprestado.\n")

        except:
            print("\nOpção inválida.\n")

    def devolver_livro(self):
        self.listar_livros()

        if not self.livros:
            return
        
        try:
            indice = int(input("Número do livro: ")) - 1

            livro = self.livros[indice]

            if livro.disponivel:
                livro.disponivel = True
                print("\nLivro devolvido com sucesso!\n")
            else:
                print("\nLivro já está disponível.\n")

        except:
            print("\nOpção inválida.\n")

    def remover_livro(self):
        self.listar_livros()

        if not self.livros:
            return
        
        try:
            indice = int(input("Número do livro:")) - 1

            removido = self.livros.pop(indice)

            print(f"\nLivro '{removido.titulo}' removido!")

        except:
            print("\nOpção inválida.\n")

def menu():

    biblioteca = Biblioteca()

    while True:
        print("=== Sistema de Bibloteca ===")
        print("1 - Adicionar Livro")
        print("2 - Listar Livros")
        print("3 - Emprestar Livro")
        print("4 - Devolver Livro")
        print("5 - Remover Livro")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            biblioteca.adicionar_livro()

        elif opcao == "2":
            biblioteca.listar_livros()
        
        elif opcao == "3":
            biblioteca.emprestar_livro()

        elif opcao == "4":
            biblioteca.devolver_livro()

        elif opcao == "5":
            biblioteca.remover_livro()

        elif opcao == "0":
            print("\nEncerrando sistema...")
            break

        else:
            print("\nOpção inválida.\n")

menu()