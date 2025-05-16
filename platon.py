import requests, json, os


f = open("exercicesPlaton.txt", 'w')
url = "https://platon.univ-eiffel.fr/api/v1/resources"
valeur = os.getenv('TOKENPLATON')
headers = {
    "accept": "*/*",
    "Authorization": valeur
}

session=requests.Session()

try:
    response = session.get(url, headers=headers, timeout=5)
except requests.exceptions.RequestException as e:
    print(e)

js = response.json()
js = js["resources"]
js2 = []

for elem in js:
    if elem["topics"] != []:
        for elem2 in elem["topics"]:
            if(elem2["name"] == "Python"):
                if elem["type"] == "EXERCISE":
                    js2.append((elem, elem["status"]))
ids = []
for elem,status in js2:
    ids.append((elem["id"], status))


i = 0
j=0
annex = open("../Exo-recommandation-data/données_exercices/exercices_autres/platon/platon_annex.txt", "w")
for id, status in ids:
    urlsoluce = "https://platon.univ-eiffel.fr/api/v1/files/compile/"+id+"/json"

    urlenonces = "https://platon.univ-eiffel.fr/api/v1/player/preview"


    body= {
        "version": "latest",
        "resource": id,
        "overrides":{}
    }
    responsesoluce = requests.post(urlsoluce, headers=headers, data="").json()
    if "variables" in responsesoluce and "soluce" in responsesoluce["variables"]:
        responseenonce = requests.post(urlenonces, headers=headers, data="", json=body).json()
        if "exercise" in responseenonce and "statement" in responseenonce["exercise"]:
            urlauthor = "https://platon.univ-eiffel.fr/api/v1/users/" + responseenonce["exercise"]["author"]
            responseauthor = requests.get(urlauthor, headers=headers).json()
            #annex.write(str(i) + " / " + id + " / " + responseenonce["exercise"]["title"] + " / " + responseauthor["resource"]["firstName"] + " " + responseauthor["resource"]["lastName"] + " / " + status + "\n")
            #print(json.dumps(responseenonce, indent=4))
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            enonce = open("./Exos/enonces/"+id+".txt", "w")
            soluce = open("./Exos/soluce/"+id+".py", "w")
            soluce.write(responsesoluce["variables"]["soluce"])
            enonce.write(responseenonce["exercise"]["statement"])
            enonce.close()
            soluce.close()
            i+=1

    js = response.json()
print (i)
