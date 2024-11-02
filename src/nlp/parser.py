import spacy

class Parser:
    def __init__(self, model='en_core_web_sm'):
        """Initialize the parser with a specified language model."""
        self.nlp = spacy.load(model)

    def parse(self, text):
        """Parse input text and return syntactic and semantic information."""
        doc = self.nlp(text)
        parsed_data = {
            "tokens": [(token.text, token.pos_, token.dep_, token.lemma_) for token in doc],
            "entities": [(ent.text, ent.label_, ent.start_char, ent.end_char) for ent in doc.ents],
            "sentences": [sent.text for sent in doc.sents],
            "dependencies": [(token.text, token.dep_, token.head.text) for token in doc],
            "noun_chunks": [(chunk.text, chunk.root.text) for chunk in doc.noun_chunks],
            "language": doc.lang_
        }
        return parsed_data

    def parse_batch(self, texts):
        """Parse a batch of texts and return their syntactic and semantic information."""
        results = []
        for text in texts:
            results.append(self.parse(text))
        return results

    def get_entity_types(self):
        """Get unique entity types recognized by the model."""
        return set(ent.label_ for ent in self.nlp.vocab if ent.has_vector)

    def visualize_dependencies(self, text):
        """Visualize the dependency parse of the input text."""
        doc = self.nlp(text)
        return [(token.text, token.dep_, token.head.text) for token in doc]

    def visualize_entities(self, text):
        """Visualize the named entities in the input text."""
        doc = self.nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents]

    def summarize(self, text):
        """Provide a summary of the parsed information."""
        parsed_data = self.parse(text)
        summary = {
            "total_tokens": len(parsed_data["tokens"]),
            "total_entities": len(parsed_data["entities"]),
            "total_sentences": len(parsed_data["sentences"]),
            "language": parsed_data["language"]
        }
        return summary
