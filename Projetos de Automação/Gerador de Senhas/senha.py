import secrets
import string

def gerar_senha(tamanho):
    caracteres = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    return "".join(
        secrets.choice(caracteres)
        for _ in range(tamanho)
    )

tamanho = int(input("Tamanho da senha: "))

print("Senha gerada:", gerar_senha(tamanho))

"""
Versão melhorada do gerador de senhas, utilizando a biblioteca "secrets" para maior segurança das senhas geradas.
O código permite ao usuário especificar o tamanho da senha desejada e inclui letras maiúsculas, minúsculas, números e caracteres especiais para aumentar a complexidade da senha.
"""