import pygame

from defs import window_size
from game import game

pygame.init()

# Set the window size

font = pygame.font.Font(None, 36)
# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption('Main Menu')

screen_main_menu = 0
screen_game = 1

current_screen = screen_main_menu
# Run the game loop
running = True
input_text = ''

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
            elif event.key == pygame.K_BACKSPACE:
                # Remove the last character from the input text
                input_text = input_text[:-1]
                word.pop()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click was within the bounds of the play button
            mouse_pos = pygame.mouse.get_pos()
            if text_rect_play.collidepoint(mouse_pos):
                current_screen = screen_game

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
        game(screen, input_text, font)
    print(word)
    pygame.display.flip()


# Quit Pygame
pygame.quit()