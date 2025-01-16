import math, random



class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = int(math.sqrt(row_length))
        self.board = [[0 for i in range(row_length)] for j in range(row_length)]


    def get_board(self):
        return self.board


    def print_board(self):
        print(self.board)


    def valid_in_row(self, row, num):
        falsereturned = False
        for char in self.board[row]:
            if char == num:
                return False
                falsereturned = True
        if falsereturned != True:
            return True


    def valid_in_col(self, col, num):
        falsereturned = False

        for row in self.board:
            if row[col] == num:
                return False
                falsereturned = True
        if falsereturned != True:
            return True


    def valid_in_box(self, row_start, col_start, num):
        falsereturned = False

        # Remember in python the ends of for loops are NOT inclusive
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.board[i][j] == num:
                    return False
                    falsereturned = True
        if falsereturned != True:
            return True


    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num) and self.valid_in_col(col, num):
            if row in range(0, 3):
                if col in range(0, 3):
                    if self.valid_in_box(0, 0, num):
                        return True
                elif col in range(3, 6):
                    if self.valid_in_box(0, 3, num):
                        return True
                elif col in range(6, 9):
                    if self.valid_in_box(0, 6, num):
                        return True
            elif row in range(3, 6):
                if col in range(0, 3):
                    if self.valid_in_box(3, 0, num):
                        return True
                elif col in range(3, 6):
                    if self.valid_in_box(3, 3, num):
                        return True
                elif col in range(6, 9):
                    if self.valid_in_box(3, 6, num):
                        return True
            elif row in range(6, 9):
                if col in range(0, 3):
                    if self.valid_in_box(6, 0, num):
                        return True
                elif col in range(3, 6):
                    if self.valid_in_box(6, 3, num):
                        return True
                elif col in range(6, 9):
                    if self.valid_in_box(6, 6, num):
                        return True
            else:
                return False
        else:
            return False


    def fill_box(self, row_start, col_start):
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        # Remember in python the ends of for loops are NOT inclusive
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                self.board[i][j] = numbers.pop()


    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[int(row)][int(col)] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        i = 0
        choice = list(range(0, 81))
        random.shuffle(choice)
        for thingy in choice:
            self.board[(thingy // 9)][(thingy % 9)] = 0
            i += 1
            if i >= self.removed_cells:
                break



def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    # print(board)
    return board

# Testing Function
# print(generate_sudoku(9,50))