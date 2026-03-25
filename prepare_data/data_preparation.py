from matplotlib import pyplot as plt
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
liste_w_yolo = []
liste_h_yolo = []
liste_x_yolo = []
liste_y_yolo = []
for i in coco['images']:
    image_height = i['height']
    image_width = i['width']
    for a in coco['annotations']:
        x_coco = a['bbox'][0]
        y_coco = a['bbox'][1]
        w_coco = a['bbox'][2]
        h_coco = a['bbox'][3]

        w_yolo = w_coco/ image_width
        h_yolo = h_coco/ image_height
        x_yolo = (x_coco + (w_coco/2))/image_width
        y_yolo = (y_coco + (h_coco/2))/image_height
        liste_w_yolo.append(w_yolo)
        liste_h_yolo.append(h_yolo)
        liste_x_yolo.append(x_yolo)
        liste_y_yolo.append(y_yolo)




print('liste w yolo:', liste_w_yolo)
print('-----' * 40)
print('liste h yolo:', liste_h_yolo)
print('-----' * 40)
print('liste x yolo:', liste_x_yolo)
print('liste y yolo:', liste_y_yolo)



# crée tout seul les dossiers train/, val/, test/ (avec les sous-dossiers images/ et labels/)
try:
    os.mkdir('../data/train')
    os.mkdir('../data/val')
    os.mkdir('../data/test')

    os.mkdir('../data/train/images')
    os.mkdir('../data/train/label')
    os.mkdir('../data/val/images')
    os.mkdir('../data/val/label')
    os.mkdir('../data/test/images')
    os.mkdir('../data/test/label')
except OSError as e:
    print(os.strerror(e.errno))


# répartit et copie les fichiers dedans (70/20/10)
