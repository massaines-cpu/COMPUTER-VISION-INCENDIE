#lit les images nettoyées depuis data/
import json
import os
from PIL import Image
from matplotlib import pyplot as plt, patches

data = '../data/'
plt.rcParams['figure.figsize'] = (15, 15)

liste_images = []
for f in os.listdir(data):
    if '.jpg' in f:
        liste_images.append(f)
print(liste_images)

for i in liste_images :
    fig, ax = plt.subplots(1, 1, figsize=(15, 15))
    img = Image.open(data+i)
    ax.imshow(img)


plt.show()
data = '../data/'
plt.rcParams['figure.figsize'] = (15, 15)

liste_images = []

for f in os.listdir(data):
    if '.jpg' in f:
        liste_images.append(f)

print('liste images', liste_images)

count = 0
with open ('../data/_annotations.coco.json') as f:
    coco = json.load(f)
plt.rcParams['figure.figsize'] = (15, 15)

for i in liste_images:
    image_id = None
    for img_info in coco['images']:
        if img_info['file_name'] == i:
            image_id = img_info['id']
            break

    fig, ax = plt.subplots(1, 1, figsize=(15, 15))
    img = Image.open(data + i)
    ax.imshow(img)
    ax.axis('off')

    for image_ann in coco['annotations']:
        if image_ann['image_id'] == image_id:
            x, y, w, h = image_ann['bbox']
            bb = patches.Rectangle((x, y), w, h, linewidth=3, edgecolor='red', facecolor='none')
            ax.add_patch(bb)

    count += 1
    if count % 20 == 0:
        plt.show()
plt.show()