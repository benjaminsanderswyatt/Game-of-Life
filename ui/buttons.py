import pygame

pygame.font.init()
button_font = pygame.font.Font(None, 18)

class Button:
    def __init__(self, text, text_colour, bg_colour, hover_colour, clicked_colour, boarder_colour, x_pos, y_pos, width,
                 height, enabled):
        self.text = text
        self.text_colour = text_colour
        self.bg_colour = bg_colour
        self.hover_colour = hover_colour
        self.clicked_colour = clicked_colour
        self.boarder_colour = boarder_colour
        self.size = width, height
        self.pos = x_pos, y_pos
        self.rect = pygame.rect.Rect(self.pos, self.size)
        self.enabled = enabled

    def draw(self, screen):
        button_text = button_font.render(self.text, True, self.text_colour)
        button_rect = self.rect

        # Get the size of the text
        text_width, text_height = button_text.get_size()

        # Calculate the centered position for the text
        text_x = self.rect.centerx - text_width // 2
        text_y = self.rect.centery - text_height // 2

        if self.enabled:
            if self.check_clicked():
                pygame.draw.rect(screen, self.clicked_colour, button_rect, 0, 5)
            elif self.check_hover():
                pygame.draw.rect(screen, self.hover_colour, button_rect, 0, 5)  # Hover color
            else:
                pygame.draw.rect(screen, self.bg_colour, button_rect, 0, 5)
        else:
            pygame.draw.rect(screen, "dark grey", button_rect, 0, 5)
        pygame.draw.rect(screen, self.boarder_colour, button_rect, 2, 5)
        screen.blit(button_text, (text_x, text_y))

    def check_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = self.rect
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = self.rect
        if button_rect.collidepoint(mouse_pos):
            return True
        else:
            return False
