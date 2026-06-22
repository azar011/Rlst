import os
from dotenv import load_dotenv

load_dotenv()

MODEL_TYPE = os.getenv("MODEL_TYPE", "whisper")

if MODEL_TYPE == "seamless":
    from Rlst.Speech_recognition.app.services.seamless_service import translate_audio

else:
    from Rlst.Speech_recognition.app.services.whisper_service import translate_audio
    