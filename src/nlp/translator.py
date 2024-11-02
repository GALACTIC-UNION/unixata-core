import logging
from transformers import MarianMTModel, MarianTokenizer, pipeline
from langdetect import detect, DetectorFactory

# Set a seed for consistent language detection results
DetectorFactory.seed = 0

logger = logging.getLogger(__name__)

class Translator:
    def __init__(self, config):
        self.config = config
        self.models = {}
        self.tokenizers = {}
        self.load_models()

    def load_models(self):
        """Load translation models for each language pair defined in the config."""
        for source_lang, target_langs in self.config.language_pairs.items():
            for target_lang in target_langs:
                model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
                logger.info(f"Loading model: {model_name}")
                self.models[(source_lang, target_lang)] = MarianMTModel.from_pretrained(model_name)
                self.tokenizers[(source_lang, target_lang)] = MarianTokenizer.from_pretrained(model_name)

    def detect_language(self, text):
        """Detect the language of the input text."""
        try:
            lang = detect(text)
            logger.info(f"Detected language: {lang}")
            return lang
        except Exception as e:
            logger.error(f"Language detection failed: {e}")
            return self.config.default_source_language  # Fallback to default

    def translate(self, text, source_lang=None, target_lang=None):
        """Translate text from source language to target language."""
        if source_lang is None:
            source_lang = self.detect_language(text)
        
        if target_lang is None:
            target_lang = self.config.default_target_language

        if (source_lang, target_lang) not in self.models:
            logger.error(f"Translation model not available for {source_lang} to {target_lang}.")
            raise ValueError(f"Translation model not available for {source_lang} to {target_lang}.")

        logger.info(f"Translating from {source_lang} to {target_lang}: {text}")
        try:
            # Tokenize the input text
            tokenizer = self.tokenizers[(source_lang, target_lang)]
            model = self.models[(source_lang, target_lang)]
            inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
            # Perform translation
            translated = model.generate(**inputs)
            # Decode the translated text
            translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
            logger.info(f"Translated text: {translated_text}")
            return translated_text
        except Exception as e:
            logger.error(f"Translation failed: {e}")
            return None  # Return None in case of failure
