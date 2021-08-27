import csv
from collections import OrderedDict
from itertools import chain, product

final_values = []

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            value = int(row[1])
            percent = int(row[2])
            # print(value + (value/percent))
            final_values.append(round(value + (value/percent), 2))
        except:
            pass

# print(final_values)

list_of_actions = [
    ('action_1', 20, 5), 
    ('action_2', 30, 10),
    ('action_3', 50, 15), 
    ('action_4', 70, 20),
    ('action_5', 60, 17), 
    ('action_6', 80, 25),
    ('action_7', 22, 7)
]


def create_combinaisons_list(list_of_actions):
    """ list_of_actions est une liste de p-uplets """
    nb = len(list_of_actions) # nombre d'éléments
    n = 2 ** nb # nombre de total_of_combinaisons
    total_of_combinaisons = [] # l'ensemble des total_of_combinaisons

    for i in range(1, n):
        binary_combinaison = bin(i)[2:] # écriture de i sur nb bits
        combinaison = [] # construction d'une combinaison
        for j in range(len(binary_combinaison)):
            if binary_combinaison[j] == "1":
                combinaison.append(list_of_actions[j])
        total_of_combinaisons.append(combinaison) # la partie construite est ajoutée à la liste
    return total_of_combinaisons


def valeur_total(liste):
    valeur = 0
    for triplet in liste:
        valeur += triplet[1]
    return valeur

def profit_total(liste):
    profit = 0
    for triplet in liste:
        profit += triplet[2]
    return profit


def check_for_the_best_combinaison(total_of_combinaisons, limit_value):
    profit_max = 0
    valeur_max = 0
    solution = []
    for combinaison in total_of_combinaisons: # un choix possible de fichiers
        profit = profit_total(combinaison)
        valeur = valeur_total(combinaison)
        if valeur <= limit_value and profit > profit_max:
            profit_max = profit
            valeur_max = valeur
            solution = combinaison
    return solution, profit_max, valeur_max

def bruteforce(list_of_actions, limit_value):
    total_of_combinaisons = create_combinaisons_list(list_of_actions)
    return check_for_the_best_combinaison(total_of_combinaisons, limit_value)
    
choix = bruteforce(list_of_actions, 165)

profit_total = choix[1]
valeur_total = choix[2]
choix_fichiers = [fichier[0] for fichier in choix[0]]
print(choix_fichiers, valeur_total, profit_total)

