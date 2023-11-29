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

         # Define a color map for tile values
        color_map = {
            0: "gray",  # Adjust the color for empty cells
            2: "lightblue",
            4: "lightgreen",
            8: "lightcoral",
            16: "lightgoldenrodyellow",
            32: "lightsalmon",
            64: "lightseagreen",
            128: "lightskyblue",
            256: "lightsteelblue",
            512: "lightyellow",
            1024: "lightcyan",
            2048: "lightpink",
            # Add more colors as needed
        }

        # Draw the board
        for i in range(4):
            for j in range(4):
                tile_value = self.board[i][j]
                color = color_map.get(tile_value, "white") # Default color is white
                tk.Label(self.master, text=str(tile_value), width=5, height=2, bg=color, borderwidth=1, relief="solid").grid(row=i, column=j)

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
        for i in range(1, 4):  # Start from the second row
            for j in range(4):
                if self.board[i][j] != 0:
                    # Check if the tile can be moved up
                    k = i
                    while k > 0 and (self.board[k - 1][j] == 0 or self.board[k - 1][j] == self.board[i][j]):
                        k -= 1

                    if k != i:
                        # Move the tile up
                        if self.board[k][j] == 0:
                            self.board[k][j] = self.board[i][j]
                            self.board[i][j] = 0
                        # Merge with the tile above
                        elif self.board[k][j] == self.board[i][j]:
                            self.board[k][j] *= 2
                            self.board[i][j] = 0

        self.fill_random_empty_cell()
        self.draw_board()

    def move_down(self):
        print("Down")
        # Implement logic to move tiles down
        for i in range(0, 3):  # Start from the second bottom row
            for j in range(4):
                if self.board[i][j] != 0:
                    # Check if the tile can be moved down
                    k = i
                    while k < 3 and (self.board[k + 1][j] == 0 or self.board[k + 1][j] == self.board[i][j]):
                        k += 1

                    if k != i:
                        # Move the tile down
                        if self.board[k][j] == 0:
                            self.board[k][j] = self.board[i][j]
                            self.board[i][j] = 0
                        # Merge with the tile above
                        elif self.board[k][j] == self.board[i][j]:
                            self.board[k][j] *= 2
                            self.board[i][j] = 0

        self.fill_random_empty_cell()
        self.draw_board()

    def move_left(self):
      print("Left")
      # Implement logic to move tiles down
      for i in range(4):  # Start from the second bottom row
        for j in range(1, 4):
            if self.board[i][j] != 0:
                # Check if the tile can be moved down
                k = j
                while k > 0 and (self.board[i][k - 1] == 0 or self.board[i][k - 1] == self.board[i][j]):
                    k -= 1

                if k != i:
                    # Move the tile down
                    if self.board[i][k] == 0:
                        self.board[i][k] = self.board[i][j]
                        self.board[i][j] = 0
                    # Merge with the tile above
                    elif self.board[i][k] == self.board[i][j]:
                        self.board[i][k] *= 2
                        self.board[i][j] = 0

        self.fill_random_empty_cell()
        self.draw_board()

    def move_right(self):
      print("Left")
      # Implement logic to move tiles down
      for i in range(4):  # Start from the second bottom row
        for j in range(0, 3):
            if self.board[i][j] != 0:
                # Check if the tile can be moved down
                k = j
                while k < 3 and (self.board[i][k + 1] == 0 or self.board[i][k + 1] == self.board[i][j]):
                    k += 1

                if k != i:
                    # Move the tile down
                    if self.board[i][k] == 0:
                        self.board[i][k] = self.board[i][j]
                        self.board[i][j] = 0
                    # Merge with the tile above
                    elif self.board[i][k] == self.board[i][j]:
                        self.board[i][k] *= 2
                        self.board[i][j] = 0

        self.fill_random_empty_cell()
        self.draw_board()

if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
