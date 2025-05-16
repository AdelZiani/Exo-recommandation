from transformers import AutoTokenizer, AutoModel
import torch

from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN



#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

def to_dict(vectors,words):
    dico = {}
    for i in range(len(words)):
        dico[tuple(vectors[i].detach().numpy().tolist())] = words[i]
    return dico

def get_values(keys, dico):
    ret = []
    for elem in keys:
        ret.append(dico[elem])
    return ret

def print_cluster(values, clusters):
    true_values = []
    dico = {}
    for elem in values:
        tag = ""
        for token in elem:
            tag+=token
        true_values.append(tag)
    for i in range (len(clusters)):
        dico.setdefault(clusters[i], []).append(true_values[i])
    for key in dico:
        print("\n\n")
        if key == -1:
            print("Noise----------------------------------------------\n")
        else:    
            print("Cluster -------------------------------------------\n")
        
        for elem in dico[key]:
            print(elem)
    print("\n\n")

def kmeans(i, dico):
    keys = list(dico.keys())
    values = get_values(keys, dico)
    means = KMeans(i,n_init=20).fit(keys)
    labels = means.labels_
    print_cluster(values, labels)

def from_children_to_tree(children, nb_labels, refs):
    lst = list(refs.keys())
    dico = {}
    for i in range(nb_labels):
        dico[i] = [refs[lst[i]]]
    i = nb_labels
    for elem in children:
        values = get_values(lst, refs)
        dico[i] = dico[elem[0]] + dico[elem[1]]
        dico.pop(elem[0])
        dico.pop(elem[1])

        print("Etape " + str(i - nb_labels) + " : ")
        print("     Cluters existants:")
        print("                 " + str(values))
        print("      Cluster Construit:")
        print ("                " + str(dico[i]))
        i += 1

def DBScan(dict):
    dico = {}
    lst = list(dict.keys())
    values = get_values(lst, dict)
    model = DBSCAN(eps=10.0, min_samples=2) # 6 à l'air d'être un epsilon raisonnable peut être à légerement ajuster
    model.fit(lst)
    labels = model.labels_
    print_cluster(values, labels)

def hierarchical_clustering(i, dico):
    keys = list(dico.keys())
    values = get_values(keys, dico)
    clustering = AgglomerativeClustering(n_clusters=i).fit(keys)
    labels = clustering.labels_
    print_cluster(values, labels)
    from_children_to_tree(clustering.children_, len(clustering.labels_), dico)

# Sentences we want sentence embeddings for
sentences =[
    "library import",
    "variable initialization",
    "data input",
    "casting",
    "float type",
    "calculation with PI",
    "real division",
    "screen display of text and variable value",
    "print function call",
    "arithmetic operator /",
    "arithmetic operator *",
    "keyboard input",
    "string to number conversion",
    "numeric operations",
    "library import",
    "input",
    "variables",
    "operations",
    "casting",
    "import",
    "modulo operator",
    "division operator"
]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers-testing/stsb-bert-tiny-safetensors')
model = AutoModel.from_pretrained('sentence-transformers-testing/stsb-bert-tiny-safetensors')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, mean pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

dico = to_dict(sentence_embeddings, sentences)


print("\nkmeans +++++++++++++++++++++++++++++++++++++++++++++\n")
kmeans(5, dico)
print("\nhierarchical ++++++++++++++++++++++++++++++++++++++++++++\n")
hierarchical_clustering(5, dico)
print("\nDBSCAN ++++++++++++++++++++++++++++++++++++++++++\n")
DBScan(dico)