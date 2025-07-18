from transformers import AutoTokenizer, AutoModel
import torch

SBERT = 'sentence-transformers-testing/stsb-bert-tiny-safetensors'
CAMEMBERT = "almanach/camembertav2-base"
CODEBERT = "microsoft/codebert-base"

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

def to_dict(vectors,words):
    dico = {}
    for i in range(len(words)):
        dico[tuple(vectors[i].detach().numpy().tolist())] = words[i]
    return dico

def get_dict_vectors(model, sentences):
    sentence_embeddings = vectorize(model, sentences)
    return to_dict(sentence_embeddings, sentences)

def vectorize(model, sentences):
    tokenizer = AutoTokenizer.from_pretrained(model)
    model = AutoModel.from_pretrained(model)
    encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = model(**encoded_input)
    return to_dict(mean_pooling(model_output, encoded_input['attention_mask']), sentences)