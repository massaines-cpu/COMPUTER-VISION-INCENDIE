from matplotlib import pyplot as plt
import matplotlib.patches as patches
import json
import pandas as pd
from PIL import Image


#écrire une fonction qui ouvre ce JSON avec json.load()

path = '../data/_annotations.coco.json'
def open_data(path):
    with open (path) as f:
        coco = json.load(f)

    return coco

coco = open_data(path)
print(len(coco['annotations']))


#Écrire une 2e fonction qui charge images et annotations dans des DataFrames pandas

df_images = pd.DataFrame(coco['images'])
df_annotations = pd.DataFrame(coco['annotations'])

def dataframe_load(coco):
    df_images = pd.DataFrame(coco['images'])
    df_annotations = pd.DataFrame(coco['annotations'])
    return df_images, df_annotations

print(df_images, df_annotations)



