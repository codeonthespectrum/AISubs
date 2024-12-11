import whisper
import os
import ffmpeg
from mtranslate import translate
from datetime import timedelta

os.environ ["IMAGEMAGICK_BINARY"] = "/usr/local/bin/convert"

def extract_audio(video_path):
    print("Extraíndo áudio do vídeo...")
    audio_path = "audio.wav"
    ffmpeg.input(video_path).output(audio_path).run(overwrite_output=True)
    print(f"Áudio extraído e salvo em {audio_path}")
    return audio_path

def transcribe_audio(audio_path):
    print("Transcrevendo áudio...")
    model = whisper.load_model("large-v1")
    result = model.transcribe(audio_path, verbose=True)
    print(f"Transcrição: {result['text']}")
    return result['text'], result['language']

def translate_subs(text, target_language = "pt"):
    print(f"Traduzindo para {target_language}...")
    try:
        text = str(text)
        translated_text = translate(text, target_language)
        if not translated_text:
            raise ValueError("Falha na tradução.")
        print(f"Texto traduzido: {translated_text}")
        return translated_text
    except Exception as e:
        print(f"Erro na tradução: {e}")
        raise
    

def save_srt (translated_text, video_duration, srt_path="output.srt"):
    print("Gerando legendas...")
    lines = translated_text.split(".")
    segment_duration = video_duration / len(lines)

    with open(srt_path, "w") as srt_file:
        for i, line in enumerate(lines, start=1):
            start_time = timedelta(seconds=int((i-1) * segment_duration))
            end_time = timedelta(seconds=int(i * segment_duration))

            srt_file.write(f"{i} \n")
            srt_file.write(f"{str (start_time) [:8]},000 --> {str (end_time) [:8]}, 000\n")
            srt_file.write(f"{line.strip()}\n\n")

        print(f"Arquivo de legendas salvo em {srt_path}")
        return srt_path

def process_video(video_path):
    print(f"Processando vídeo {video_path}...")
    audio_path = extract_audio(video_path)
    transcription = transcribe_audio(audio_path)
    translated_text = translate_subs(transcription)

    video_duration = ffmpeg.probe(video_path)['format']['duration']
    video_duration = float(video_duration)

    srt_path = os.path.splitext(video_path)[0] + "translated.srt"
    save_srt (translated_text, video_duration, srt_path)

    print(f"Arquivo de legenda traduzido salvo em {srt_path}.")
    return srt_path

if __name__ == "__main__":
    video_path = "/usr/pasta/seu_video.mp4"
    srt_path = process_video(video_path)
    print(f"Processamento concluído. Arquivo de legenda traduzido salvo em {srt_path}.")