import requests
from config import API_KEY, BASE_URL

def obter_clima(cidade):
    parametros = {
        "q" : cidade,
        "appid" : API_KEY,
        "units" : "metric",
        "lang" : "pt_br"
    }

    resposta = requests.get(BASE_URL, params=parametros)

    if resposta.status_code != 200:
        print("Cidade não encontrada ou ocorreu um erro na requisição.")
        return
    
    dados = resposta.json()

    nome = dados["name"]
    pais = dados["sys"]["country"]
    temperatura = dados["main"]["temp"]
    sensacao = dados["main"]["feels_like"]
    umidade = dados["main"]["humidity"]
    descricao = dados["weather"][0]["description"]
    vento = dados["wind"]["speed"]

    print("=" * 40)
    print(f"Cidade: {nome}, {pais}")
    print(f"Temperatura: {temperatura}°C")
    print(f"Sensação Térmica: {sensacao}°C")
    print(f"Umidade: {umidade}%")
    print(f"Descrição: {descricao}")
    print(f"Velocidade do Vento: {vento} m/s")
    print("=" * 40)

def main():
    print("=== Bot de Previsão do Tempo ===")

    while True:
        cidade = input("\nDigite o nome da cidade (ou 'sair' para encerrar): ")

        if cidade.lower() == "sair":
            break

        obter_clima(cidade)

if __name__ == "__main__":
    main()