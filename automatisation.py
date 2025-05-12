f = open("../Exo-recommandation-data/exercices_autres/Developpez/data.txt", "r")



content = ""
file = None
line = ""
while(line!= None):
    line = f.readline()

    if line.startswith("1"):
        if file != None:
            file.write(content)
            content = ""
        file = open("../Exo-recommandation-data/exercices_autres/Developpez/exercices/" + "Developpez-"+ line[:-1] + ".txt", "w")
    else:
        content +=line 
"""
for i in range(20):
    v = True
    while v:
       line = f.readline()
        if line.startswith("1"):
            if file != None:
                file.write(content)
                content = ""
                file = open("../Exo-recommandation-data/exercices_autres/Developpez/solutions/" + "Developpez-"+ line + ".txt", "w")
        else:
            content +=line
            """