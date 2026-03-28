import os
# crée tout seul les dossiers train/, val/, test/ (avec les sous-dossiers images/ et labels/)
try:
    os.mkdir('../data/train')
    os.mkdir('../data/val')
    os.mkdir('../data/test')

    os.mkdir('../data/train/images')
    os.mkdir('../data/train/labels')
    os.mkdir('../data/val/images')
    os.mkdir('../data/val/labels')
    os.mkdir('../data/test/images')
    os.mkdir('../data/test/labels')
except OSError as e:
    print(os.strerror(e.errno))