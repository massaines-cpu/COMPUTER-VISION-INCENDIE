from matplotlib import pyplot as plt
import matplotlib.patches as patches
import json
import pandas as pd
from PIL import Image

#écrire une fonction qui ouvre ce JSON avec json.load()

with open ('../data/_annotations.coco.json') as f:
    coco = json.load(f)
plt.rcParams['figure.figsize'] = (15, 15)

image_id = None
image_name = '../data/cl6e3e9qm003rgk55efdu14ah_2_FALSE_COLOR_jpg.rf.8abfdde94619a88574680bdb5bafa4dc.jpg'

for image in coco['images']:
    if image['file_name'] == image_name.split('/')[-1]:
        image_id = image['id']
        break


fig, ax = plt.subplots(1, 1, figsize=(15, 15))
img = Image.open(image_name)
ax.imshow(img)

for image_ann in coco['annotations']:
    if image_ann['image_id'] == image_id:
        x, y, w, h = image_ann['bbox']
        bb = patches.Rectangle((x, y), w, h, linewidth=3, edgecolor='red', facecolor='none')
        ax.add_patch(bb)

plt.show()