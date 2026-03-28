from pathlib import Path
import os
import shutil
from sklearn.model_selection import train_test_split

from pipeline import clean_images
from prepare_data.data_loader import open_data

data2 = '../data/_annotations.coco.json'
coco = open_data(data2)

coco_clean = clean_images(coco)

# le bon truc a split
print(len(coco_clean['images']))

id_des_images = [i['id'] for i in coco_clean['images']]

train_id, temporaire_id = train_test_split(id_des_images, test_size=0.30, random_state=0)
print(len(train_id))
val_id, test_id = train_test_split(temporaire_id, test_size=0.67, random_state=0)
print(len(test_id))
print(len(val_id))

train_annotations = [a for a in coco_clean['annotations'] if a['image_id'] in train_id]
print('nb annotations dans train:', len(train_annotations))
test_annotations = [a for a in coco_clean['annotations'] if a['image_id'] in test_id]
print('nb annotations dans test:', len(test_annotations))
val_annotations = [a for a in coco_clean['annotations'] if a['image_id'] in val_id]
print('nb annotations dans val:', len(val_annotations))


data = '../data/'
def copie_des_images(images, split_ids, destination):
    for i in images:
        if i['id'] in split_ids:
            source = os.path.join(data, i['file_name'])
            dst = os.path.join(destination, i['file_name'])
            shutil.copy(source, dst)

copie_des_images(coco_clean['images'], train_id, '../data/train/images')
copie_des_images(coco_clean['images'], val_id, '../data/val/images')
copie_des_images(coco_clean['images'], test_id, '../data/test/images')