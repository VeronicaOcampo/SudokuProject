import pygame, sys
from constants import *
import Board
import os
import time

def draw_game_start(screen):
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    bg = pygame.image.load("bg.png")
    screen.fill(BG_COLOR)

    screen.blit(bg, (0, 0))

    title_surface = start_title_font.render("Sudoku", 0, (255,0,0))
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 250))
    screen.blit(title_surface, title_rectangle)

    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))
    quit_text = button_font.render("Quit", 0, (255, 255, 255))

    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))

    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 50))

    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 50))

    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2, HEIGHT //2 + 150))

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)
    screen.blit(quit_surface, quit_rectangle)
    global difficulty

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    difficulty = "EASY"
                    return

                elif medium_rectangle.collidepoint(event.pos):
                    difficulty = "MEDIUM"
                    return

                elif hard_rectangle.collidepoint(event.pos):
                    difficulty = "HARD"
                    return


                elif quit_rectangle.collidepoint(event.pos):
                    sys.exit()

        pygame.display.update()

def draw_game_over(screen):
    while True:
        game_over_font = pygame.font.Font(None, 40)
        screen.fill(BG_COLOR)

        if board.check_board():
            text = f'Player {winner} wins!'
        else:
            text = 'No one wins!'

        game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
        game_over_rect = game_over_surf.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(game_over_surf, game_over_rect)
        restart_surf = game_over_font.render(
            'Press r to play again...', 0, LINE_COLOR)
        restart_rect = restart_surf.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(restart_surf, restart_rect)

        menu_surf = game_over_font.render(
            'Press m to return to the main menu...', 0, LINE_COLOR)
        menu_rect = menu_surf.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 150))
        screen.blit(menu_surf, menu_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                global playing
                if event.key == pygame.K_m:
                    playing = True
                    return

                elif event.key == pygame.K_r:
                    playing = False
                    board.reset()
                    return

if __name__ == '__main__':
    noquit = True
    playing = True
    while True:

        game_over = False
        chip = 'x'
        winner = 0

        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Sudoku')
        if playing:
            draw_game_start(screen)

            screen.fill(BG_COLOR)

            board = Board.Board(WIDTH, HEIGHT, screen, difficulty)
        screen.fill(BG_COLOR)
        pygame.display.update()
        noquit = True




        while noquit:
            board.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    mouspos = pygame.mouse.get_pos()
                    if mouspos[1] < 600:
                        clicked_row = int(event.pos[1] / SQUARE_SIZE)
                        clicked_col = int(event.pos[0] / SQUARE_SIZE)
                        #print(clicked_row, clicked_col)
                        #print(board.board[clicked_row][clicked_col].row,board.board[clicked_row][clicked_col].col,board.board[clicked_row][clicked_col].value)
                        board.draw()
                    else:
                        if board.restart_rectangle.collidepoint(event.pos):
                            playing = True
                            noquit = False
                            board.draw()
                            break

                        elif board.reset_rectangle.collidepoint(event.pos):
                            board.reset()

                            board.draw()

                        elif board.exit_rectangle.collidepoint(event.pos):
                            sys.exit()


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        board.board[clicked_row][clicked_col].set_sketched_value(1)
                        board.board[clicked_row][clicked_col].draw()
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        board.board[clicked_row][clicked_col].set_sketched_value(2)
                        board.board[clicked_row][clicked_col].draw()
                    elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        board.board[clicked_row][clicked_col].set_sketched_value(3)
                        board.board[clicked_row][clicked_col].draw()
                    elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        board.board[clicked_row][clicked_col].set_sketched_value(4)
                        board.board[clicked_row][clicked_col].draw()
                    elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        board.board[clicked_row][clicked_col].set_sketched_value(5)
                        board.board[clicked_row][clicked_col].draw()
                    elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        board.board[clicked_row][clicked_col].set_sketched_value(6)
                        board.board[clicked_row][clicked_col].draw()
                    elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        board.board[clicked_row][clicked_col].set_sketched_value(7)
                        board.board[clicked_row][clicked_col].draw()
                    elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        board.board[clicked_row][clicked_col].set_sketched_value(8)
                        board.board[clicked_row][clicked_col].draw()
                    elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        board.board[clicked_row][clicked_col].set_sketched_value(9)
                        #print(board.board[clicked_row][clicked_col].sketched_value)
                        board.board[clicked_row][clicked_col].draw()


                    elif event.key == pygame.K_KP_ENTER:
                        board.board[clicked_row][clicked_col].set_cell_value(board.board[clicked_row][clicked_col].sketched_value)
                        board.board[clicked_row][clicked_col].draw()
                    board.draw()

                    pygame.display.update()

                if board.is_full():
                    draw_game_over(screen)
                    noquit = False
                    break


            pygame.display.update()






