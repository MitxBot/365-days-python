import yt_dlp

PATH = "="  #Caminho para o diretório onde os vídeos serão salvos

def baixar_video(url, qualidade="best", nome_saida="video"):
    """
    Baixa um vídeo de plataformas suportadas.
    
    Parâmetros:
        url (str): URL do vídeo.
        qualidade (str): Qualidade desejada (ex: 'best', 'worst', '720p', '1080p').
        nome_saida (str): Nome do arquivo de saída (sem extensão).
    """

    # Define o formato com base na qualidade escolhida
    if qualidade.lower() in ["best", "worst"]:
        formato = qualidade
    else:
        # Tenta pegar a resolução exata (ex: '720p' -> 'bestvideo[height=720]+bestaudio')
        try:
            altura = int(qualidade.replace("p", ""))
            formato = f"bestvideo[height={altura}]+bestaudio/best"
        except ValueError:
            print("Qualidade inválida, usando 'best'.")
            formato = "best"

    opcoes = {
        'format': formato,
        'outtmpl': f'{nome_saida}.%(ext)s',
        'merge_output_format': 'mp4',  # Garante saída em MP4
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    print("=== Downloader com yt-dlp ===")
    url = input("Digite a URL do vídeo: ").strip()
    qualidade = input("Qualidade desejada (ex: 1080p, 720p, best, worst): ").strip()
    nome_saida = input("Nome do arquivo de saída (sem extensão): ").strip()

    baixar_video(url, qualidade, nome_saida)
    print("Download concluído!")