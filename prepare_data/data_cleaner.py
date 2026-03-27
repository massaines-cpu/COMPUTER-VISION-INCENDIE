# Écrire au moins 5 fonctions
from pathlib import Path
import os
from data_loader import open_data
# Fonction 1 — Extensions des fichiers : lister les extensions présentes dans le dossier images.
data = '../data/'

path = os.listdir(data)

print(set(f.split('.')[-1] for f in path))


# Fonction 2 — Cohérence images ↔ JSON : vérifier que chaque image sur disque a bien une entrée dans
# le JSON, et inversement.


data2 = '../data/_annotations.coco.json'
coco = open_data(data2)

liste = []
for f in os.listdir(data):
    if '.jpg' in f:
        for i in coco['images']:
           if i['file_name'] == f:
               liste.append(i)

print('nombre d\'image qui ont une entrée JSON:', len(liste))

# Fonction 3 — Images sans annotations : retourner la liste des images qui n'ont aucune annotation
# associée.

liste_id_des_images = set()
for i in coco['images']:
    liste_id_des_images.add(i['id'])
print('liste id images', liste_id_des_images)

liste_id_des_images_annotation = set()

for a in coco['annotations']:
    liste_id_des_images_annotation.add(a['image_id'])
print('liste id images annotation', liste_id_des_images_annotation)

print('liste des images sans annotations :', liste_id_des_images - liste_id_des_images_annotation)

# Fonction 4 — Annotations orphelines : retourner les annotations qui pointent vers une image inexistante.

liste_id_des_images2 = []
for i in coco['images']:
    liste_id_des_images2.append(i['id'])
print('liste id image', liste_id_des_images2)


liste_id_des_images_inexistantes = []

for a in coco['annotations']:
    if a['image_id'] not in liste_id_des_images2:
        liste_id_des_images_inexistantes.append(a['image_id'])

print('liste d\'annotations qui pointent vers une image inexistante:', liste_id_des_images_inexistantes)

# print('liste des annotations qui pointent vers une image inexistante :', liste_id_des_images2 - liste_id_des_images_annotation1)



# Fonction 5 — Valeurs aberrantes : détecter les bounding boxes incohérentes (largeur=0, hauteur négative,
# etc.).
liste_bbox = []
liste_bbox_negativo = []

for a in coco['annotations']:
    x = a['bbox'][0]
    y = a['bbox'][1]
    w = a['bbox'][2]
    h = a['bbox'][3]
    liste_bbox.append([x, y, w, h])

    if x < 0 or y < 0 or w < 0 or h < 0:
        liste_bbox_negativo.append([x, y, w, h])
print(len(liste_bbox_negativo))
