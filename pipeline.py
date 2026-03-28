#Réunir dans un seul fichier toutes les étapes de nettoyage dans l'ordre
from prepare_data.data_loader import open_data
import os, shutil

data = '../data/'
data2 = '../data/_annotations.coco.json'
coco = open_data(data2)

#supprimer les images sans annotations
def clean_images(coco):
    image_valides = {a['image_id'] for a in coco['annotations']}
    coco['images'] = [i for i in coco['images'] if i['id'] in image_valides]
    return coco

#supprimer les annotations orphelines
def supprimer_annotations(annotations):
    ids_images = {i['id'] for i in coco['images']}
    coco['annotations'] = [a for a in coco['annotations'] if a['image_id'] in ids_images]

#migration des photos, copie
def copie_des_images(liste_images, ids, destination):
    for i in liste_images:
        if i['id'] in ids:
            source = os.path.join(data, i['file_name'])
            dst = os.path.join(destination, i['file_name'])
            shutil.copy(source, dst)


