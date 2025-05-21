PATH = "../Exo-recommandation-data/données_exercices/exercices_autres/Developpez/solutions/"

def delete_commentary(file):
    comment = False
    content = ""
    f = open(file, 'r')
    line = f.readline()
    while line != "":
        if not line.startswith("\"\"\"") and not line.startswith("#"):
            content += line
        line = f.readline()
    f.close()
    f = open(file, "w")
    f.write(content)
    f.close()



for i in range(2, 22):
    delete_commentary(PATH + "Developpez-14-2-"+ str(i)+".py")