from transformers import AutoTokenizer, AutoModel
import torch



camembertav2 = AutoModel.from_pretrained("microsoft/codebert-base")
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
inputs = tokenizer("entrées clavier, conversion de chaines de caractères, opérations numériques, import de bibliothèque", return_tensors="pt")
inputs2 = tokenizer("input, operations, cast, import", return_tensors="pt")
tokens = inputs.tokens()
tokens2 = inputs2.tokens()

