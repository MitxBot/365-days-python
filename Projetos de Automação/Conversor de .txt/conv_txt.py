from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

entrada = Path(r"") #Define a pasta onde estão os arquivos .txt
saida = Path(r"") #Define a pasta onde os PDFs convertidos serão salvos

#Cria a pasta de saída caso ela ainda não exista e também cria as pastas que estiverem faltando no caminho
saida.mkdir(parents=True,exist_ok=True)

#Obtém alguns estilos de texto prontos do ReportLab
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