import whisper
import os
import ffmpeg
import argparse
import tempfile
from mtranslate import translate
from datetime import timedelta
import sys

#os.environ ["IMAGEMAGICK_BINARY"] = "/usr/local/bin/convert"

def extract_audio(video_path):
    try:
        print("Extraíndo áudio do vídeo...")
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
            audio_path = temp_audio.name
            ffmpeg.input(video_path).output(audio_path, acodec='pcm_s16le').run(overwrite_output=True, quiet=True)
            print(f"Áudio extraído e salvo em {audio_path}")
            return audio_path
    except ffmpeg.Error as e:
        print(f"Erro ao extrair áudio: {e.stderr.decode('utf-8')}")
        raise

def transcribe_audio(audio_path, model):
    try:
        print("Transcrevendo áudio...")
        result = model.transcribe(audio_path, verbose=True)
        print("Transcrição concluída")
        return result['text'], result['language'], result['segments']
    except Exception as e:
        print(f"Erro na transcrição: {e}")
        raise
        
      

def translate_subs(text, target_language = "pt"):
    try:
        if not text:
            raise ValueError("Texto vazio não pode ser traduzido.")
        translated_text = translate(text, target_language)
        return translated_text.strip()
    except Exception as e:
        print(f"Erro na tradução: {e}")
        return text
        
def save_srt (segments, translated_segments, srt_path):
    try:
        print("Gerando legendas...")
        with open(srt_path, "w") as srt_file:
            for i, (segment, translated_text) in enumerate(zip(segments, translated_segments), start=1):
                start_seconds = segment['start']
                end_seconds = segment['end']

                def format_time(seconds):
                    hours = int(seconds // 3600)
                    minutes = int((seconds % 3600) // 60)
                    secs = int (seconds % 60)
                    millis = int((seconds - int(seconds)) * 1000)
                    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"
                
                
                start_time = format_time(start_seconds)
                end_time = format_time(end_seconds)
                srt_file.write(f"{i}\n{start_time} --> {end_time}\n{translated_text}\n\n")
        print(f"Arquivo de legenda salvo em {srt_path}")
    except IOError as e:
        print(f"Erro ao salvar arquivo de legenda: {e}")
        raise

def process_video(video_path, target_language = "pt"):
    model = whisper.load_model("large-v1")

    try:
        audio_path = extract_audio(video_path)
        text, language, segments = transcribe_audio(audio_path, model)
        translated_segments = [translate_subs(seg['text'], target_language) for seg in segments]
        srt_path = os.path.splitext(video_path)[0] + "translated.srt"
        save_srt(segments, translated_segments, srt_path)

        return srt_path
    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)
            print(f"Áudio temporário removido: {audio_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gera legendas traduzidas para vídeos")
    parser.add_argument("video_path", help="Caminho para o arquivo de vídeo")
    parser.add_argument("--target", "-t", help="Idioma para tradução (padrão: pt)", default="pt")
    args = parser.parse_args()

    try:
        srt_path = process_video(args.video_path,args.target)
        print(f"Processamento concluído. Arquivo de legenda traduzido salvo em {srt_path}.")
    except Exception as e:
        print(f"Erro ao processar vídeo: {e}")
        sys.exit(1)