import requests
from bs4 import BeautifulSoup
import os

url_pagina = ""#URL da página

#Pasta para salvar as imagens
pasta_destino = ""
os.makedirs(pasta_destino, exist_ok=True)

try:
    #Fazer o download da página
    resposta = requests.get(url_pagina)
    resposta.raise_for_status()  #Verifica se a requisição foi bem-sucedida

    #Processar o HTML
    soup = BeautifulSoup(resposta.text, "html.parser")

    #Encontrar todas as tags <img>
    tags_img = soup.find_all("img")

    #Baixar cada imagem relevante
    for i, tag in enumerate(tags_img):
        #Extrair o atributo 'src'
        src = tag.get("src")
        if src:
            #Ignorar imagens com palavras-chave indesejadas
            palavras_chave = ["icon", "thumb", "avatar"]
            if any(palavra in src for palavra in palavras_chave):
                print(f"Ignorando: {src}")
                continue

            #Ignorar imagens pequenas (opcional)
            largura = tag.get("width")
            altura = tag.get("height")
            if largura and altura and (int(largura) < 200 or int(altura) < 200):
                print(f"Ignorando imagem pequena: {src}")
                continue

            #Tratar URLs relativas
            if not src.startswith("http"):
                src = url_pagina + src
            
            #Baixar a imagem
            print(f"Baixando: {src}")
            img_resposta = requests.get(src)
            img_resposta.raise_for_status()

            #Nome do arquivo
            nome_arquivo = os.path.join(pasta_destino, f"imagem_{i + 1}.jpg")

            #Salvar o arquivo
            with open(nome_arquivo, "wb") as f:
                f.write(img_resposta.content)
            print(f"Imagem salva em: {nome_arquivo}")
except Exception as e:
    print(f"Erro ao processar a página: {e}")