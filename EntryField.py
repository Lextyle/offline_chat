from pygame.font import Font
from pygame.draw import rect as draw_rect
from pygame.draw import line as draw_line
from pygame import KEYDOWN
from pygame import K_BACKSPACE, K_RETURN
from time import time
class EntryField():
	def __init__(self, x, y, width, height, color, font, max_lines):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.font = font
		self.letter_example = self.font.render("Q", True, (200, 200, 200))
		self.lines = [""]
		self.max_lines = max_lines
		self.time_1 = int(time())
		self.time_2 = int(time())
	def update(self, event):
		if event.type == KEYDOWN:
			if event.key == K_BACKSPACE:
				if self.lines[-1] == "":
					if len(self.lines) != 1:
						self.lines = self.lines[0:-1]
						self.height -= self.letter_example.get_height()
						self.y += self.letter_example.get_height()
				else:
					self.lines[-1] = self.lines[-1][0:-1]
			elif event.key != K_RETURN:
				self.lines[-1] += event.unicode
				line_render = self.font.render(self.lines[-1], True, (200, 200, 200))
				if line_render.get_width() > self.width:
					if len(self.lines) < self.max_lines:
						self.lines[-1] = self.lines[-1][0:-1]
						self.lines.append(event.unicode)
						self.height += self.letter_example.get_height()
						self.y -= self.letter_example.get_height()
					else:
						self.lines[-1] = self.lines[-1][0:-1]
			else:
				if len(self.lines) < self.max_lines:
					self.lines.append("")
					self.height += self.letter_example.get_height()
					self.y -= self.letter_example.get_height()
			self.time_1 = int(time())
	def draw(self, window):
		self.time_2 = int(time())
		draw_rect(window, self.color, (self.x, self.y, self.width, self.height))
		y = self.y
		for line in self.lines:
			line_render = self.font.render(line, True, (200, 200, 200))
			window.blit(line_render, (self.x, y + (self.letter_example.get_height() - line_render.get_height())))
			y += self.letter_example.get_height()
		self.draw_line = self.time_2 - self.time_1 in range(1)
		if self.draw_line:
			draw_line(window, (255, 255, 255), (self.x + line_render.get_width(), y - self.letter_example.get_height() + 3), (self.x + line_render.get_width(), (y - self.letter_example.get_height() + 3) + 35), 2)
		else:
			if not self.time_2 - self.time_1 in range(1, 2):
				self.time_1 = int(time())