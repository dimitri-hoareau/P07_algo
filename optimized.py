import csv

final_values = []
list_of_actions =[]

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            value = int(row[1])
            percent = round(int(row[1]) + (int(row[1]) * int(row[2])/100), 2)
            print(percent)
            list_of_actions.append((row[0], value, percent))
        except:
            pass

# Solution optimale - programmation dynamique
def sacADos_dynamique(capacite, elements):

    # matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]
    matrice = []
    for x in range(len(elements) + 1):
        matrice_line = []
        for x in range(capacite + 1):
            matrice_line.append(0)
        matrice.append(matrice_line)

    for i in range(1, len(elements) + 1): # on parcourt les lignes
        for w in range(1, capacite + 1): # on parcourt chaque element de ligne
            if elements[i-1][1] <= w: # si le poid < capacité du sac
                matrice[i][w] = max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w]) # on compare avec le résultat optimisé de la ligne d'avant met dans la matrice le maximum
            else:
                matrice[i][w] = matrice[i-1][w] # sinon on garde la solution optimisé de la ligne d'avant

    # Retrouver les éléments en fonction de la somme
    w = capacite
    n = len(elements)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = elements[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]

        n -= 1

    return round(matrice[-1][-1], 2), elements_selection

# Nom
# poids
# Valeur

print('Algo dynamique', sacADos_dynamique(500, list_of_actions))

# # https://cache.media.eduscol.education.fr/file/NSI/63/7/RA20_NSI_G_T_progdyn_1298637.pdf


# explication bien https://www.youtube.com/watch?v=wDsZhd1wEuk


# # TODO => bon calcul des pourcentages + renommer variables + ordre décroissant de valeur !!
# faire la solution de bruteforce de algomius
# faire un fichier de test avec moins de données et des tableaux de 5 éléments
# slide avec code + arbre + matrice