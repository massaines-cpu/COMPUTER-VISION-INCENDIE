from prepare_data.data_split import train_id, train_annotations, coco_clean, test_id, val_id
import json

train_set = {
    'images': train_id,
    'annotations': train_annotations,
    'categorie': coco_clean['categories']
}
test_set = {
    'images': test_id,
    'annotations': train_annotations,
    'categorie': coco_clean['categories']
}

val_set = {
    'images': val_id,
    'annotations': train_annotations,
    'categorie': coco_clean['categories']
}

print(coco_clean['categories'])
# with open('../data/train/annotations.json', 'w') as f:
#     json.dump(train_set, f)
# with open('../data/test/annotations.json', 'w') as f:
#     json.dump(test_set, f)
# with open('../data/val/annotations.json', 'w') as f:
#     json.dump(val_set, f)