# simple_translation.py

from translation_module import Translator  # Replace with your actual translation module

def main():
    # Initialize the translator
    translator = Translator()

    # Example text to translate
    text_to_translate = "Hello, how are you?"
    target_language = "es"  # Spanish

    # Perform the translation
    translated_text = translator.translate(text_to_translate, target_language)

    # Display the result
    print(f"Original Text: {text_to_translate}")
    print(f"Translated Text ({target_language}): {translated_text}")

if __name__ == "__main__":
    main()
