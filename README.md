
## <center>Analyse des sentiments et des émotions sur les tweets</center>

<p align="center">
  <img src="image.png" alt="tweet image" width="300"/>
</p>

## Description du projet

## Contexte

Les réseaux sociaux, et en particulier Twitter, sont des plateformes essentielles où les utilisateurs expriment leurs sentiments et émotions au quotidien. Analyser les tweets peut fournir des informations précieuses sur l’humeur collective et les préoccupations des gens. Ce projet utilise un dataset de tweets disponible sur Kaggle pour explorer les relations entre les sentiments exprimés dans les tweets et les émotions des utilisateurs.

## Dataset

Le dataset utilisé pour ce projet est disponible sur Kaggle :
- **[Tweet Sentiment and Emotion Analysis](https://www.kaggle.com/datasets/subhajournal/tweet-sentiment-and-emotion-analysis)**

## Objectif

Le projet a pour but de développer un modèle de machine learning capable de :

1. **Classifier les Sentiments** : Déterminer si un tweet exprime un sentiment **négatif**, **neutre** ou **positif**.
2. **Identifier les Émotions** : Catégoriser les émotions des utilisateurs en **heureux**, **anxieux**, **stressé** ou **déprimé**.

## Méthodologie

Le projet est structuré autour des étapes suivantes :

1. **Préparation des Données** :
   - Chargement et manipulation des données en utilisant **pandas** et **numpy**.
   - Nettoyage des données et prétraitement du texte pour une analyse efficace.

2. **Analyse des Textes** :
   - Nettoyage et normalisation des textes avec **neattext**.
   - Transformation du texte en vecteurs numériques avec **CountVectorizer** et **TFIDFTransformer**.

3. **Modélisation** :
   - Entraînement et évaluation de plusieurs modèles de classification avec **GridSearchCV** pour l'optimisation des hyperparamètres.

4. **Évaluation des Modèles** :
   - Comparaison des performances des modèles en utilisant des métriques telles que la précision, le rappel, et la F-mesure.

5. **Visualisation des Données** :
   - Création de graphiques avec **Seaborn**, **Matplotlib**, et **WordCloud**.

6. **Développement de l'Application** :
   - Développement d'une application web interactive avec **Streamlit**.

## Librairies Utilisées

- **pandas**, **numpy**
- **neattext**
- **CountVectorizer**, **TFIDFTransformer**
- **RandomForestClassifier**, **SVC**, **MultinomialNB**, **LogisticRegression**, **KNeighborsClassifier**
- **GridSearchCV**
- **Seaborn**, **Matplotlib**
- **WordCloud**
- **Streamlit**

## Conclusion

En utilisant des techniques avancées de traitement du langage naturel et des algorithmes de machine learning, ce projet vise à fournir des outils puissants pour analyser les sentiments et émotions des tweets. L'application développée permettra une exploration interactive des résultats, facilitant ainsi l'interprétation des données textuelles et la compréhension des sentiments et émotions exprimés sur Twitter.


### Comment utiliser l'Application :

1. Cloner ce dépôt sur votre machine locale.
2. Installer les dépendances en utilisant `pip install -r requirements.txt`.
3. Entraîner le modèle en exécutant le script `train_model.py`.
4. Déployer l'application en exécutant `python app.py`.
5. Accéder à l'application via votre navigateur web à l'adresse http://localhost:5000.





[Lien du projet sur Github](https://www.github.com/HMourad2023) 