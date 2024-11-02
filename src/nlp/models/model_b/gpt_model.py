import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments

class GPTModel:
    def __init__(self, model_name='gpt2'):
        """Initialize the GPT model for text generation."""
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)

    def encode_data(self, texts, max_length=1024):
        """Encode the input texts into the format required by GPT-2."""
        encodings = self.tokenizer(texts, truncation=True, padding=True, max_length=max_length, return_tensors='pt')
        return encodings

    def train(self, train_texts, epochs=3, batch_size=2):
        """Train the GPT model on the provided training data."""
        train_encodings = self.encode_data(train_texts)

        train_dataset = torch.utils.data.TensorDataset(train_encodings['input_ids'], train_encodings['attention_mask'])

        training_args = TrainingArguments(
            output_dir='./results',
            num_train_epochs=epochs,
            per_device_train_batch_size=batch_size,
            save_steps=10_000,
            save_total_limit=2,
            logging_dir='./logs',
            logging_steps=200,
            load_best_model_at_end=True,
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
        )

        trainer.train()
        return trainer

    def generate_text(self, prompt, max_length=50, num_return_sequences=1):
        """Generate text based on a given prompt."""
        input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
        with torch.no_grad():
            outputs = self.model.generate(
                input_ids,
                max_length=max_length,
                num_return_sequences=num_return_sequences,
                no_repeat_ngram_size=2,
                early_stopping=True
            )
        return [self.tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

    def save_model(self, save_directory):
        """Save the model and tokenizer to the specified directory."""
        self.model.save_pretrained(save_directory)
        self.tokenizer.save_pretrained(save_directory)

    def load_model(self, load_directory):
        """Load the model and tokenizer from the specified directory."""
        self.model = GPT2LMHeadModel.from_pretrained(load_directory)
        self.tokenizer = GPT2Tokenizer.from_pretrained(load_directory)
