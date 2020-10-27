from pygame import Surface
class Message():
	def __init__(self, x, y, lines, font):
		self.x = x
		self.y = y
		self.lines = lines
		self.font = font
		self.letter_example = self.font.render("f", True, (200, 200, 200))
		line_widths = []
		for line in lines:
			line_render = self.font.render(line, True, (200, 200, 200))
			line_widths.append(line_render.get_width())
		self.width = max(line_widths)
		self.height = self.letter_example.get_height() * len(self.lines)
		self.message = Surface((self.width, self.height))
		self.message.fill((30, 30, 30))
		y = 0
		for line in self.lines:
			line_render = self.font.render(line, True, (200, 200, 200))
			self.message.blit(line_render, (0, y))
			y += line_render.get_height()
	def draw(self, window):
		window.blit(self.message, (self.x, self.y))