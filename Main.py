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
letter_example = font.render("f", True, (200, 200, 200))
entry_field = EntryField(0, window_height - letter_example.get_height(), window_width, letter_example.get_height(), (30, 30, 30), font, 6)
messages = []
submit_button = Button(window_width - 40, window_height - 40, pygame.transform.scale(pygame.image.load("submit_button_image.png"), (40, 40)), pygame.transform.scale(pygame.image.load("submit_button_image.png"), (40, 40)))
edit_buttons = []
edit_button_image = pygame.image.load("edit_button_image.png")
edit = [False, 0]
while True:
	window.fill((60, 60, 60))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 4:
				if len(messages) > 0:
					for message in messages:
						message.y += 20
					for edit_button in edit_buttons:
						edit_button.y += 20
			if event.button == 5:
				if len(messages) > 0:
					for message in messages:
						message.y -= 20
					for edit_button in edit_buttons:
						edit_button.y -= 20
		entry_field.update(event)
		submit_button.update(event)
		for edit_button in edit_buttons:
			edit_button.update(event)
			if edit_button.pressed:
				edit = [True, edit_buttons.index(edit_button)]
				for edit_button_2 in edit_buttons:
					if edit_button_2 != edit_button:
						edit_button_2.pressed = False
				entry_field.lines = messages[edit[1]].lines
				entry_field.height = len(messages[edit[1]].lines) * letter_example.get_height()
				entry_field.y = window_height - entry_field.height
				break
	if len(messages) > 0:
		if messages[0].y > 10:
			difference = messages[0].y - 10
			for message in messages:
				message.y -= difference
			for edit_button in edit_buttons:
				edit_button.y -= difference
		if messages[-1].y + messages[-1].height < (window_height - letter_example.get_height()) - 10:
			difference = ((window_height - letter_example.get_height()) - 10) - (messages[-1].y + messages[-1].height)
			for message in messages:
				message.y += difference
			for edit_button in edit_buttons:
				edit_button.y += difference
	if submit_button.pressed:
		if not "" in entry_field.lines:
			if edit[0]:
				line_widths = []
				for line in entry_field.lines:
					line_render = font.render(line, True, (200, 200, 200))
					line_widths.append(line_render.get_width())
				last_message_height = messages[edit[1]].height
				messages[edit[1]].width = max(line_widths)
				messages[edit[1]].height = letter_example.get_height() * len(entry_field.lines)
				present_message_height = messages[edit[1]].height
				messages[edit[1]].message = pygame.Surface((messages[edit[1]].width, messages[edit[1]].height))
				messages[edit[1]].message.fill((30, 30, 30))
				y = 0
				for line in entry_field.lines:
					line_render = font.render(line, True, (200, 200, 200))
					messages[edit[1]].message.blit(line_render, (0, y))
					y += line_render.get_height()
				for message in messages:
					message.y -= present_message_height - last_message_height
					if messages.index(message) == edit[1]:
						break
				for edit_button in edit_buttons:
					edit_button.y -= present_message_height - last_message_height
					if edit_buttons.index(edit_button) == edit[1]:
						break
				edit_buttons[edit[1]].x = messages[edit[1]].x + messages[edit[1]].width + 5
				edit_buttons[edit[1]].y = (messages[edit[1]].y + messages[edit[1]].height // 2) - edit_button_image.get_height() // 2
				edit = [False, 0]
			else:
				if len(messages) != 0:
					messages.append(Message(10, messages[-1].y + messages[-1].height + 10, entry_field.lines, font))
					if messages[-1].y + messages[-1].height > window_height - letter_example.get_height():
						difference = ((messages[-1].y + messages[-1].height) - (window_height - letter_example.get_height())) + 10
						for message in messages:
							message.y -= difference 
						for edit_button in edit_buttons:
							edit_button.y -= difference
				else:
					messages.append(Message(10, (window_height - letter_example.get_height()) - 10, entry_field.lines, font))
					messages[-1].y -= messages[-1].height
				edit_buttons.append(Button(messages[-1].x + messages[-1].width + 5, (messages[-1].y + messages[-1].height // 2) - edit_button_image.get_height() // 2, edit_button_image, edit_button_image))
			entry_field.lines = [""]
			entry_field.height = letter_example.get_height()
			entry_field.y = window_height - letter_example.get_height()
	for message in messages:
		message.draw(window)
	for edit_button in edit_buttons:
		edit_button.draw(window)
	entry_field.draw(window)
	submit_button.draw(window)
	pygame.display.update()