import logging
import re

logger = logging.getLogger(__name__)

class ContextRecognizer:
    def __init__(self, config):
        self.config = config
        self.cultural_contexts = self.load_cultural_contexts()

    def load_cultural_contexts(self):
        """Load cultural contexts from a database or file."""
        # For simplicity, we will use a hardcoded dictionary
        return {
            "greeting": ["hello", "hi", "hey", "greetings", "salutations"],
            "farewell": ["goodbye", "bye", "see you", "take care"],
            "gratitude": ["thank you", "thanks", "appreciate"],
            "apology": ["sorry", "apologize", "my bad"],
            "request": ["please", "could you", "would you mind"],
            "compliment": ["great", "awesome", "fantastic", "wonderful"],
            # Add more contexts as needed
        }

    def recognize_context(self, text):
        """Recognize cultural context based on input text."""
        logger.info(f"Recognizing context for text: {text}")
        text_lower = text.lower()
        recognized_contexts = []

        for context, keywords in self.cultural_contexts.items():
            # Use regex to match keywords in a case-insensitive manner
            pattern = r'\b(?:' + '|'.join(map(re.escape, keywords)) + r')\b'
            if re.search(pattern, text_lower):
                recognized_contexts.append(context)
                logger.info(f"Context recognized: {context}")

        if recognized_contexts:
            return recognized_contexts
        else:
            logger.info("No specific cultural context recognized.")
            return ["general"]  # Default context if none recognized
