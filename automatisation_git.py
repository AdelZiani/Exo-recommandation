PATH = "../Exo-recommandation-data/exercices_autres/Github/"
f = open(PATH + "PythonGithub.txt", "r")
i = 0

content = ""
line = ""
state = "SEARCH_QUESION"
while line != None:
    line = f.readline()
    if line.startswith("Question"):
        print("Questionn")
        state = "QUESTION"
        if content != "":
            file = open(PATH + "Correction/Github" + str(i) +".py", "w")
            file.write(content)
            file.close()
            content = ""
            i+=1

    elif line.startswith("Hint"):
        State="SEARCH_ANSWER"
    elif line.startswith("Solution"):
        state="ANSWER"
        if content != "":
            file = open(PATH + "Exo/Github" + str(i) +".txt", "w")
            file.write(content)
            file.close()
            content = ""
    else:
        if state == "QUESTION" or state=="ANSWER":
            content += line