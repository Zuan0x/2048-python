import random
import tkinter as tk

class Game2048:
    def __init__(self, master):
        self.master = master
        self.master.title("2048 Game")
        self.master.geometry("400x400")

        self.board = [[0] * 4 for _ in range(4)]

        # Initialize the starting tiles
        self.start_x1, self.start_y1 = self.generate_random_empty_cell()
        self.start_x2, self.start_y2 = self.generate_random_empty_cell()

        # Place the starting tiles on the board
        self.board[self.start_x1][self.start_y1] = 2
        self.board[self.start_x2][self.start_y2] = 2

        self.draw_board()

        # Bind arrow keys to the corresponding functions
        self.master.bind("<Up>", lambda event:self.move_up())
        self.master.bind("<Down>", lambda event:self.move_down())
        self.master.bind("<Left>", lambda event:self.move_left())
        self.master.bind("<Right>", lambda event:self.move_right())

    def draw_board(self):
        # Clear the previous labels
        for widget in self.master.winfo_children():
            widget.destroy()

        # Draw the board
        for i in range(4):
            for j in range(4):
                tile_value = self.board[i][j]
                tk.Label(self.master, text=str(tile_value), width=5, height=2, borderwidth=1, relief="solid").grid(row=i, column=j)

    def generate_random_empty_cell(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        return random.choice(empty_cells)
    
    def fill_random_empty_cell(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if empty_cells:
            random_cell = random.choice(empty_cells)
            self.board[random_cell[0]][random_cell[1]] = 2

    def move_up(self):
        print("Up")
        # Implement logic to move tiles up
        for i in range(4):
            for j in range(4):
                if self.board[i][j] != 0:
                    # Check if the tile can be moved up
                    if i - 1 >= 0 and self.board[i - 1][j] == 0:
                        self.board[i - 1][j] = self.board[i][j]
                        self.board[i][j] = 0
                    # Check if the tile can be merged with the tile above
                    elif i - 1 >= 0 and self.board[i - 1][j] == self.board[i][j]:
                        self.board[i - 1][j] *= 2
                        self.board[i][j] = 0
        self.fill_random_empty_cell()
        self.draw_board()

    def move_down(self):
        print("Down")
        # Implement logic to move tiles down
        for i in range(3, -1, -1):
            for j in range(4):
                if self.board[i][j] != 0:
                    # Check if the tile can be moved down
                    if i + 1 <= 3 and self.board[i + 1][j] == 0:
                        self.board[i + 1][j] = self.board[i][j]
                        self.board[i][j] = 0
                    # Check if the tile can be merged with the tile below
                    elif i + 1 <= 3 and self.board[i + 1][j] == self.board[i][j]:
                        self.board[i + 1][j] *= 2
                        self.board[i][j] = 0
        self.fill_random_empty_cell()
        self.draw_board()

    def move_left(self):
        print("Left")
        # Implement logic to move tiles left
        for i in range(4):
            for j in range(4):
                if self.board[i][j] != 0:
                    # Check if the tile can be moved left
                    if j - 1 >= 0 and self.board[i][j - 1] == 0:
                        self.board[i][j - 1] = self.board[i][j]
                        self.board[i][j] = 0
                    # Check if the tile can be merged with the tile on the left
                    elif j - 1 >= 0 and self.board[i][j - 1] == self.board[i][j]:
                        self.board[i][j - 1] *= 2
                        self.board[i][j] = 0
        self.fill_random_empty_cell()
        self.draw_board()

    def move_right(self):
        print("Right")
        # Implement logic to move tiles right
        for i in range(4):
            for j in range(3, -1, -1):
                if self.board[i][j] != 0:
                    # Check if the tile can be moved right
                    if j + 1 <= 3 and self.board[i][j + 1] == 0:
                        self.board[i][j + 1] = self.board[i][j]
                        self.board[i][j] = 0
                    # Check if the tile can be merged with the tile on the right
                    elif j + 1 <= 3 and self.board[i][j + 1] == self.board[i][j]:
                        self.board[i][j + 1] *= 2
                        self.board[i][j] = 0
        self.fill_random_empty_cell()
        self.draw_board()

if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
