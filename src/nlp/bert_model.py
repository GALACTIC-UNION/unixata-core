import torch
from torch import nn
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

class BertModel:
    def __init__(self, model_name='bert-base-uncased', num_labels=2):
        """Initialize the BERT model for sequence classification."""
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)

    def encode_data(self, texts, labels=None, max_length=128):
        """Encode the input texts and labels into the format required by BERT."""
        encodings = self.tokenizer(texts, truncation=True, padding=True, max_length=max_length, return_tensors='pt')
        if labels is not None:
            encodings['labels'] = torch.tensor(labels)
        return encodings

    def train(self, train_texts, train_labels, eval_texts=None, eval_labels=None, epochs=3, batch_size=16):
        """Train the BERT model on the provided training data."""
        train_encodings = self.encode_data(train_texts, train_labels)
        eval_encodings = self.encode_data(eval_texts, eval_labels) if eval_texts and eval_labels else None

        train_dataset = torch.utils.data.TensorDataset(train_encodings['input_ids'], train_encodings['attention_mask'], train_encodings['labels'])
        eval_dataset = torch.utils.data.TensorDataset(eval_encodings['input_ids'], eval_encodings['attention_mask'], eval_encodings['labels']) if eval_encodings else None

        training_args = TrainingArguments(
            output_dir='./results',
            num_train_epochs=epochs,
            per_device_train_batch_size=batch_size,
            per_device_eval_batch_size=batch_size,
            evaluation_strategy='epoch',
            logging_dir='./logs',
            logging_steps=10,
            save_total_limit=2,
            load_best_model_at_end=True,
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            compute_metrics=self.compute_metrics,
        )

        trainer.train()
        return trainer

    def compute_metrics(self, p):
        """Compute accuracy, precision, recall, and F1 score."""
        preds = p.predictions.argmax(-1)
        precision, recall, f1, _ = precision_recall_fscore_support(p.label_ids, preds, average='weighted')
        acc = accuracy_score(p.label_ids, preds)
        return {
            'accuracy': acc,
            'f1': f1,
            'precision': precision,
            'recall': recall
        }

    def predict(self, texts):
        """Make predictions on new texts."""
        encodings = self.encode_data(texts)
        with torch.no_grad():
            outputs = self.model(encodings['input_ids'], attention_mask=encodings['attention_mask'])
        predictions = outputs.logits.argmax(dim=-1)
        return predictions.numpy()

    def save_model(self, save_directory):
        """Save the model and tokenizer to the specified directory."""
        self.model.save_pretrained(save_directory)
        self.tokenizer.save_pretrained(save_directory)

    def load_model(self, load_directory):
        """Load the model and tokenizer from the specified directory."""
        self.model = BertForSequenceClassification.from_pretrained(load_directory)
        self.tokenizer = BertTokenizer.from_pretrained(load_directory)
