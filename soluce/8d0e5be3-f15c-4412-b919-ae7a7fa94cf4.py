def insertion_triee2(liste, element):
    liste.append(element)
    
    for i in range(len(liste)-1, 0, -1):
        if liste[i] >= liste[i-1]:
            break
        liste[i], liste[i-1] = liste[i-1], liste[i]