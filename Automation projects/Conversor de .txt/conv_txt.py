from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

entrada = Path(r"")#Pasta de entrada
saida = Path(r"")#Pasta de saida

saida.mkdir(parents=True,exist_ok=True)

styles = getSampleStyleSheet()

for arquivo in entrada.glob("*.txt"):
    
    destino = saida / f"{arquivo.stem}.pdf"

    with open(arquivo, encoding="utf-8") as f:
        texto = f.read()

    doc = SimpleDocTemplate(destino)

    doc.build([
        Paragraph(texto,styles["Normal"])
    ])

    print(f"{arquivo.name} foi convertido para PDF.")

"""
O script converte todos arquivos .txt de uma determinada pasta para .pdf
"""