from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import torch

class SentimentAnalyzer:
    def __init__(self, model_name='distilbert-base-uncased-finetuned-sst-2-english'):
        """Initialize the sentiment analyzer with a specified model."""
        self.model_name = model_name
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.sentiment_pipeline = pipeline("sentiment-analysis", model=self.model, tokenizer=self.tokenizer)

    def analyze(self, text):
        """Analyze sentiment of the input text."""
        result = self.sentiment_pipeline(text)
        return result

    def analyze_batch(self, texts):
        """Analyze sentiment for a batch of texts."""
        results = self.sentiment_pipeline(texts)
        return results

    def get_sentiment_labels(self):
        """Get the sentiment labels used by the model."""
        return self.sentiment_pipeline.model.config.id2label

    def fine_tune_model(self, train_dataset, eval_dataset, training_args):
        """Fine-tune the sentiment analysis model on a custom dataset."""
        from transformers import Trainer

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
        )
        trainer.train()
        return trainer

    def predict_sentiment(self, text):
        """Predict sentiment for a single text input."""
        result = self.analyze(text)
        return result[0]  # Return the first result

    def summarize_sentiment(self, texts):
        """Provide a summary of sentiment analysis results for a batch of texts."""
        results = self.analyze_batch(texts)
        summary = {
            "positive": sum(1 for res in results if res['label'] == 'POSITIVE'),
            "negative": sum(1 for res in results if res['label'] == 'NEGATIVE'),
            "neutral": sum(1 for res in results if res['label'] == 'NEUTRAL'),
            "total": len(results)
        }
        return summary
