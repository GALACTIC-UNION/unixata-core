import logging

logger = logging.getLogger(__name__)

class UserInterface:
    def __init__(self, translator, context_recognizer):
        self.translator = translator
        self.context_recognizer = context_recognizer

    def start(self):
        print("Welcome to the Unixata Universal Translation System!")
        print("Type 'exit' to quit the application.")
        
        while True:
            source_text = input("\nEnter text to translate (or 'exit' to quit): ")
            if source_text.lower() == 'exit':
                print("Exiting the application. Goodbye!")
                break
            
            source_lang = input("Enter source language (or press Enter to auto-detect): ")
            target_lang = input("Enter target language (default: fr): ") or self.translator.config.default_target_language
            
            # Recognize cultural context
            context = self.context_recognizer.recognize_context(source_text)
            print(f"Cultural context recognized: {context}")

            # Perform translation
            translated_text = self.translator.translate(source_text, source_lang or None, target_lang)
            if translated_text is not None:
                print(f"Translated text: {translated_text}")
            else:
                print("Translation failed. Please try again.")

            # Ask if the user wants to translate another text
            continue_translation = input("Do you want to translate another text? (y/n): ")
            if continue_translation.lower() != 'y':
                print("Exiting the application. Goodbye!")
                break

    def batch_translate(self):
        """Allow users to translate multiple texts in one go."""
        print("Batch Translation Mode")
        print("Type 'done' when you are finished entering texts.")
        
        translations = []
        while True:
            source_text = input("Enter text to translate (or 'done' to finish): ")
            if source_text.lower() == 'done':
                break
            
            source_lang = input("Enter source language (or press Enter to auto-detect): ")
            target_lang = input("Enter target language (default: fr): ") or self.translator.config.default_target_language
            
            # Recognize cultural context
            context = self.context_recognizer.recognize_context(source_text)
            print(f"Cultural context recognized: {context}")

            # Perform translation
            translated_text = self.translator.translate(source_text, source_lang or None, target_lang)
            if translated_text is not None:
                translations.append((source_text, translated_text))
                print(f"Translated text: {translated_text}")
            else:
                print("Translation failed for this text. Please try again.")

        print("\nBatch Translation Results:")
        for original, translated in translations:
            print(f"Original: {original} | Translated: {translated}")
