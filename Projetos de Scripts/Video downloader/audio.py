import yt_dlp

PATH = ""#Necessário usar \\ ao invés \

def baixar_audio(url, nome_saida):
    opcoes = {
        'format': 'bestaudio/best',  #Baixa o melhor áudio disponível
        'outtmpl': f'{nome_saida}.mp3',  #Define o nome do arquivo de saída
        'extractaudio': True,  #Extrai o áudio
        'audioformat': 'mp3',  #Converte para MP3
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  #Qualidade de 192 kbps
        }],
    }
    
    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Digite a URL do vídeo: ")
    nome_saida = input("Digite o nome do arquivo de saída (sem extensão): ")
    baixar_audio(url, nome_saida)
    print(f"Áudio baixado como {nome_saida}.mp3")

"""
O script baixa o aúdio de determinado vídeo.
"""