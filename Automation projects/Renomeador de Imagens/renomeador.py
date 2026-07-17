import os
from pathlib import Path

def renomear_imagens(pasta, nome_base="imagem"):
    pasta = Path(pasta)

    # Filtra apenas arquivos de imagem comuns
    extensoes_validas = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"]
    imagens = [f for f in pasta.iterdir() if f.suffix.lower() in extensoes_validas]

    # Ordena por data de criação
    imagens.sort(key=lambda f: f.stat().st_ctime)

    for i, img in enumerate(imagens, start=1):
        # Se for menor que 10, adiciona zero à esquerda
        if i < 10:
            novo_nome = f"{nome_base} 0{i}{img.suffix.lower()}"
        else:
            novo_nome = f"{nome_base} {i}{img.suffix.lower()}"

        novo_caminho = pasta / novo_nome
        os.rename(img, novo_caminho)
        print(f"Renomeado: {img.name} -> {novo_nome}")

# Coloque o caminho da pasta onde estão suas imagens
renomear_imagens(r"", nome_base="")#O caminho deve conter \\ e não \.O valor do nome desejado deve ser colocado em nome_base.

"""
Um script simples que renomeia e organiza as imagens de uma pasta para nome específicado pelo usuário, as imagens são organizadas pela data de criação.
"""