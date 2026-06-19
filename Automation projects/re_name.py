from pathlib import Path

caminho = input("Digite o caminho da pasta: ")
nome = input("Digite um novo nome: ")#A saída será: nomeEscolhido_001

pasta = Path(caminho)

arquivos = [a for a in pasta.iterdir() if a.is_file()]

for i, arquivo in enumerate(arquivos,start=1):

    novo_nome = f"{nome}_{i:03d}{arquivo.suffix}"

    arquivo.rename(pasta / novo_nome)
    
print(f"{len(arquivos)} arquivos renomeados.")