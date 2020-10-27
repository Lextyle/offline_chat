import pygame
from pyautogui import size
from EntryField import *
from Message import *
from Button import *
pygame.init()
window_width = size()[0]
window_height = size()[1]
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
font = pygame.font.Font("SFPixelate.ttf", 50)
letter_example = font.render("Q", True, (200, 200, 200))
entry_field = EntryField(0, window_height - letter_example.get_height(), window_width, letter_example.get_height(), (30, 30, 30), font, 6)
messages = []
submit_button = Button(window_width - 40, window_height - 40, pygame.transform.scale(pygame.image.load("submit_button_image.png"), (40, 40)), pygame.transform.scale(pygame.image.load("submit_button_image.png"), (40, 40)))
while True:
	window.fill((60, 60, 60))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 4:
				if len(messages) > 0:
					for message in messages:
						message.y -= 20
			if event.button == 5:
				if len(messages) > 0:
					for message in messages:
						message.y += 20
		entry_field.update(event)
		submit_button.update(event)
	if len(messages) > 0:
		if messages[0].y > 10:
			difference = messages[0].y - 10
			for message in messages:
				message.y -= difference	
		if messages[-1].y + messages[-1].height < (window_height - letter_example.get_height()) - 10:
			difference = ((window_height - letter_example.get_height()) - 10) - (messages[-1].y + messages[-1].height)
			for message in messages:
				message.y += difference
	if submit_button.pressed:
		if not "" in entry_field.lines:
			if len(messages) != 0:
				messages.append(Message(10, messages[-1].y + messages[-1].height + 10, entry_field.lines, font))
				if messages[-1].y + messages[-1].height > window_height - letter_example.get_height():
					differance = (messages[-1].y + messages[-1].height) - (window_height - letter_example.get_height()) + 10
					for message in messages:
						message.y -= differance 
			else:
				messages.append(Message(10, (window_height - letter_example.get_height()) - 10, entry_field.lines, font))
				messages[-1].y -= messages[-1].height
			entry_field.lines = [""]
			entry_field.height = letter_example.get_height()
			entry_field.y = window_height - letter_example.get_height()
	for message in messages:
		message.draw(window)
	entry_field.draw(window)
	submit_button.draw(window)
	pygame.display.update()