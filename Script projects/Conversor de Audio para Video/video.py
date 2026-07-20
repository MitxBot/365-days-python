from moviepy.editor import AudioFileClip, ImageClip

def audio_para_video():
    #Pega os caminhos a partir da entrada do usuário.
    audio_path = input("Digite o caminho do arquivo de áudio: ")
    image_path = input("Digite o caminho da imagem: ")
    output_path = input("Digite o nome do arquivo de saída (ex: video.mp4): ")

    #Carrega o áudio.
    audio = AudioFileClip(audio_path)

    #Cria clipe de imagem com duração igual ao áudio.
    imagem = ImageClip(image_path).set_duration(audio.duration)

    #Adiciona o áudio ao vídeo.
    video = imagem.set_audio(audio)

    #Exporta como mp4.
    video.write_videofile(output_path, fps=24)

if __name__ == "__main__":
    audio_para_video()
"""
O script cria um video com uma imagem estática e audio de fundo, como uma faixa de uma banda com uma capa de álbum.
"""