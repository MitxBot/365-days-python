from pathlib import Path
import pandas as pd

PASTA_ENTRADA = Path(r"")
PASTA_SAIDA = Path(r"")

PASTA_SAIDA.mkdir(exist_ok=True)

for arquivo in PASTA_ENTRADA.glob("*.csv"):

    try:
    
        print(f"Convertendo {arquivo.name}...")

        df = pd.read_csv(arquivo)

        destino = PASTA_SAIDA / f"{arquivo.stem}.xlsx"

        df.to_excel(destino, index=False)

    except Exception as e:
        print(f"Erro em {arquivo.name}: {e}")

print("Conversão concluída!")