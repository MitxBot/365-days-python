variaveis = {}

def interpretar(linha):
    partes = linha.split()

    if partes[0] == "print":
        print(variaveis.get(partes[1],partes[1]))

    elif "=" in linha:
        var,valor = linha.split("=")
        variaveis[var.strip()] = valor.strip()

#Teste

interpretar("x=10")
interpretar("print x")