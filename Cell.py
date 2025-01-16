import pygame
from constants import *
class Cell:
	def __init__(self, value, row, col, screen):
		self.value = value
		self.row = row
		self.col = col
		self.screen = screen
		self.sketched_value = None
		self.sketched_value = self.value
		#print(self.value,self.row,self.col)

	def set_cell_value(self, value):
		# setter for cell value
		self.value = value

	def set_sketched_value(self, value):
		self.sketched_value = value

		# setter for this cell's sketched value
		# no clue what this is asking me

	def draw(self):
		squarey = (self.row  * 66.6667)
		squarex = (self.col * 66.6667)
		# Draws this cell, along with the value inside it.
		# If this cell has a nonzero value, that value is displayed
		#Otherwise, no value is displayed in the cell.
		#The cell is outlined red if it is currently selected
		if self.sketched_value != 0:
			if self.value !=0:
				font = pygame.font.Font(None, 40)
				content = str(self.value)
				text = font.render(content,0,LINE_COLOR)
				text_rect = text.get_rect(center=(squarex + 66.6667// 2, squarey + 66.6667 // 2))
				self.screen.blit(text, text_rect)
			else:
				font = pygame.font.Font(None, 40)
				content = str(self.sketched_value)
				text = font.render(content, 0, SKETCH_COLOR)
				text_rect = text.get_rect(center=(squarex + 66.6667 // 2, squarey + 66.6667 // 2))
				self.screen.blit(text, text_rect)
		if self.value != 0:
			font = pygame.font.Font(None, 40)
			content = str(self.value)
			text = font.render(content, 0, LINE_COLOR)
			text_rect = text.get_rect(center=(squarex + 66.6667 // 2, squarey + 66.6667 // 2))
			self.screen.blit(text, text_rect)

		if pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()

			square_position = (squarex,squarey)
			if (square_position[0] <= mouse_x <= square_position[0] + SQUARE_SIZE and square_position[1] <= mouse_y <= square_position[1] + SQUARE_SIZE):

				square_color = (255, 0, 0)  # Red color
				pygame.draw.rect(self.screen,(255,0,0),rect=(squarex,squarey,66.6667,66.6667),width=1)
"""	THE BOARD HASNT BEEN BUILT I DUNNO WHERE TO SET THIS		
if (square_position[0] <= mouse_x <= square_position[0] + SQUARE_SIZE and
					square_position[1] <= mouse_y <= square_position[1] + SQUARE_SIZE):
"""				# All you have to do is predict the variable location using constants smh