PATH = "../../Exo-recommandation-data/données_exercices/exercices_autres/Github/46/"
PATHSOURCE = "../../Exo-recommandation-data/exercices_autres/Github/46-Simple-Python-Exercises-Solutions-master/"

for i in range(1, 38):
    state = 0
    if i > 9:
        f = open(PATHSOURCE+ "problem_" +str(i)+".py", 'r')
    else:
        f = open(PATHSOURCE+ "problem_0" +str(i)+".py", 'r')
    enonce = open(PATH + "enonces/problem_"+str(i)+ ".txt", 'w')
    soluce = open(PATH + "soluces/problem_"+str(i)+ ".py",'w')
    f.readline()
    line = "ff"

    while line != "":
        line = f.readline()
        if line.startswith("\'\'\'"):
            state = 1
            continue
        if state == 0:
            enonce.write(line)
        else:
            soluce.write(line)
        print(line)
    enonce.close()
    soluce.close()