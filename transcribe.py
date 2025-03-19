import os
from pathlib import Path
from openai import OpenAI
from config import get_config

CONFIG = get_config()
API_KEY = CONFIG["api_key"]

def transcribe_audio(client, audio_file_path):
    """Transcribe audio using OpenAI client"""
    with open(audio_file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=CONFIG["model"],
            file=audio_file
        )
    return transcription.text

def process_audio_folder(input_folder, output_folder):
    """Process all audio files in folder"""
    client = OpenAI(api_key=API_KEY)
    
    Path(output_folder).mkdir(exist_ok=True)
    
    audio_extensions = ['.mp3', '.wav', '.m4a', '.mp4', '.webm', '.mpeg']
    audio_files = [f for f in os.listdir(input_folder)
                  if os.path.splitext(f)[1].lower() in audio_extensions]
    
    for filename in audio_files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, 
                                 f"{os.path.splitext(filename)[0]}.txt")
        
        if os.path.exists(output_path):
            print(f"Skipping {filename} - exists")
            continue
            
        try:
            transcription = transcribe_audio(client, input_path)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(transcription)
            print(f"Processed {filename}")
        except Exception as e:
            print(f"Failed {filename}: {str(e)}")

if __name__ == "__main__":
    # Validate config
    if not API_KEY:
        print("Missing API_KEY in .env file")
        exit(1)
        
    input_folder = input("Audio files folder: ").strip()
    output_folder = input("Output folder [transcriptions]: ").strip() or "transcriptions"
    
    process_audio_folder(input_folder, output_folder)