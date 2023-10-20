import turtle
import random
import copy

# random.seed(42)

class Grid():
    def __init__(self):
        super().__init__()
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.penup()
        self.t.rt(90) # to offset a text pos

        self.t.shape('assets/Cell_tile.gif')

        self.generate_positions()
        # self.curr_positions = [
        #     [4,2,4,4],
        #     [2,2,2,None],
        #     [2,2,2,2],
        #     [2,4,4,2]
        # ]

    def generate_positions(self):
        self.curr_positions = [[None for _ in range(4)] for _ in range(4)]
        
        for _ in range(4):
            self.fill_empty_cell()

    def fill_empty_cell(self):
        none_cells = [(i, j) for i in range(len(self.curr_positions)) for j in range(len(self.curr_positions[0])) if self.curr_positions[i][j] is None]
        if len(none_cells) > 0:
            random_cell = random.choice(none_cells)
            self.curr_positions[random_cell[0]][random_cell[1]] = 2
        else:
            print('game over')

    # me-eh, too complicated. Maybe later (never)
    # def transpose(self, matrix, reverse=False):
    #     if reverse:
    #         matrix = [list(reversed(col)) for col in zip(*matrix)]
    #     else:
    #         matrix = [list(col) for col in zip(*matrix)]
    #     return matrix

    def up(self):
        for j in range(len(self.curr_positions[0])):
            column = [self.curr_positions[i][j] for i in range(len(self.curr_positions))]
            self.merge_row(column)
            for i in range(len(self.curr_positions)):
                self.curr_positions[i][j] = column[i]

        self.fill_empty_cell()

    def down(self):
        for j in range(len(self.curr_positions[0])):
            column = [self.curr_positions[i][j] for i in range(len(self.curr_positions))]
            column = list(reversed(column))
            self.merge_row(column)
            column = list(reversed(column))
            for i in range(len(self.curr_positions)):
                self.curr_positions[i][j] = column[i]

        self.fill_empty_cell()

    def left(self):
        for i in range(len(self.curr_positions)):
            row = self.curr_positions[i]
            self.merge_row(row)

        self.fill_empty_cell()

    def right(self):
        for i in range(len(self.curr_positions)):
            row = list(reversed(self.curr_positions[i]))
            self.merge_row(row)
            self.curr_positions[i] = list(reversed(row))
        
        self.fill_empty_cell()

    def merge_row(self, _row):
        merged = [False] * len(_row)
        for j in range(len(_row)):
            curr_val = _row[j]
            for k in range(j + 1, len(_row)):
                neighbor = _row[k]
                if neighbor is not None:
                    if curr_val is not None and curr_val == neighbor and not merged[k]:
                        _row[k] = None
                        _row[j] = curr_val * 2
                        merged[j] = True
                    break

        for j in range(len(_row)):
            curr_val = _row[j]
            if curr_val is not None: continue 
            for k in range(j + 1, len(_row)):
                neighbor = _row[k]
                if neighbor is not None:
                    _row[j] = neighbor
                    _row[k] = None
                    break

    def render_tick(self):
        self.t.clear()
        step = 140
        offset = len(self.curr_positions)/2 * step - step/2

        for row_i in range(len(self.curr_positions)):
            for col_j in range(len(self.curr_positions[row_i])):
                self.t.setpos(step * col_j - offset, -step * row_i + offset)
                cell_text = self.curr_positions[row_i][col_j]
                if cell_text == None:
                    cell_text = ''

                self.t.stamp()
                self.t.forward(30)
                self.t.write(f'{cell_text}', align="center", font=('Arial', 40, 'bold'))
