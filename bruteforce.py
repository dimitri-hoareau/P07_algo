import csv

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


def imbricated_iteration_function(number_of_imbrications, array):
    iteration = 0

    for index in range(number_of_imbrications - 1):
        for value in array:
            if index > number_of_imbrications:
                for value in array:
                    print(value)
            print("hey")
            # combinaison = value + value2 + value3


    print(value)







test_array =["a","b","c","d","e"]   


complete_list = []
new_array = []
third_array = test_array
# a = [i for i in test_array]
for value in test_array:
    new_array.append(value)

for index in range(len(test_array) - 1):
    # print(index)
    imbricated_iteration_function(len(test_array), test_array)


for value in test_array:
    for value2 in test_array:
        for value3 in test_array:
            combinaison = value + value2 + value3
            complete_list.append(combinaison)

# # a = [x+i for i in test_array for x in a]

print(complete_list)


# for value in new_array:
#     for value2 in test_array:
#         for value3 in third_array:
#             combinaison = value + value2 + value3
#             complete_list.append(combinaison)

# # a = [x+i for i in test_array for x in a]

# print(complete_list)





# #on va tester toutes les combinaisons pour chacun des numéro
# for index, element in enumerate(test_array):



#     # on limite a 4 combinaisons
#     if number_of_combinaison < 4:

#         print(len(test_array))

#         combinaison = 0

#         for i in range(len(test_array)):


#         # print(test_array[index])

#         # number_of_combinaison += 1

        


#     # array_of_combinaison.append({index : element})

# print(array_of_combinaison)

# transformer l'array de nombre en array de dict pour retrouver le nom de l'action et la valeur initiale qui ne doit pas dépasser 500

# parcourir tableau, prendre premiere valeur
















# calculer bénéfice de chaque action au bout de 2 ans, ajouter une colone valeur nette + 2 ans

#classer le tableau a partir des données de la colonne 3

# additionner les données de la colonne 1 sans dépasser 500

#si ça dépasse, passe au suivant jusqu'a approcher 500