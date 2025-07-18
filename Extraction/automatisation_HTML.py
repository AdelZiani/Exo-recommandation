import requests

import html

import re

PATH = "../../Exo-recommandation-data/données_exercices/exercices_autres/WayToLearn/"


regenonces = r"<h6>Exercice [0-9]+:</h6>\\n<p>(.*?)<"
regsoluces = r"<pre class=\"EnlighterJSRAW\" data-enlighter-language=\"python\">(.*?)</"
clust = 58
url = "https://waytolearnx.com/2024/09/exercice-corrige-numpy-partie-9.html"
response = requests.get(url)
content = str(response.content)

enonces = re.findall(regenonces, str(content))
solutions = re.findall(regsoluces, str(content))

for i in range(len(enonces)):
    enonces[i] = bytes(enonces[i], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8')
    f = open(PATH + "Enonces/WayToLearn_"+str(clust) +"_"+ str(i)+".txt", "w")
    f.write(enonces[i])
    f.close

for i in range(len(solutions)):
    solutions[i] = html.unescape(solutions[i])
    solutions[i] = bytes(solutions[i], 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8')
    f = open(PATH + "Solutions/WayToLearn_"+str(clust) +"_"+ str(i)+".py", "w")
    f.write(solutions[i])
    f.close

print(len(solutions), "  ", len(enonces))

#print(content)
