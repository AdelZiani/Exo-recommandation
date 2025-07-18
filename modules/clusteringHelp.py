from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN

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

def get_values(keys, dico):
    ret = []
    for elem in keys:
        ret.append(dico[elem])
    return ret

def kmeans(i, dico):
    keys = list(dico.keys())
    print(keys)
    values = get_values(keys, dico)
    means = KMeans(i,n_init=20).fit(keys)
    labels = means.labels_
    print_cluster(values, labels)

def hierarchical_clustering(i, dico):
    keys = list(dico.keys())
    values = get_values(keys, dico)
    clustering = AgglomerativeClustering(n_clusters=i).fit(keys)
    labels = clustering.labels_
    print_cluster(values, labels)
    from_children_to_tree(clustering.children_, len(clustering.labels_), dico)


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
    model = DBSCAN(eps=5.0, min_samples=2) # 6 à l'air d'être un epsilon raisonnable peut être à légerement ajuster
    model.fit(lst)
    labels = model.labels_
    print_cluster(values, labels)

def define_list_of_tag(file):
    f = open(file, "r")
    lst = set()
    line = None
    while line != '':
        line = f.readline().removesuffix("\n")
        if line not in lst and not line.startswith("#"):
            lst.add(line)
    f.close()
    return list(lst)

def read_clusters(file, order):
    f = open(file, "r")
    pred = [None for elem in order]
    num_cluster = -1
    line =None
    while line != "":
        line = f.readline()
        if line.startswith('#'):
            num_cluster+=1
        else:
            index = order.index(line.removesuffix("\n"))
            if pred[index] == None:
                pred[index] = num_cluster
    f.close()
    return pred
