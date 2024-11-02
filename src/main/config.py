import os

class Config:
    def __init__(self):
        self.language_pairs = {
            "en": ["fr", "es", "zh", "de", "ru"],
            "fr": ["en", "es", "zh", "de", "ru"],
            "es": ["en", "fr", "zh", "de", "ru"],
            # Add more language pairs as needed
        }
        self.default_source_language = "en"
        self.default_target_language = "fr"
        self.api_key = os.getenv("UNIXATA_API_KEY", "your_api_key_here")
        self.cultural_context_db_path = os.getenv("CULTURAL_CONTEXT_DB", "path/to/cultural_context.db")
        self.model_path = os.getenv("MODEL_PATH", "path/to/models/")
        self.logging_level = os.getenv("LOGGING_LEVEL", "INFO")

    def get_language_pairs(self):
        return self.language_pairs

    def get_default_languages(self):
        return self.default_source_language, self.default_target_language

    def get_api_key(self):
        return self.api_key

    def get_cultural_context_db_path(self):
        return self.cultural_context_db_path

    def get_model_path(self):
        return self.model_path

    def get_logging_level(self):
        return self.logging_level
