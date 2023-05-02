import pyxel
import random

largeur = 800
hauteur = 800

cellules = 8

grille_largeur = largeur // cellules
grille_hauteur = hauteur // cellules

class GameOfLife:
    def __init__(self):
        self.grid = [[random.randint(0, 1) for x in range(grille_largeur)] for y in range(grille_hauteur)]
    
    def update(self):
        new_grid = [[0 for x in range(grille_largeur)] for y in range(grille_hauteur)]
        
        # parcourir chaque cellule
        for y in range(grille_hauteur):
            for x in range(grille_largeur):
                # compter le nombre de voisins vivants
                neighbors = self.get_neighbors(x, y)
                
                # déterminer l'état de la cellule dans la prochaine génération
                if self.grid[y][x] == 1 and neighbors in [2, 3]:
                    new_grid[y][x] = 1
                elif self.grid[y][x] == 0 and neighbors == 3:
                    new_grid[y][x] = 1
        
        self.grid = new_grid
    
    def get_neighbors(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                row = (y + i + grille_hauteur) % grille_hauteur
                col = (x + j + grille_largeur) % grille_largeur
                count += self.grid[row][col]
        count -= self.grid[y][x]
        return count
    
    def draw(self):
        # effacer l'écran
        pyxel.cls(0)
        
        # dessiner chaque cellule vivante
        for y in range(grille_hauteur):
            for x in range(grille_largeur):
                if self.grid[y][x] == 1:
                    pyxel.rect(x * cellules, y * cellules, cellules, cellules, 7)
    
# initialiser le jeu
game = GameOfLife()

# initialiser la fenêtre Pyxel
pyxel.init(largeur, hauteur)

# définir la fonction de mise à jour
def update():
    game.update()

# définir la fonction de dessin
def draw():
    game.draw()

# démarrer la boucle principale
pyxel.run(update, draw)
