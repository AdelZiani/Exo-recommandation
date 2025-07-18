def insertion_triee3(liste, element):
    for position in range(len(liste)):
        if liste[position] >= element:
            break
    liste.insert(position, element)