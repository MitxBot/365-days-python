from pypdf import PdfReader

arquivo_pdf = "documento.pdf"

reader = PdfReader(arquivo_pdf)

texto = ""

for pagina in reader.pages:
    texto += pagina.extract_text() + "\n"

print(texto)