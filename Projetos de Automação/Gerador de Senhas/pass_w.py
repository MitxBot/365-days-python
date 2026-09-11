import secrets
import string
import random

tamanho = int(input("Digite o tamanho da senha: "))

senha = [
    secrets.choice (string.ascii_lowercase),
    secrets.choice (string.ascii_uppercase),
    secrets.choice (string.digits),
    secrets.choice (string.punctuation)
]

todos = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

while len(senha) < tamanho:
    senha.append(secrets.choice(todos))

    random.shuffle(senha)

print("Senha gerada: ", ''.join(senha))

"""
Está versão garante que exista pelo menos um de cada tipo de caractere.
"""