import re

def check(str):
    motif = 'ab+?'
    if re.search(motif, str):
        return 'Une correspondance trouvée!'
    else:
        return('Pas de correspondance!')

print(check("ac"))
print(check("a"))
print(check("ab"))
print(check("abc"))