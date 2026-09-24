from pathlib import Path
import pandas as pd

#Define a pasta onde estão os arquivos CSV
PASTA_ENTRADA = Path(r"") #Coloque aqui o caminho da pasta de entrada

#Define a pasta onde os arquivos Excel convertidos serão salvos
PASTA_SAIDA = Path(r"") #Coloque aqui o caminho da pasta de saída

#Cria a pasta de saída caso ela ainda não exista
PASTA_SAIDA.mkdir(exist_ok=True)

for arquivo in PASTA_ENTRADA.glob("*.csv"):

    try:
    
        print(f"Convertendo {arquivo.name}...")

        df = pd.read_csv(arquivo)

        destino = PASTA_SAIDA / f"{arquivo.stem}.xlsx"

        df.to_excel(destino, index=False)

    except Exception as e:
        print(f"Erro em {arquivo.name}: {e}")

print("Conversão concluída com sucesso!")