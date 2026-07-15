import string

def analisar_texto(texto):
    texto = texto.strip()

    caracteres = len(texto)

    caracteres_sem_espaços = len(texto.replace(" ",""))

    texto_limpo = texto.translate(str.maketrans("","",string.punctuation))

    palavras = texto_limpo.split()

    quantidade_palavras = len(palavras)

    palavras_unicas = len(set(palavras))

    print("===== RESULTADO =====")
    print(f"Palavras: {quantidade_palavras}")
    print(f"Palavras únicas: {palavras_unicas}")
    print(f"Caracteres: {caracteres}")
    print(f"Caracteres (sem espaços): {caracteres_sem_espaços}")

while True:
    print("\n===== CONTADOR DE PALAVRAS =====")
    print("1 - Digitar um texto")
    print("2 - Ler texto de um arquivo (.txt)")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        texto = input("\nDigite o texto: \n")
        analisar_texto(texto)

    elif opcao == "2":
        nome_arquivo = input("Nome do arquivo: ")

        try:
            with open(nome_arquivo,"r",encoding="utf-8") as arquivo:
                texto = arquivo.read()
                analisar_texto(texto)

        except FileNotFoundError:
            print("Arquivo não encontrado!")

    elif opcao == "3":
        print("\nPrograma encerrado.")
        break

    else:
        print("Opção inválida!")