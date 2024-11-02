import json
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OfflineTranslator:
    def __init__(self, dictionary_file='offline_dictionary.json'):
        """Initialize the offline translator."""
        self.dictionary_file = dictionary_file
        self.translations = self.load_dictionary()
        logging.info("Offline Translator initialized.")

    def load_dictionary(self):
        """Load the translation dictionary from a JSON file."""
        if os.path.exists(self.dictionary_file):
            with open(self.dictionary_file, 'r') as file:
                logging.info("Loaded translation dictionary from file.")
                return json.load(file)
        logging.warning("Dictionary file not found. Starting with an empty dictionary.")
        return {}

    def save_dictionary(self):
        """Save the current translation dictionary to a JSON file."""
        with open(self.dictionary_file, 'w') as file:
            json.dump(self.translations, file, indent=4)
            logging.info("Saved translation dictionary to file.")

    def add_translation(self, source_text: str, translated_text: str):
        """Add a new translation to the dictionary."""
        self.translations[source_text] = translated_text
        self.save_dictionary()
        logging.info(f"Added translation: '{source_text}' -> '{translated_text}'.")

    def translate(self, source_text: str) -> str:
        """Translate the source text using the offline dictionary."""
        translated_text = self.translations.get(source_text, None)
        if translated_text:
            logging.info(f"Translated '{source_text}' to '{translated_text}'.")
            return translated_text
        else:
            logging.warning(f"No translation found for '{source_text}'.")
            return f"[No translation found for '{source_text}']"

    def display_dictionary(self):
        """Display all translations in the dictionary."""
        if not self.translations:
            print("No translations available.")
            return
        for source, translation in self.translations.items():
            print(f"{source} -> {translation}")

# Example usage
if __name__ == "__main__":
    translator = OfflineTranslator()

    # Adding translations
    translator.add_translation("Hello", "Hola")
    translator.add_translation("Goodbye", "Adiós")

    # Translating text
    print(translator.translate("Hello"))  # Output: Hola
    print(translator.translate("Goodbye"))  # Output: Adiós
    print(translator.translate("Thank you"))  # Output: [No translation found for 'Thank you']

    # Displaying the dictionary
    translator.display_dictionary()
