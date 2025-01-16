from Cell import Cell
from sudoku_generator import SudokuGenerator as SG, generate_sudoku
import pygame
from constants import *

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        # The Difficulty levels
        if difficulty == "EASY":
            self.difficulty = 30
        elif difficulty == "MEDIUM":
            self.difficulty = 40
        elif difficulty == "HARD":
            self.difficulty = 50
        self.board = generate_sudoku(9, self.difficulty)
        self.original = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]




        for i in range (0,len(self.board)):
            j = 0
            for char in self.board[i]:
                self.original[i][j] = char
                j += 1

        #print(self.original)
        for i in range (0,len(self.board)):
            j = 0

            for char in self.board[i]:

                self.board[i][j] = Cell(char,i,self.board[i].index(char),self.screen)
                j += 1



        #print(self.board)
        #print(self.original)



    def reset(self):
        for i in range (0,len(self.original)):
            j = 0

            for char in self.original[i]:

                self.board[i][j].value = char
                j += 1

        for i in range (0,len(self.board)):
            for char in self.board[i]:
                char.set_sketched_value(0)
                char.draw()


    def draw(self):
        self.screen.fill((255, 255, 255))
        for i in range(1, 10):
            if i % 3 == 0:  # Creates the big lines in the horizontal direction
                pygame.draw.line(
                    self.screen,
                    color=(0, 0, 0),
                    start_pos=(0, i * 66.6667),
                    end_pos=(600, i * 66.6667),
                    width=5
                )
            else:  # Creates the smaller horizontal lines
                pygame.draw.line(
                    self.screen,
                    color=(0, 0, 0),
                    start_pos=(0, i * 66.6667),
                    end_pos=(600, i * 66.6667),
                    width=1
                )
        # Draws the vertical lines
        for i in range(1, 9):
            if i % 3 == 0:  # Creates the larger vertical lines
                pygame.draw.line(
                    self.screen,
                    color=(0, 0, 0),
                    start_pos=(i * 66.6667, 0),
                    end_pos=(i * 66.6667, 600),
                    width=5
                )
            else:  # Creates the smaller vertical lines
                pygame.draw.line(
                    self.screen,
                    color=(0, 0, 0),
                    start_pos=(i * 66.6667, 0),
                    end_pos=(i * 66.6667, 600),
                    width=1
                )
        for cell in self.board:
            for thingy in cell:
                thingy.draw()

        button_font = pygame.font.Font(None, 40)

        self.restart_text = button_font.render("Restart", 0, (255, 255, 255))

        self.restart_surface = pygame.Surface((self.restart_text.get_size()[0] + 20,self.restart_text.get_size()[1] + 20))
        self.restart_surface.fill(LINE_COLOR)
        self.restart_surface.blit(self.restart_text, (10, 10))


        self.restart_rectangle = self.restart_surface.get_rect(
            center=(WIDTH // 2, 650))

        self.reset_text = button_font.render("Reset", 0, (255, 255, 255))

        self.reset_surface = pygame.Surface((self.reset_text.get_size()[0] + 20, self.reset_text.get_size()[1] + 20))
        self.reset_surface.fill(LINE_COLOR)
        self.reset_surface.blit(self.reset_text, (10, 10))

        self.reset_rectangle = self.reset_surface.get_rect(
            center=(WIDTH // 4, 650))

        self.exit_text = button_font.render("Exit", 0, (255, 255, 255))

        self.exit_surface = pygame.Surface((self.exit_text.get_size()[0] + 20, self.exit_text.get_size()[1] + 20))
        self.exit_surface.fill(LINE_COLOR)
        self.exit_surface.blit(self.exit_text, (10, 10))

        self.exit_rectangle = self.exit_surface.get_rect(
            center=(WIDTH // (4/3), 650))

        self.screen.blit(self.restart_surface, self.restart_rectangle)
        self.screen.blit(self.reset_surface, self.reset_rectangle)
        self.screen.blit(self.exit_surface, self.exit_rectangle)

    def select(self, row, col):
        # Ok, so this one is supposed happen after the user selects the cell to modify it
        self.row, self.col = row, col
        if self.original[row][col] == 0:
            self.selected = self.board[row][col]
            self.board[row][col].draw()

    def click(self, x, y):
        # user selects a cell
        if (x, y) in ((0, 600), (0, 600)):
            row = int(x // (self.width / 9))
            col = int(x // (self.width / 9))
            return [row, col]
        return None

    def clear(self):
        # clears current cell value
        # Make sure user can only clear the cells they've made changed to
        if self.selected.can_be_cleared:
            self.selected.value = 0

    def sketch(self, value):
        try:
            if self.selected.can_be_cleared:
                self.selected.set_sketched_value(value)
        except:
            pass

    def place_number(self, value):
        # Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key
        try:
            if self.selected.can_be_cleared:
                self.selected.set_cell_value(value)
        except:
            pass


    def is_full(self):
        # checks if the board's full
        # prolly can do something like check each row to see if it's full and if one thing's open, it spits out false
        for row in range(9):
            for col in range(9):
                if self.board[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.
        for row in range(9):
            for col in range(9):
                self.board[self.row][self.col] = self.selected.value

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x, y)
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return [i, j]
        return None

    def check_board(self):
        # checks to see if the board's done correctly
        def check_duplicates(row):  # This function checks if the there's gonna be any duplicates
            row = [num.value for num in row if num.value != 0]
            return len(row) == len(set(row))

        # Checks the rows
        for row in self.board:
            if not check_duplicates(row):
                return False

        # Checks the columns
        for col in zip(*self.board):
            if not check_duplicates(col):
                return False

# Checks the boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [self.board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not check_duplicates(box):
                    return False
        return True