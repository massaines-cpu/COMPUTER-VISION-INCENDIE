from data_loader import open_data

data = '../data/_annotations.coco.json'
coco = open_data(data)

#supprimer les images sans annotations
def supprimer_images(images):
    id_valid = {a['image_id'] for a in coco['annotations']}
    coco['images'] = [i for i in coco['images'] if i['id'] in id_valid]

#supprimer les annotations orphelines
def supprimer_annotations(annotations):
    ids_images = {i['id'] for i in coco['images']}
    coco['annotations'] = [a for a in coco['annotations'] if a['image_id'] in ids_images]