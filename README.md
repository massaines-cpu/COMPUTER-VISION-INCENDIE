# Choisir le modèle (questions de réflexion)

• Quel type de modèle répond à la détection d'objets ? (YOLO, Faster R-CNN, SSD…)




• Qu'est-ce qu'un modèle pré-entraîné ? Pourquoi l'utiliser ici ?





• CPU vs GPU : quelle différence pour l'entraînement ? Quel est l'équipement dispo ?




• Modèle recommandé : YOLO (ultralytics), version nano ou small pour aller vite.





• Si le dataset est trop petit → data augmentation (rotation, zoom, flou…).




# Définir les métriques d'évaluation

• Recall (rappel) : parmi toutes les zones brûlées réelles, combien le modèle en détecte ?





• Precision : parmi toutes les détections du modèle, combien sont correctes ?






• IoU (Intersection over Union) : à quel point la boîte prédite chevauche la vraie boîte ?






• mAP (mean Average Precision) : métrique principale, combine precision et recall sur toutes les classes.





• Pour les pompiers → prioriser le Recall : mieux vaut une fausse alarme que rater un incendie.