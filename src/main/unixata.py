import sys
import logging
from config import Config
from nlp.translator import Translator
from cultural.context_recognition import ContextRecognizer
from user_interface import UserInterface

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Unixata:
    def __init__(self):
        self.config = Config()
        self.translator = Translator(self.config)
        self.context_recognizer = ContextRecognizer(self.config)
        self.ui = UserInterface(self.translator, self.context_recognizer)

    def run(self):
        logger.info("Starting Unixata Universal Translation System...")
        self.ui.start()

if __name__ == "__main__":
    try:
        unixata_app = Unixata()
        unixata_app.run()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)
