import tkinter as tk

#Janela Principal

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.resizable(False,False)

#Variável que guarda o que aparece no visor

expressao = ""

#Função para adicionar números e operadores

def adicionar(valor):
    global expressao

    expressao += str(valor)
    visor.delete(0,tk.END)
    visor.insert(0,expressao)

#Função para Calcular

def calcular():
    global expressao

    try:
        resultado = eval(expressao)
        visor.delete(0,tk.END)
        visor.insert(0,resultado)
        expressao = str(resultado)

    except:
        visor.delete(0,tk.END)
        visor.insert(0,"Erro")
        expressao = ""

#Função para Limpar

def limpar():
    global expressao

    expressao = ""
    visor.delete(0,tk.END)

#Visor

visor = tk.Entry(
    janela,
    font=("Arial",24),
    justify="right"
)

visor.pack(
    padx=10,
    pady=20,
    fill="x"
)

#Área dos Botões

frame = tk.Frame(janela)
frame.pack()

#Botões

botoes = [
    ("7", 0, 0),
    ("8", 0, 1),
    ("9", 0, 2),
    ("/", 0, 3),

    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("*", 1, 3),

    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("-", 2, 3),

    ("0", 3, 0),
    (".", 3, 1),
    ("+", 3, 2),
    ("=", 3, 3),
]

for texto,linha,coluna in botoes:

    if texto == "=":
        comando = calcular

    else:
        comando = lambda valor=texto: adicionar(valor)

    botao = tk.Button(
        frame,
        text=texto,
        font=("Arial",18),
        width=5,
        height=2,
        command=comando
    )

    botao.grid(
        row=linha,
        column=coluna,
        padx=2,
        pady=2
    )

#Botão Limpar

botao_limpar = tk.Button(
    janela,
    text="C",
    font=("Arial", 18),
    width=22,
    height=2,
    command=limpar
)

botao_limpar.pack(pady=10)

#Mantém a janela aberta

janela.mainloop()