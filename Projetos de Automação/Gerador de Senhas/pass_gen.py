import random
import string

tamanho = int(input("Tamanho da senha: "))

caracteres = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

senha = ""

for _ in range(tamanho):
    senha += random.choice(caracteres)

print(f"Senha gerada: {senha}")