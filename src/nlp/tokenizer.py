import re
from transformers import BertTokenizer, GPT2Tokenizer, RobertaTokenizer

class Tokenizer:
    def __init__(self, model_name='bert-base-uncased'):
        self.model_name = model_name
        self.tokenizer = self.load_tokenizer(model_name)

    def load_tokenizer(self, model_name):
        """Load the appropriate tokenizer based on the model name."""
        if 'gpt2' in model_name:
            return GPT2Tokenizer.from_pretrained(model_name)
        elif 'roberta' in model_name:
            return RobertaTokenizer.from_pretrained(model_name)
        else:
            return BertTokenizer.from_pretrained(model_name)

    def tokenize(self, text):
        """Tokenize input text into tokens."""
        tokens = self.tokenizer.tokenize(text)
        return tokens

    def detokenize(self, tokens):
        """Convert tokens back to text."""
        text = self.tokenizer.convert_tokens_to_string(tokens)
        return text

    def encode(self, text, add_special_tokens=True):
        """Encode text into token IDs."""
        return self.tokenizer.encode(text, return_tensors='pt', add_special_tokens=add_special_tokens)

    def decode(self, token_ids, skip_special_tokens=True):
        """Decode token IDs back to text."""
        return self.tokenizer.decode(token_ids[0], skip_special_tokens=skip_special_tokens)

    def batch_tokenize(self, texts):
        """Tokenize a batch of texts."""
        return [self.tokenize(text) for text in texts]

    def batch_encode(self, texts, add_special_tokens=True):
        """Encode a batch of texts into token IDs."""
        return self.tokenizer.batch_encode_plus(
            texts,
            return_tensors='pt',
            padding=True,
            truncation=True,
            add_special_tokens=add_special_tokens
        )

    def batch_decode(self, token_ids_list, skip_special_tokens=True):
        """Decode a batch of token IDs back to text."""
        return [self.decode(token_ids, skip_special_tokens) for token_ids in token_ids_list]

    def get_special_tokens(self):
        """Get special tokens used by the tokenizer."""
        return {
            "pad_token": self.tokenizer.pad_token,
            "unk_token": self.tokenizer.unk_token,
            "cls_token": self.tokenizer.cls_token,
            "sep_token": self.tokenizer.sep_token,
            "mask_token": self.tokenizer.mask_token,
        }

    def is_subword_token(self, token):
        """Check if a token is a subword token."""
        return re.match(r'^\w+##\w+$', token) is not None

    def tokenize_with_subwords(self, text):
        """Tokenize text and indicate subword tokens."""
        tokens = self.tokenize(text)
        return [(token, self.is_subword_token(token)) for token in tokens]
