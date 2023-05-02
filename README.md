
# Game of the Life

_Jeu de la vie en python, réalisé par Shímáo, Mirvit68 & Witrold._

![Wallpaper](https://i.ytimg.com/vi/2oa0U53B278/mqdefault.jpg)

## Installation

__Windows__

Après avoir installé [Python3](https://www.python.org/) (version 3.7 ou supérieure), exécutez la commande suivante :
```bash
  pip install -U pyxel
  npm install random
```
Si vous installez Python à l'aide de l'installateur officiel, cochez la case `Add Python 3.x to PATH` pour activer la commande `pyxel`. Documentation de [Pyxel](https://github.com/kitao/pyxel#windows).


## Usage/Examples
Nous définissons ensuite les dimensions de l'écran, la taille des cellules et la taille de la grille :
```python
largeur = 800
hauteur = 800

cellules = 8

grille_largeur = largeur // cellules
grille_hauteur = hauteur // cellules

```
Nous créons ensuite la classe GameOfLife qui contiendra la logique du jeu. Le constructeur initialise la grille avec des cellules aléatoires :
```python
class GameOfLife:
    def __init__(self):
        self.grid = [[random.randint(0, 1) for x in range(grille_largeur)] for y in range(grille_hauteur)]

```

La méthode update() calcule la prochaine génération de cellules en parcourant chaque cellule et en comptant le nombre de voisins vivants. Elle utilise ensuite ces informations pour déterminer l'état de chaque cellule dans la prochaine génération :
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

La méthode get_neighbors() compte le nombre de voisins vivants d'une cellule donnée en parcourant les huit cellules adjacentes :
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

La méthode draw() dessine les cellules vivantes à l'écran en parcourant chaque cellule de la grille et en dessinant un rectangle si la cellule est vivante :
```python
    def draw(self):
        pyxel.cls(0)
        
        for y in range(grille_hauteur):
            for x in range(grille_largeur):
                if self.grid[y][x] == 1:
                    pyxel.rect(x * cellules, y * cellules, cellules, cellules, 7)
```

Nous initialisons ensuite le jeu en créant une instance de la classe GameOfLife :
```python
game = GameOfLife()
```

Nous initialisons également la fenêtre Pyxel en appelant la fonction pyxel.init() et en passant les dimensions de l'écran en pixels :
```python
pyxel.init(largeur, hauteur)
```

Nous définissons ensuite la fonction de mise à jour update() qui sera appelée chaque frame de la boucle principale Pyxel et qui mettra à jour l'état du jeu en appelant game.update() :
```python
def update():
```