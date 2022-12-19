import pygame

from defs import window_size, cell_size, grid_size

grid_width = cell_size[0] * grid_size[0]
grid_height = cell_size[1] * grid_size[1]
grid_x = (window_size[0] - grid_width) // 2
grid_y = (window_size[1] - grid_height) // 2


def game(screen, input_text, font):
    for row in range(grid_size[1]):
        for col in range(grid_size[0]):
            x = grid_x + col * cell_size[0]
            y = grid_y + row * cell_size[1]
            rect = pygame.Rect(x, y, cell_size[0], cell_size[1])
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)
            input_surface = font.render(input_text, True, (255, 255, 255))
            input_rect = input_surface.get_rect()
