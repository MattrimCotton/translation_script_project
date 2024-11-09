# Projet de Traduction de Fichiers Textes

Ce projet permet de traduire des fichiers texte entre l'anglais et le français en utilisant une interface utilisateur simple pour la sélection des fichiers. Il utilise la bibliothèque `translate` pour effectuer les traductions et permet de traiter de longs fichiers en les découpant en segments plus petits afin d'éviter les erreurs liées à la longueur.

## Structure du Projet

- `main.py` : Script principal qui gère l'interface utilisateur, l'importation et l'exportation de fichiers, et la logique de traduction.
- `file_handler.py` : Gère l'importation et l'exportation de fichiers.
- `translator.py` : Contient la logique de traduction, y compris le découpage du texte en segments et l'utilisation de la bibliothèque `translate`.

## Prérequis

1. **Installer Python 3.x** :
   - Téléchargez et installez Python depuis [python.org/downloads](https://www.python.org/downloads/).
   - Assurez-vous que Python est ajouté à votre `PATH` lors de l'installation.

2. **Installer la bibliothèque `translate`** :
   - La bibliothèque est utilisée pour effectuer les traductions. Pour l'installer, utilisez la commande suivante :
     ```bash
     pip install translate
     ```

3. **Module `tkinter`** :
   - `tkinter` est utilisé pour l'interface graphique afin de sélectionner les fichiers d'entrée et de sortie.
   - Ce module est généralement inclus avec Python par défaut. Si vous rencontrez un problème, vous pouvez consulter la documentation pour l'installation :
     - Pour Windows : `tkinter` est inclus avec l'installation de Python.
     - Pour Linux : Vous devrez peut-être installer `python3-tk` via votre gestionnaire de paquets :
       ```bash
       sudo apt-get install python3-tk
       ```

## Utilisation du Projet

### Étapes pour exécuter le projet

1. **Cloner ou télécharger le projet** :
   - Si le projet est hébergé sur GitHub, vous pouvez le cloner avec :
     ```bash
     git clone <URL_DU_PROJET>
     ```
   - Sinon, téléchargez simplement les fichiers `main.py`, `file_handler.py` et `translator.py` dans un même dossier.

2. **Lancer le script principal** :
   - Exécutez le fichier `main.py` pour démarrer le programme :
     ```bash
     python main.py
     ```
   - Vous verrez une interface graphique vous demandant de sélectionner le fichier d'entrée `.txt` à traduire.

3. **Sélectionner un fichier d'entrée** :
   - Choisissez le fichier `.txt` que vous souhaitez traduire à l'aide de la boîte de dialogue qui s'ouvre.

4. **Choisir le fichier de sortie** :
   - Une boîte de dialogue s'ouvrira pour vous permettre de spécifier où enregistrer le fichier traduit.

5. **Choisir la direction de la traduction** :
   - Le programme vous demandera de choisir la langue de destination :
     - Tapez `1` pour traduire de l'anglais vers le français.
     - Tapez `2` pour traduire du français vers l'anglais.

6. **Le fichier est traduit et sauvegardé** :
   - Le fichier traduit sera enregistré à l'emplacement que vous avez spécifié.

## Détails Techniques

### `main.py`

- Utilise `tkinter` pour permettre à l'utilisateur de sélectionner des fichiers d'entrée et de sortie via une interface graphique.
- Lit le contenu du fichier d'entrée, appelle les méthodes de traduction depuis `translator.py`, puis écrit le fichier traduit.

### `file_handler.py`

- Contient des méthodes pour lire le contenu du fichier d'entrée et écrire le contenu dans un fichier de sortie.

### `translator.py`

- Utilise la bibliothèque `translate` pour traduire le texte.
- Divise le texte en segments de 500 caractères maximum pour éviter les erreurs de longueur de requête.
- Deux méthodes principales :
  - `translate_to_french` : Traduit le texte de l'anglais vers le français.
  - `translate_to_english` : Traduit le texte du français vers l'anglais.

## Limitations

- Le projet utilise la bibliothèque `translate` qui s'appuie sur des services gratuits, ce qui peut entraîner des limitations sur les longues chaînes de texte ou sur la qualité de la traduction.
- Actuellement, seuls les fichiers `.txt` sont pris en charge.

## Personnalisation

- Vous pouvez modifier la longueur des segments dans `translator.py` en ajustant la valeur `max_length` dans la méthode `_split_text`.
- Ajoutez ou modifiez les méthodes de traduction pour utiliser d'autres langues ou services.

## Auteurs

- Ce projet a été créé pour faciliter la traduction simple et rapide de fichiers texte entre l'anglais et le français.
