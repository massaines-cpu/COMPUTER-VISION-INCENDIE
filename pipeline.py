from data_loader import open_data



#supprimer les images sans annotations
def clean_images(coco):
    image_valides = {a['image_id'] for a in coco['annotations']}
    coco['images'] = [i for i in coco['images'] if i['id'] in image_valides]
    return coco

#supprimer les annotations orphelines
def supprimer_annotations(annotations):
    ids_images = {i['id'] for i in coco['images']}
    coco['annotations'] = [a for a in coco['annotations'] if a['image_id'] in ids_images]

