# Game of the Life

_Jeu de la vie en python, réalisé par Shímáo, Mirvit68 & Witrold._

![Wallpaper](https://repository-images.githubusercontent.com/354123897/d4480700-9612-11eb-99b4-4bea6745f663)

## Installation

__Windows__

Après avoir installé [Python3](https://www.python.org/) (version 3.7 ou supérieure), exécutez la commande suivante :
```bash
  pip install -U pyxel
  npm install random
```
Si vous installez Python à l'aide de l'installateur officiel, cochez la case `Add Python 3.x to PATH` pour activer la commande `pyxel`. Documentation de [Pyxel](https://github.com/kitao/pyxel#windows).


## Usage/Exemples
__Initialisation du jeu:__

Nous commençons par définir les dimensions de l'écran, la taille des cellules et la taille de la grille :
```python
largeur = 800
hauteur = 800

cellules = 8
grille_largeur = largeur // cellules
grille_hauteur = hauteur // cellules

```
Nous créons ensuite la classe `GameOfLife` qui contiendra la logique du jeu. Le constructeur initialise la grille avec des cellules aléatoires :
```python
class GameOfLife:
    def __init__(self):
        self.grid = [[random.randint(0, 1) for x in range(grille_largeur)] for y in range(grille_hauteur)]
```
__Mise à jour du jeu:__

La méthode `update()` calcule la prochaine génération de cellules en parcourant chaque cellule et en comptant le nombre de voisins vivants. Elle utilise ensuite ces informations pour déterminer l'état de chaque cellule dans la prochaine génération :
```python
def update(self):
    new_grid = [[0 for x in range(grille_largeur)] for y in range(grille_hauteur)]
    
    for y in range(grille_hauteur):
        for x in range(grille_largeur):
            neighbors = self.get_neighbors(x, y)
            
            if self.grid[y][x] == 1 and neighbors in [2, 3]:
                new_grid[y][x] = 1
            elif self.grid[y][x] == 0 and neighbors == 3:
                new_grid[y][x] = 1
    
    self.grid = new_grid
```
La méthode `get_neighbors()` compte le nombre de voisins vivants d'une cellule donnée en parcourant les huit cellules adjacentes :
```python
def get_neighbors(self, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            row = (y + i + grille_hauteur) % grille_hauteur
            col = (x + j + grille_largeur) % grille_largeur
            count += self.grid[row][col]
    count -= self.grid[y][x]
    return count
```
__Affichage du jeu:__

La méthode `draw()` dessine les cellules vivantes à l'écran en parcourant chaque cellule de la grille et en dessinant un rectangle si la cellule est vivante :
```python
def draw(self):
    pyxel.cls(0)
    
    for y in range(grille_hauteur):
        for x in range(grille_largeur):
            if self.grid[y][x] == 1:
                pyxel.rect(x * cellules, y * cellules, cellules, cellules, 7)
```
__Boucle principale:__

Nous pouvons maintenant commencer la boucle principale Pyxel. Nous appelons la fonction pyxel.run() en passant les fonctions de mise à jour et de dessin en tant que paramètres :
```python
pyxel.run(update, draw)
```
La boucle principale Pyxel appellera la fonction update() chaque frame pour mettre à jour l'état du jeu, puis la fonction draw() pour dessiner l'état actuel du jeu à l'écran.

__Exécution:__

Pour exécuter le jeu, ouvrez un terminal et exécutez la commande suivante à la racine du projet :
```bash
python main.py
```
__Conclusion:__

Nous avons créé un jeu de la vie en utilisant Pyxel et Python. Nous avons implémenté la logique du jeu de la vie en utilisant une grille de cellules et en calculant la prochaine génération de cellules en fonction de l'état actuel de chaque cellule et du nombre de voisins vivants.

Nous avons également utilisé Pyxel pour dessiner les cellules vivantes à l'écran et pour gérer la boucle principale du jeu.

Nous espérons que vous avez apprécié ce tutoriel et que vous avez appris quelque chose de nouveau. N'hésitez pas à explorer Pyxel et à créer vos propres jeux avec Python !