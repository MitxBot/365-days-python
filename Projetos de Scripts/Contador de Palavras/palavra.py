import string
from pathlib import Path

def analisar_texto(texto):
    texto = texto.strip()

    caracteres = len(texto)

    caracteres_sem_espaços = len(texto.replace(" ",""))

    texto_limpo = texto.translate(str.maketrans("","",string.punctuation))

    palavras = texto_limpo.split()

    quantidade_palavras = len(palavras)

    palavras_unicas = len(set(palavras))

    print("=== Resultado ===")
    print(f"Palavras: {quantidade_palavras}")
    print(f"Palavras únicas: {palavras_unicas}")
    print(f"Caracteres: {caracteres}")
    print(f"Caracteres (sem espaços): {caracteres_sem_espaços}")

while True:
    print("\n=== Contador de Palavras ===")
    print("1 - Digitar um texto")
    print("2 - Ler texto de um arquivo (.txt)")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        texto = input("\nDigite o texto: \n")
        analisar_texto(texto)

    elif opcao == "2":
        caminho = Path(input("\nDigite o caminho do arquivo (.txt): ").strip())#Necessário colocar da seguinte forma: C:\Users\Usuario\Documents\Pasta\arquivo.txt

        if not caminho.exists():
            print("\nArquivo não encontrado!")

        elif caminho.suffix.lower() != ".txt":
            print("\nO arquivo precisa ser do tipo .txt")

        else:
            try:
                texto = caminho.read_text(encoding="utf-8")
                analisar_texto(texto)

            except Exception as erro:
                print(f"\nErro ao ler o arquivo: {erro}")

    elif opcao == "3":
        print("\nPrograma encerrado.")
        break

    else:
        print("Opção inválida!")