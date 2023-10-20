import turtle

class GridController():
    def __init__(self, grid_ref):
        super().__init__()
        self.t = turtle.Turtle()
        self.t.ht()

        self.grid = grid_ref
        self.input_setup()

    def input_setup(self):
        self.t.screen.onkeypress(self.grid.up, 'w')
        self.t.screen.onkeypress(self.grid.down, 's')
        self.t.screen.onkeypress(self.grid.left, 'a')
        self.t.screen.onkeypress(self.grid.right, 'd')
