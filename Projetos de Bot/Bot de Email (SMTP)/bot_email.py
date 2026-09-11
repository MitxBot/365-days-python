import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(remetente,senha,destinatario,assunto,mensagem):
    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = assunto

    msg.attach(MIMEText(mensagem,"plain"))

    try:
        servidor = smtplib.SMTP("smtp.gmail.com",587)
        servidor.starttls()
        servidor.login(remetente,senha)

        servidor.send_message(msg)
        servidor.quit()

        print("Email enviado com sucesso!")

    except Exception as e:
        print("Erro ao enviar:",e)
        
#Exemplo de uso

enviar_email(
    remetente="seuemail@gmail.com",
    senha="SSENHA_DE_APP",
    destinatario="destino@email.com",
    assunto="Teste Bot Python",
    mensagem="Olá! Esse é um email automático enviado por Python"
)

"""
O Gmail não aceita senha normal, você precisa de uma senha de app.
Ative a verificação em 2 etapas na conta.
Gere a senha em: Conta Google → Segurança → Senhas de app.
"""