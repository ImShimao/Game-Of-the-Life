import tkinter as tk
import gameoflife
import pyxel

class GameOfLife:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1920x1080')
        self.root.title('Game of the Life')

        title_label = tk.Label(self.root, text='Game of Life', font=('Arial', 60))
        title_label.pack(pady=100)

        start_button = tk.Button(self.root, text='Start', font=('Arial', 30), command=self.start_game)
        start_button.pack(pady=50)

        self.root.mainloop()

    def start_game(self):
        self.root.destroy()

        pyxel.init(800, 800, title='Game of Life', fps=15)
        game = gameoflife.GameOfLife()
        pyxel.run(game.update, game.draw)

if __name__ == '__main__':
    GameOfLife()
