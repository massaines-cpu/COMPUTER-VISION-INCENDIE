import os
from prepare_data.data_loader import open_data
from prepare_data.data_split import coco_clean, train_id, val_id, test_id

# convertit les annotations au format YOLO

data2 = '../data/_annotations.coco.json'
coco = open_data(data2)

def labels_repartition(images, annotations, split_ids, dest_folder):
    for i in images:
        if i['id'] in split_ids:
            image_height = i['height']
            image_width = i['width']

            annotations_image = [a for a in annotations if a['image_id'] == i['id']]
            ligne_yolo = []
            for a in annotations_image:
                x_coco = a['bbox'][0]
                y_coco = a['bbox'][1]
                w_coco = a['bbox'][2]
                h_coco = a['bbox'][3]
                category_id = a['category_id']

                w_yolo = w_coco / image_width
                h_yolo = h_coco / image_height
                x_yolo = (x_coco + w_coco / 2) / image_width
                y_yolo = (y_coco + h_coco / 2) / image_height
                ligne_yolo.append(f"{category_id} {x_yolo} {y_yolo} {w_yolo} {h_yolo}")

            nom_fichier = i['file_name'].replace('.jpg', '.txt')
            with open(f'{dest_folder}/{nom_fichier}', 'w') as f:
                f.write('\n'.join(ligne_yolo))

labels_repartition(coco_clean['images'], coco_clean['annotations'], train_id, '../data/train/labels')
labels_repartition(coco_clean['images'], coco_clean['annotations'], test_id, '../data/test/labels')
labels_repartition(coco_clean['images'], coco_clean['annotations'], val_id, '../data/val/labels')

