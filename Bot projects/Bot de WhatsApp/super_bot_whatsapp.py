def menu():
    print("1 - Enviar Email")
    print("2 - Enviar WhatsApp")

    escolha = input("Escolha: ")

    if escolha == "1":
        email = input("Seu email: ")
        senha = input("Senha app: ")
        destino = input("Destino: ")
        assunto = input("Assunto: ")
        msg = input("Mensagem: ")

        enviar_email(email,senha,destino,assunto,msg)

    elif escolha == "2":
        numero = input("Número (+55...): ")
        msg = input("Mensagem: ")
        hora = input("Hora: ")
        minuto = input("Minuto: ")

        enviar_whatsapp(numero,msg,hora,minuto)
    
    else:
        print("Opção inválida")

menu()