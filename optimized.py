import csv

final_values = []
list_of_actions =[]

# with open('data.csv', 'r') as file:
# with open('dataset1_Python+P7.csv', 'r') as file:
with open('dataset2_Python+P7.csv', 'r') as file:
    next(file)
    reader = csv.reader(file)
    for row in reader:
        try:
            value = int(float(row[1]) * 100)
            percent = value * (float(row[2]))/100
            # percent = int(percent)
            if value > 0:
                list_of_actions.append((row[0], value, percent))
        except:
            pass

list_of_actions.sort(key=lambda value:value[2], reverse=True )

def sacADos_dynamique(capacite, list_of_actions):






    

    # matrice = [[0 for x in range(capacite + 1)] for x in range(len(list_of_actions) + 1)] #synthaxe optimisée
    matrice = []
    for x in range(len(list_of_actions) + 1):
        matrice_line = []
        for x in range(capacite + 1):
            matrice_line.append(0) # permet de construire les lignes de la matrice

        matrice.append(matrice_line) # permet d'associer les lignes de la matrice

    for i in range(1, len(list_of_actions) + 1): # on parcourt les lignes
        for w in range(1, capacite + 1): # on parcourt chaque element de ligne à travers les colonnes
            if list_of_actions[i-1][1] <= w: # si le poid < capacité du sac
                matrice[i][w] = max(list_of_actions[i-1][2] + matrice[i-1][round(w-list_of_actions[i-1][1])], matrice[i-1][w]) # on compare avec le résultat optimisé de la ligne d'avant met dans la matrice le maximum
            else:
                matrice[i][w] = matrice[i-1][w] # sinon on garde la solution optimisé de la ligne d'avant

    # Retrouver les éléments en fonction de la somme
    w = capacite
    number_of_actions = len(list_of_actions)
    list_of_actions_selection = []

    while w >= 0 and number_of_actions >= 0:
        e = list_of_actions[number_of_actions-1]
        if matrice[number_of_actions][w] == matrice[number_of_actions-1][w-e[1]] + e[2]:
            list_of_actions_selection.append(e)
            w -= e[1]

        number_of_actions -= 1

        total_price = 0
        list_of_actions_names = []
        for element in list_of_actions_selection:
            total_price += element[1]
            list_of_actions_names.append(element[0])

        # print(total_price)
        total_benefit = round(matrice[-1][-1], 2)
        total_benefit = round(total_benefit / 100, 2)

    return total_benefit, list_of_actions_names, total_price/100

# Nom
# poids
# Valeur

print('Algo dynamique', sacADos_dynamique(50000, list_of_actions))

# # https://cache.media.eduscol.education.fr/file/NSI/63/7/RA20_NSI_G_T_progdyn_1298637.pdf


# explication bien https://www.youtube.com/watch?v=wDsZhd1wEuk


# # TODO => bon calcul des pourcentages + renommer variables + ordre décroissant de valeur !!
# faire la solution de bruteforce de algomius
# faire un fichier de test avec moins de données et des tableaux de 5 éléments
# slide avec code + arbre + matrice
# big O

#https://ichi.pro/fr/notation-big-o-complexite-de-calcul-206781157312338

# multiplier par 100 OK
# classer par valeur OK
# supprimer si negatif OK
# rediviser par 100 OK
# donner la valeur totale en dessous des 500 OK
#corriger percent pour brutforce
# passer le csv en parametre
# README
#slide comparaiosn derniere

#198.55 /197.96