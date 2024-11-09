import os
from google.cloud import translate_v2 as translate

LANGUAGE_MAP = {
    "Tamil": "ta",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Chinese": "zh",
    "Japanese": "ja",
    "Arabic": "ar",
    "Russian": "ru"
}

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/cra/Downloads/sarvamm/Third Shade Translation.json"

def translate_text(source_language: str, text: str):
    translate_client = translate.Client()
    result = translate_client.translate(text, source_language=LANGUAGE_MAP.get(source_language, "en"), target_language="en")
    return result["translatedText"]
