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

videos = [('Video 1', 114, 4.57), ('Video 2', 32, 0.630),
('Video 3', 20, 1.65), ('Video 4', 4, 0.085),
('Video 5', 18, 2.15), ('Video 6', 80, 2.71),
('Video 7', 5, 0.320)]

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

def ens_des_parties(ensemble):
    """ ensemble est une liste de p-uplets """
    nb = len(ensemble) # nombre d'éléments
    n = 2 ** nb # nombre de parties
    parties = [] # l'ensemble des parties

    for i in range(1, n):
        ch = int_to_bin(i, nb) # écriture de i sur nb bits
        partie = [] # construction d'une partie
        for j in range(len(ch)):
            if ch[j] == "1":
                partie.append(ensemble[j])
        parties.append(partie) # la partie construite est ajoutée à la liste
    return parties

def duree_totale(liste):
    d = 0
    for triplet in liste:
        d += triplet[1]
    return d

def taille_totale(liste):
    t = 0
    for triplet in liste:
        t += triplet[2]
    return t

def recherche(ens_parties, contrainte):
    duree_max = 0
    solution = []
    for partie in ens_parties: # un choix possible de fichiers
        duree = duree_totale(partie)
        taille = taille_totale(partie)
        if taille <= contrainte and duree > duree_max:
            duree_max = duree
            solution = partie
    return solution, duree_max

def force_brute(fichiers, taille_max):
    parties = ens_des_parties(fichiers)
    return recherche(parties, taille_max)
    
choix = force_brute(videos, 5)
duree_totale = choix[1]
choix_fichiers = [fichier[0] for fichier in choix[0]]
print(choix_fichiers, duree_totale)

