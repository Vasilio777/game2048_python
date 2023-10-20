from Grid import Grid
from GridController import GridController
from GameMode import GameMode
import turtle

t = turtle.Turtle()
t.ht()
t.screen.addshape('assets/Cell_tile.gif')

game_mode = GameMode()
grid = Grid()

GridController = GridController(grid)
game_mode.init_game(grid)
