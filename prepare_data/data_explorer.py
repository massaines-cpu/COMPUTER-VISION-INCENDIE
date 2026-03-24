#Écrire au moins 4 fonctions d'exploration :
import os
import numpy as np
import json
from data_loader import open_data
from collections import Counter
# 1.a. Nombre total d'image

data = '../data/'

lst = [f for f in os.listdir(data) if '.jpg' in f]
number_files = len(lst)
print('nombre d\'images:', number_files)

# 1.b. Nombre total d'annotations

data2 = '../data/_annotations.coco.json'
coco = open_data(data2)

print('nombre d\'annotations:',  len(coco['annotations']))

# 2. Liste des catégories (ex : 'wildfire', 'fire').

names = [c['name'] for c in coco['categories']]

print('noms des catégories: ', names)


# 3. Nombre d'images par catégorie.


nombre_image0 = [i for i in coco['annotations'] if i['category_id'] == 0]
print('nombre d\'images dans catégorie wildfire: ', len(nombre_image0))

nombre_image1 = [i for i in coco['annotations'] if i['category_id'] == 1]
print('nombre d\'images dans catégorie fire: ', len(nombre_image1))


# 4. Statistiques sur le nombre d'annotations par image (min, max, moyenne).

count = Counter(a['image_id'] for a in coco['annotations'])
print('nombre d\'annotations par image:', count)

#moyenne
# moyenne = list(count.values()) / len(coco['annotations'])
print(list(count.values()))

annotation_par_image = list(count.values())

moyenne = np.mean(list(count.values()))
print('moyenne d\'annotations par image:', moyenne)

moyenne_ines = len(coco['annotations']) / len(count)
print(moyenne_ines)

valeur_max_annotation_par_image = np.max(annotation_par_image)
print('valeur maxime al:', valeur_max_annotation_par_image)

valeur_min_annotation_par_image = np.min(annotation_par_image)
print('valeur minimale:', valeur_min_annotation_par_image)

# print('moyenne des annotations par image:', moyenne)

# for person in people:
#     income = float(person["income"].replace("$",""))
#     salaires = salaires + income
#     salaire_moyen = salaires / len(people)