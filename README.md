# FilmRecommenderSystem
Plateforme de recommandation de films personnalisée utilisant le machine learning. Acquérir, stocker et analyser les données pour offrir des suggestions de films basées sur les préférences des utilisateurs. Déployé avec une interface utilisateur conviviale pour une expérience de recommandation immersive.



## Commencer

Pour exécuter cette application en local, suivez les étapes ci-dessous :

### Prérequis

#### Create Conda environment

##### run below commands in terminal but make sure conda is installed or use anaconda prompt which you will get as part of anaconda installation

1. `conda create -n envname python=3.9 ipykernel`
it will create a conda env named envname and install python version 3.9 and a ipykernel inside this environment

2. Activate the environment
`conda activate envname`

3. add newly created environment to the notebook as kernel
`python -m ipykernel install --user --name=envname`

4. install notebook inside the environment
`pip install notebook`

#### ## Installation

2. Installer les dépendances requises : `pip install -r requirements.txt`

* `pip install pandas`
* `pip install numpy`
* `pip install scikit-learn`
* `pip install imblearn`
* `pip install matplotlib`
* `pip install mlflow`

## Utilisation

1. Exécuter le notebook Jupyter `notebook.ipynb` pour suivre le processus de développement du modèle.
2. Pour déployer le modèle en production, suivre les instructions dans `deployement.md`.


## Contributeurs

- Alimou DIALLO (@santoudllo): Data engineer


## Licence

Ce projet est sous licence MIT. N'hésitez pas à utiliser et modifier le code pour vos propres projets.