from openpyxl import load_workbook

#Abre a planilha

planilha = load_workbook("")#Nome do arquivo

#Seleciona a aba ativa

aba = planilha.active

#Cabeçalho

aba [""] = ""

#Percorre as linhas

for linha in range(2,aba.max_row +1):
    quantidade = aba[f"B{linha}"].value
    preco = aba[f"C{linha}"].value

    total = quantidade * preco

    aba[f"D{linha}"] = total

#Salva as alterações

planilha.save("")#Nome do arquivo

print("Planilha atualizada!")