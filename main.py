import random

import pygame

from defs import window_size, compare
from game import game
from get_all_five_letter_words import get_random_word

pygame.init()


# Extract the list of 5-letter words from the response
past_answers = [[], [], [], [], [], [], []]

actual_word = get_random_word()
# Set the window size

font = pygame.font.Font(None, 36)
# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption('Main Menu')

screen_main_menu = 0
screen_game = 1
win_screen = 2
lose_screen = 3
current_screen = screen_main_menu
# Run the game loop
running = True
input_text = ''
attempt = 0
word = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif (pygame.K_a <= event.key <= pygame.K_z) & (len(word) < 5):
                # Append the letter to the input text
                input_text += chr(event.key)
                word.append(chr(event.key))
                # Check if the key pressed was backspace
            elif (event.key == pygame.K_BACKSPACE) & (len(word) > 0):
                # Remove the last character from the input text
                input_text = input_text[:-1]
                word.pop()
            elif (event.key == pygame.K_RETURN) & (len(word) == 5):
                compared = compare(actual_word, word)
                word = []

                if 0 in compared or 1 in compared:
                    # saves the answer in past_answers
                    for i in range(5):
                        past_answers[attempt].append((input_text[i], compared[i]))
                    attempt += 1
                else:
                    current_screen = win_screen
                input_text = []

                if attempt == 7:
                    current_screen = lose_screen

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click was within the bounds of the play button
            mouse_pos = pygame.mouse.get_pos()
            if (text_rect_play.collidepoint(mouse_pos)) & (current_screen == screen_main_menu):
                current_screen = screen_game
            elif text_rect_play.collidepoint(mouse_pos):
                pygame.quit()
    screen.fill((30, 30, 30))
    # Handle events
    if current_screen == screen_main_menu:
        # Draw the main menu
        font = pygame.font.Font(None, 36)
        text_play = font.render('Play', True, (255, 255, 255))
        text_rect_play = text_play.get_rect()
        text_rect_play.center = (400, 300)
        screen.blit(text_play, text_rect_play)

        # Update the display
    elif current_screen == screen_game:
        game(screen, input_text, font, attempt, past_answers)
    elif current_screen == win_screen:
        font = pygame.font.Font(None, 36)
        text_play = font.render('You Win!', True, (255, 255, 255))
        text_rect_play = text_play.get_rect()
        text_rect_play.center = (400, 300)
        screen.blit(text_play, text_rect_play)
    elif current_screen == lose_screen:
        font = pygame.font.Font(None, 36)
        text_play = font.render(f'You Loose! Word was {actual_word}', True, (255, 255, 255))
        text_rect_play = text_play.get_rect()
        text_rect_play.center = (400, 300)
        screen.blit(text_play, text_rect_play)
    pygame.display.flip()


# Quit Pygame
pygame.quit()