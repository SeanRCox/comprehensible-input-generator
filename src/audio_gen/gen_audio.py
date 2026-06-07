import os

from datetime import date
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from gen_text import gen_text
from pathlib import Path

def gen_audio():
    load_dotenv()
    ELEVENLABS_KEY = os.getenv('ELEVENLABS_KEY')
    client = ElevenLabs(api_key=ELEVENLABS_KEY)

    texts = gen_text()
    audio_num = 1

    WINDOWS_PATH = os.getenv('WINDOWS_PATH')
    WINDOWS_PATH += str(date.today())
    folder_path = Path(WINDOWS_PATH)
    folder_path.mkdir(parents=True, exist_ok=True)

    for text in texts:
        audio_iterator = client.text_to_speech.convert(
            text=text,
            voice_id="OSwaPSNdfituxkWcjlkR",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128"
        )

        save_path = WINDOWS_PATH + f"/audio_{audio_num}"
        text_save = save_path + ".txt"
        audio_save = save_path + ".mp3"

        with open(text_save, "w") as f:
            f.write(text)

        with open(audio_save, "wb") as f:
            for chunk in audio_iterator:
                f.write(chunk) 

        audio_num += 1
    

if __name__ == "__main__":
    gen_audio()