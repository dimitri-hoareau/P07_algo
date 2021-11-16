import csv

final_values = []
list_of_actions =[]

with open('data.csv', 'r') as file:
# with open('dataset1_Python+P7.csv', 'r') as file:
# with open('dataset2_Python+P7.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            value = float(row[1])
            percent = float(row[2])
            list_of_actions.append((row[0], value, percent))
        except:
            pass


def int_to_bin(n, nb):
    """ n et nb sont de type int
        n est le nombre à convertir en binaire
        nb est le nombre de bits utilisés """
    ch = ""
    while n > 0:
        r = n % 2
        n = n // 2
        ch = str(r) + ch
    ch = (nb - len(ch)) * "0" + ch
    return ch

def create_combinaisons_list(list_of_actions):
    """ list_of_actions est une liste de p-uplets """
    number_of_elements = len(list_of_actions) # nombre d'éléments
    number_of_combinaisons = 2 ** number_of_elements # nombre de total_of_combinaisons
    total_of_combinaisons = [] # l'ensemble des total_of_combinaisons

    for i in range(1, number_of_combinaisons):
        binary_combinaison = int_to_bin(i, number_of_elements) # écriture de i sur nb bits

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
        rounded_profit = round((triplet[1] * triplet[2]/100), 2)
        profit += rounded_profit
    return profit


def check_for_the_best_combinaison(total_of_combinaisons, limit_value):
    profit_max = 0
    valeur_max = 0
    solution = [] 
    for combinaison in total_of_combinaisons: 
        profit = profit_total(combinaison) # on teste le profit total pour chaque combinaison
        valeur = valeur_total(combinaison) # on teste la valeur totale pour chaque combinaison
        if valeur <= limit_value and profit > profit_max: 
            profit_max = profit
            valeur_max = valeur
            solution = combinaison
    return solution, valeur_max, profit_max

def bruteforce(list_of_actions, limit_value):
    total_of_combinaisons = create_combinaisons_list(list_of_actions) # récupère la liste de toutes les combinaisons
    return check_for_the_best_combinaison(total_of_combinaisons, limit_value)
    
choix = bruteforce(list_of_actions, 500)
valeur_total = choix[1]
profit_total = round(choix[2], 2)

choix_fichiers = [fichier[0] for fichier in choix[0]]

print(profit_total, choix_fichiers, valeur_total)




# explication bien https://www.youtube.com/watch?v=wDsZhd1wEuk


