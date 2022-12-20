import pygame

from defs import window_size, cell_size, grid_size

grid_width = cell_size[0] * grid_size[0]
grid_height = cell_size[1] * grid_size[1]
grid_x = (window_size[0] - grid_width) // 2
grid_y = (window_size[1] - grid_height) // 2


def game(screen, input_text, font, attempt, past_answers):
    for row in range(grid_size[1]):
        for col in range(grid_size[0]):
            x = grid_x + col * cell_size[0]
            y = grid_y + row * cell_size[1]
            rect = pygame.Rect(x, y, cell_size[0], cell_size[1])

            pygame.draw.rect(screen, (255, 255, 255), rect, 1)
            if (len(input_text) > col) & (row == attempt):
                input_surface = font.render(input_text[col], True, (255, 255, 255))
                input_rect = input_surface.get_rect()
                input_rect.center = (x + 25, y + 25)
                screen.blit(input_surface, input_rect)
            elif row < attempt:
                past_answer_surface = None
                if past_answers[row][col][1] == 0:
                    past_answer_surface = font.render(past_answers[row][col][0], True,
                                                      (200, 0, 0))
                elif past_answers[row][col][1] == 1:
                    past_answer_surface = font.render(past_answers[row][col][0], True,
                                                      (200, 120, 0))
                else:
                    past_answer_surface = font.render(past_answers[row][col][0], True,
                                                      (0, 200, 0))
                past_rect = past_answer_surface.get_rect()
                past_rect.center = (x + 25, y + 25)
                screen.blit(past_answer_surface, past_rect)
