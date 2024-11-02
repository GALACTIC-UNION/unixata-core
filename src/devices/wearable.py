import speech_recognition as sr
import pyttsx3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WearableTranslator:
    def __init__(self, language='en'):
        """Initialize the wearable translator."""
        self.language = language
        self.recognizer = sr.Recognizer()
        self.synthesizer = pyttsx3.init()
        self.synthesizer.setProperty('voice', self.get_voice_by_language(language))
        logging.info("Wearable translator initialized.")

    def get_voice_by_language(self, language):
        """Get the appropriate voice for the specified language."""
        voices = self.synthesizer.getProperty('voices')
        for voice in voices:
            if language in voice.languages:
                return voice.id
        return voices[0].id  # Default to the first voice if none found

    def listen_and_translate(self):
        """Listen for speech and translate it."""
        with sr.Microphone() as source:
            logging.info("Listening for speech...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio, language=self.language)
                logging.info(f"Recognized text: {text}")
                return text
            except sr.UnknownValueError:
                logging.error("Could not understand audio.")
                return None
            except sr.RequestError as e:
                logging.error(f"Could not request results from Google Speech Recognition service; {e}")
                return None

    def speak(self, text):
        """Speak the translated text."""
        self.synthesizer.say(text)
        self.synthesizer.runAndWait()
        logging.info(f"Spoken text: {text}")

    def translate_and_speak(self, text, target_language):
        """Translate the text and speak it in the target language."""
        # Placeholder for translation logic
        translated_text = f"[Translated to {target_language}]: {text}"  # Replace with actual translation logic
        self.speak(translated_text)
