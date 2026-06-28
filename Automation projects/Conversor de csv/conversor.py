from pathlib import Path
import pandas as pd

PASTA_ENTRADA = Path("")
PASTA_SAIDA = Path("")

PASTA_SAIDA.mkdir(exist_ok=True)

for arquivo in PASTA_ENTRADA.glob("*.csv"):

    print(f"Convertendo {arquivo.name}...")

    df = pd.read_csv(arquivo)

    destino = PASTA_SAIDA / f"{arquivo.stem}.xlsx"

    df.to_excel(destino, index=False)

print("Conversão concluída!")