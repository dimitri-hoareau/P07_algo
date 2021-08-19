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


test_array =["a","b","c","d","e"]   

# def bruteforce(charset, maxlength):
#     return (''.join(candidate)
#         for candidate in chain.from_iterable(product(charset, repeat=i)
#         for i in range(1, maxlength + 1)))

# def bruteforce(charset, maxlength):
#     for i in range(1, maxlength + 1):
#         for candidate in chain.from_iterable(product(charset, repeat=i)):
#             print(candidate)
#             return (''.join(candidate))

# list(bruteforce(test_array, 5))

















# def imbricated_iteration_function(number_of_imbrications, array):
#     iteration = 0

#     for index in range(number_of_imbrications - 1):
#         for value in array:
#             if index > number_of_imbrications:
#                 for value in array:
#                     print(value)
#             print("hey")
#             # combinaison = value + value2 + value3


#     print(value)







test_array =["a","b","c","d","e","f"]   
# test_array =[1,2,3,4,5] 
# test_array = [
#     {"action_1": 1},
#     {"action_2": 2},  
#     {"action_3": 3},  
#     {"action_4": 4},   
#     {"action_5": 5},
# ]

# test_array = {
#     "action_1": "a",
#     "action_2": "b",  
#     "action_3": "c",  
#     "action_4": "d",   
#     "action_5": "e",
# }

# test_array = OrderedDict([
#     ('action_1', '1'),
#     ('action_2', '2'),
#     ('action_3', '3'),
#     ('action_4', '4'),
#     ('action_5', '5'),
# ])

index = 0
complete_list = []

test_array1 = test_array
test_array2 = test_array
test_array3 = test_array

# for index in range(len(test_array) - 1):
#     # print(index)
#     imbricated_iteration_function(len(test_array), test_array)


# for key1, value1 in test_array1.items():
#     for key2, value2 in test_array2.items():
#         for key3, value3 in test_array3.items():
#             if value1 != value2 and value1 != value3 and value3 != value2:
#                 combinaison = value1 + value2 + value3
#                 complete_list.append(combinaison)
#                 # print(complete_list)


# while depasse pas 500
for value1 in test_array1:
    for value2 in test_array2:
        for value3 in test_array3:
            if value1 != value2 and value1 != value3 and value3 != value2:
                combinaison = value1 + value2 + value3
                complete_list.append(combinaison)

    del test_array1[index]

    index += 1



print(complete_list)







# # #on va tester toutes les combinaisons pour chacun des numéro
# # for index, element in enumerate(test_array):



# #     # on limite a 4 combinaisons
# #     if number_of_combinaison < 4:

# #         print(len(test_array))

# #         combinaison = 0

# #         for i in range(len(test_array)):


# #         # print(test_array[index])

# #         # number_of_combinaison += 1

        


# #     # array_of_combinaison.append({index : element})

# # print(array_of_combinaison)

# # transformer l'array de nombre en array de dict pour retrouver le nom de l'action et la valeur initiale qui ne doit pas dépasser 500

# # parcourir tableau, prendre premiere valeur



# # calculer bénéfice de chaque action au bout de 2 ans, ajouter une colone valeur nette + 2 ans

# #classer le tableau a partir des données de la colonne 3

# # additionner les données de la colonne 1 sans dépasser 500

# #si ça dépasse, passe au suivant jusqu'a approcher 500