# Générateur de Grilles de Sudoku

![Exemple de Grille](./samples/sample_puzzle.png)

Ceci est un **Générateur de Grilles de Sudoku** écrit en Python, supportant la génération de grilles de Sudoku de différents niveaux de difficulté (`facile`, `moyen`, `difficile`). Le générateur permet de personnaliser le nombre d'indices, d'utiliser une symétrie optionnelle, et de créer des grilles de Sudoku de qualité professionnelle. Il peut également générer des PDFs des grilles et de leurs solutions. Le générateur utilise le **multiprocessing** pour exploiter tous les cœurs CPU disponibles, rendant le processus de génération plus rapide.

## Fonctionnalités

- **Difficulté Personnalisable** : Générez des grilles avec des niveaux de difficulté `facile`, `moyen` ou `difficile`.
- **Nombre d'Indices Personnalisé** : Spécifiez le nombre d'indices pour chaque grille (par exemple, `difficile:1:17` génère une grille difficile avec exactement 17 indices).
- **Symétrie Optionnelle** : Utilisez le drapeau `--use-symmetry` pour générer des grilles avec un placement symétrique des indices pour un aspect professionnel.
- **Génération de Solutions** : Générez un PDF séparé avec les solutions des grilles.
- **Génération Parallèle de Grilles** : Utilise le multiprocessing pour générer des grilles en parallèle, exploitant tous les cœurs CPU disponibles pour une génération plus rapide.
- **Sortie PDF** : Produit les grilles générées et les solutions sous forme de PDFs.

## Installation

Pour utiliser ce projet, assurez-vous d'avoir Python 3.x installé ainsi que les dépendances nécessaires :

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/alicommit-malp/sudoku
   cd sudoku
   ```

2. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

### Dépendances

- `numpy` : Utilisé pour gérer la grille de Sudoku.
- `fpdf` : Pour générer les PDFs des grilles et des solutions.
- `argparse` : Pour analyser les arguments de ligne de commande.
- `multiprocessing` : Pour paralléliser la génération de grilles.

## Utilisation

Vous pouvez exécuter le générateur de Sudoku depuis la ligne de commande en utilisant la commande `python`. Voici des exemples de différentes façons d'exécuter le générateur.

### Exemple Basique

Générez **10 grilles faciles** avec **40 indices** et **5 grilles moyennes** avec **35 indices**, sans symétrie :

```bash
python sudoku.py -config facile:10:40 -config moyen:5:35 -output sudoku_puzzles.pdf
```

### Génération de Grilles Difficiles avec Exactement 17 Indices

Générez **5 grilles difficiles** avec **exactement 17 indices**, en utilisant la symétrie et la vérification de difficulté avancée, ainsi que les solutions :

```bash
python sudoku.py -config difficile:5:17 -output sudoku_puzzles.pdf --use-symmetry --gen-answers
```

### Arguments de Ligne de Commande

- `-config` : Spécifiez le niveau de difficulté et le nombre de grilles à générer au format `difficulté:nombre:indices`. Vous pouvez fournir plusieurs configurations.
  - Exemple : `-config facile:10:40` génère 10 grilles faciles avec 40 indices chacune.
  - Vous pouvez également omettre le nombre d'indices, et une valeur par défaut sera utilisée en fonction de la difficulté.

- `-output` : Spécifiez le nom du fichier PDF de sortie (par exemple, `sudoku_puzzles.pdf`).

- `--gen-answers` : Si ce drapeau est fourni, un deuxième PDF avec les solutions sera généré.

- `--use-symmetry` : Si ce drapeau est fourni, les grilles seront générées avec un placement symétrique des indices pour un aspect professionnel.

### Nombres d'Indices par Défaut

Si vous ne fournissez pas un nombre d'indices pour une grille, les valeurs par défaut suivantes seront utilisées en fonction de la difficulté :

- `facile` : 40 indices
- `moyen` : 35 indices
- `difficile` : 30 indices

## Exemples

### Générer 5 Grilles Difficiles avec 17 Indices Chacune :

```bash
python sudoku.py -config difficile:5:17 -output hard_puzzles.pdf --gen-answers
```

Cela générera 5 grilles difficiles avec exactement 17 indices chacune, et les solutions seront sauvegardées dans `hard_puzzles_answers.pdf`.

### Générer des Grilles de Difficultés Mixtes :

```bash
python sudoku.py -config facile:10:40 -config moyen:5:35 -config difficile:3:30 -output mixed_puzzles.pdf
```

Cela générera :

- 10 grilles faciles avec 40 indices chacune.
- 5 grilles moyennes avec 35 indices chacune.
- 3 grilles difficiles avec 30 indices chacune.

### Activer la Symétrie :

Pour activer le placement symétrique des indices dans les grilles, utilisez le drapeau `--use-symmetry` :

```bash
python sudoku.py -config difficile:5:17 -output symmetrical_hard_puzzles.pdf --use-symmetry
```

### Générer des Grilles en Parallèle :

Le générateur détecte automatiquement le nombre de cœurs CPU disponibles et parallélise le processus de génération de grilles. Aucun drapeau supplémentaire n'est nécessaire pour le multiprocessing.

## Contribution

N'hésitez pas à forker ce dépôt et à soumettre des pull requests pour des améliorations ou des corrections de bugs. Si vous avez des problèmes ou des demandes de fonctionnalités, veuillez ouvrir une issue.

## Licence

Ce projet est sous licence MIT.
