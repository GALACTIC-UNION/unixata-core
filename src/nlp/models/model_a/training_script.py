from transformers import Trainer, TrainingArguments, BertForSequenceClassification, BertTokenizer
from datasets import load_dataset

def train_model():
    dataset = load_dataset("glue", "mrpc")
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased")
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    def tokenize_function(examples):
        return tokenizer(examples["sentence1"], examples["sentence2"], truncation=True)

    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
        load_best_model_at_end=True,
        metric_for_best_model="accuracy",
        greater_is_better=True,
        save_total_limit=2,
        save_steps=500,
        eval_steps=500,
        logging_dir="./logs",
        logging_strategy="steps",
        logging_first_step=True,
        push_to_hub=False,
        report_to="none",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["validation"],
        compute_metrics=lambda pred: {"accuracy": torch.sum(pred.label_ids == pred.predictions.argmax(-1)).item()},
    )

    trainer.train()
