from pygame import MOUSEBUTTONDOWN, MOUSEMOTION
class Button():
	def __init__(self, x, y, not_hover_image, hover_image):
		self.not_hover_image = not_hover_image
		self.hover_image = hover_image
		self.image = self.not_hover_image
		self.x = x
		self.y = y
		self.pressed = False
	def update(self, event):
		if event.type == MOUSEMOTION:
			if event.pos[0] in range(self.x, self.x + self.image.get_width()) and event.pos[1] in range(self.y, self.y + self.image.get_height()):
				self.image = self.hover_image
			else:
				self.image = self.not_hover_image
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				if event.pos[0] in range(self.x, self.x + self.image.get_width()) and event.pos[1] in range(self.y, self.y + self.image.get_height()):
					self.pressed = True
	def draw(self, window):
		self.pressed = False
		window.blit(self.image, (self.x, self.y))