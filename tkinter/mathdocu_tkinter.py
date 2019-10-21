import tkinter as tk

from mathdocu.model.game import Game
from mathdocu.model.grid import NEIGHBOR_TOP, NEIGHBOR_RIGHT, NEIGHBOR_BOTTOM, NEIGHBOR_LEFT

class App(tk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack()

        # create a toolbar
        toolbar = tk.Frame(root)

        b = tk.Button(toolbar, text="toggle coordinates", command=self.toggle_coordinates)
        b.pack(side=tk.LEFT, padx=2, pady=2)

        b = tk.Button(toolbar, text="solve", command=None)
        b.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.board = Board(self)
        self.board.pack()

    def toggle_coordinates(self):
        self.board.toggle_coordinates()


class Board(tk.Frame):

    def __init__(self, master, width=500, height=500):
        super().__init__(master, width=500, height=500)
        self.pack()

        self.pane1 = BoardGrid(self)

    def toggle_coordinates(self):
        self.pane1.toggle_coordinates()


class BoardGrid(tk.Canvas):

    CELL_HEIGHT = 70
    CELL_WIDTH = 70

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.pack()

        self.configure(highlightbackground="blue",
                       highlightcolor="blue",
                       highlightthickness=1,
                       width=500,
                       height=500,
                       bd=0)

        self.grid_lines = set()
        self.cell_coordinates = set()
        self.display_grid(6)

    def display_grid(self, grid_size = 7):
        self.delete(tk.ALL)
        self.display_grid_lines(self, grid_size)
        self.display_grid_coordinates(self, grid_size)


    def display_grid_coordinates(self, canvas, grid_size = 7, cell_width = CELL_WIDTH, cell_height = CELL_HEIGHT, with_coordinates=True):
        offset_x = 4
        offset_y = 4

        if with_coordinates:
            for r in range(grid_size):
                for c in range(grid_size):
                    id = canvas.create_text((c + 1) * cell_width - offset_x,
                                            r * cell_height + offset_y,
                                            anchor=tk.NE,
                                            text='abcdefghi'[r] + '123456789'[c],
                                            font=('Arial', 12),
                                            fill='gray')
                    self.cell_coordinates.add(id)


    def display_grid_lines(self, canvas, grid_size=7, cell_width = CELL_WIDTH, cell_height = CELL_HEIGHT, with_coordinates=True):
        outline_color = 'gray'
        for r in range(grid_size):
            for c in range(grid_size):
                rect = (c * cell_width,
                        r * cell_height,
                        (c + 1) * cell_width,
                        (r + 1) * cell_height)
                id = canvas.create_rectangle(rect,
                                             outline=outline_color)
                self.grid_lines.add(id)

    def display_constraints(self, w, grid, constraints):

        grid_size = grid.grid_size
        size = self.grid_width // grid_size - 1
        offset_x = 2
        offset_y = 2
        outline_color = 'black'
        line_width = 3

        for constraint in constraints:

            r, c = tuple(constraint.cell_coordinates[0])
            x = grid.column_indeces.index(c)
            y = grid.row_indeces.index(r)
            label = tk.Label(w,
                             text = str(constraint.result) + constraint.operator,
                             font = ('Arial', 14),
                             bg = 'White',
                             fg = 'Black')
            label.place(x = offset_x + x * size + 2,
                        y = offset_x + y * size + 2)

            for coordinate in constraint.cell_coordinates:
                r, c = tuple(coordinate)

                border_top = r == grid.row_indeces[0] or \
                             grid.get_neighbor_coordinate(coordinate, NEIGHBOR_TOP) \
                             not in constraint.cell_coordinates
                border_right = c == grid.column_indeces[-1] or \
                               grid.get_neighbor_coordinate(coordinate, NEIGHBOR_RIGHT) \
                               not in constraint.cell_coordinates
                border_bottom = r == grid.row_indeces[-1] or \
                                grid.get_neighbor_coordinate(coordinate, NEIGHBOR_BOTTOM) \
                                not in constraint.cell_coordinates
                border_left = c == grid.column_indeces[0] or \
                              grid.get_neighbor_coordinate(coordinate, NEIGHBOR_LEFT) \
                              not in constraint.cell_coordinates

                x = grid.column_indeces.index(c)
                y = grid.row_indeces.index(r)
                if border_top:
                    line = (offset_x + x * size,
                            offset_y + y * size,
                            offset_x + (x + 1) * size,
                            offset_y + y * size)
                    w.create_line(line, capstyle=tk.ROUND, fill=outline_color, width=line_width)
                if border_right:
                    line = (offset_x + (x + 1) * size,
                            offset_y + y * size,
                            offset_x + (x + 1) * size,
                            offset_y + (y + 1) * size)
                    w.create_line(line, capstyle=tk.ROUND, fill=outline_color, width=line_width)
                if border_bottom:
                    line = (offset_x + x * size,
                            offset_y + (y + 1) * size,
                            offset_x + (x + 1) * size,
                            offset_y + (y + 1) * size)
                    w.create_line(line, capstyle=tk.ROUND, fill=outline_color, width=line_width)
                if border_left:
                    line = (offset_x + x * size,
                            offset_y + y * size,
                            offset_x + x * size,
                            offset_y + (y + 1) * size)
                    w.create_line(line, capstyle=tk.ROUND , fill=outline_color, width=line_width)
        w.pack()

    def toggle_coordinates(self):
        current_state = self.itemcget(list(self.cell_coordinates)[0],'state')
        for id in self.cell_coordinates:
            self.itemconfigure(id, state='hidden' if current_state in ('','normal') else 'normal')


if __name__ == '__main__':

    root = tk.Tk()
    root.title('mathdocu tkinter demo')
    root.geometry("600x600")

    app = App(root)

    root.mainloop()