import re

def verificar_senha(senha):
    pontuacao = 0
    problemas = []

    #Tamanho

    if len(senha) >= 8:
        pontuacao += 1

    else:
        problemas.append("A senha deve ter pelo menos 8 caracteres.")

    
    #Letra maiúscula

    if re.search(r"[A-Z]",senha):
        pontuacao += 1

    else:
        problemas.append("Adicione pelo menos uma letra maiúscula.")

    #Letra minúscula

    if re.search(r"[a-z]",senha):
        pontuacao += 1

    else:
        problemas.append("Adicione pelo menos uma letra minúscula.")

    #Número

    if re.search(r"\d",senha):
        pontuacao += 1

    else:
        problemas.append("Adicione pelo menos um número.")

    #Caractere especial

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]",senha):
        pontuacao += 1

    else:
        problemas.append("Adicione pelo menos um caractere especial.")

    return pontuacao,problemas

def nivel_senha(pontuacao):
    if pontuacao == "5":
        return "Senha muito forte!"
    
    elif pontuacao == "4":
        return "Forte"
    
    elif pontuacao == "3":
        return "Média"
    
    elif pontuacao == "2":
        return "Fraca"
    
    else:
        return "Muito fraca"
    
print("=" * 40)
print("=== Verificador de Senhas ===")
print("=" * 40)

senha = input("Digite uma senha: ")

pontuacao,problemas = verificar_senha(senha)

print("\nResultado: ")
print("-" * 40)
print(f"Pontuação: {pontuacao}/5")
print(f"Nível: {nivel_senha(pontuacao)}")

if problemas:
    print("\nSugestões para melhorar: ")
    for problema in problemas:
        print(f"- {problema}")

else:
    print("\nParabéns! Sua senha atende a todos os critérios de segurança.")