from matplotlib import pyplot as plt
import supervision as sv
from pathlib import Path
import matplotlib.patches as patches
import json
import pandas as pd
from data_loader import open_data
from PIL import Image
import os
# lit les images nettoyées depuis data/


# data = '../data/'
# plt.rcParams['figure.figsize'] = (15, 15)
#
# liste_images = []
# for f in os.listdir(data):
#     if '.jpg' in f:
#         liste_images.append(f)
# print(liste_images)
#
# for i in liste_images :
#     fig, ax = plt.subplots(1, 1, figsize=(15, 15))
#     img = Image.open(data+i)
#     ax.imshow(img)
#
#
# plt.show()
data = '../data/'
plt.rcParams['figure.figsize'] = (15, 15)

liste_images = []

for f in os.listdir(data):
    if '.jpg' in f:
        liste_images.append(f)

print(liste_images)

count = 0

# for i in liste_images:
#     fig, ax = plt.subplots(1, 1, figsize=(15, 15))
#     img = Image.open(data + i)
#     ax.imshow(img)
#     ax.axis('off')
#
#     count += 1
#     if count % 20 == 0:
#         plt.show()
# # plt.show()

# convertit les annotations au format YOLO

data2 = '../data/_annotations.coco.json'
coco = open_data(data2)

os.makedirs('../data/labels', exist_ok=True)
for i in coco['images']:
    image_id = i['id']
    image_height = i['height']
    image_width = i['width']

    annotations_image = [a for a in coco['annotations']
                         if a['image_id'] == image_id]
    ligne_yolo = []
    for a in annotations_image:
        x_coco = a['bbox'][0]
        y_coco = a['bbox'][1]
        w_coco = a['bbox'][2]
        h_coco = a['bbox'][3]
        category_id = a['category_id']


        w_yolo = w_coco/ image_width
        h_yolo = h_coco/ image_height
        x_yolo = (x_coco + (w_coco/2))/image_width
        y_yolo = (y_coco + (h_coco/2))/image_height
        ligne_yolo.append(f"{category_id} {x_yolo} {y_yolo} {w_yolo} {h_yolo}")

    nom_fichier = i['file_name'].replace('.jpg', '.txt')
    with open(f'../data/labels/{nom_fichier}', 'w') as f:
        f.write('\n'.join(ligne_yolo))


# crée tout seul les dossiers train/, val/, test/ (avec les sous-dossiers images/ et labels/)
try:
    os.mkdir('../data/train')
    os.mkdir('../data/val')
    os.mkdir('../data/test')

    os.mkdir('../data/train/images')
    os.mkdir('../data/train/labels')
    os.mkdir('../data/val/images')
    os.mkdir('../data/val/labels')
    os.mkdir('../data/test/images')
    os.mkdir('../data/test/labels')
except OSError as e:
    print(os.strerror(e.errno))

# répartir et copier les fichiers dedans (70/20/10)
#70 dans train
#20 dans val
#10 dans test

liste_images_path = []
for f in os.listdir(data):
     if '.jpg' in f:
         path_img = Path(data) / f
         liste_images_path.append(path_img)
print(liste_images_path)

import shutil

