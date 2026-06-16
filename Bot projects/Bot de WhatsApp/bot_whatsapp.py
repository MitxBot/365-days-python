import pywhatkit as kit

def enviar_whatsapp(numero,mensagem,hora,minuto):
    try:
        kit.sendwhatsmsg(numero,mensagem,hora,minuto)
        print("Mensagem agendada com sucesso!")
    except Exception as e:
        print("Erro!",e)

#Exemplo

enviar_whatsapp(
    numero="+5511999999999", #Formato internacional
    mensagem="Olá! Mensagem automática",
    hora=15,
    minuto=30
)
"""
Esse método usa o WhatsApp Web (abre o navegador automaticamente).
Necessário pywhatkit
<<<pip install pywhatkit>>>
"""