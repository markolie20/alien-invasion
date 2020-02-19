import pygame


class Settings:
    def __init__(self):

        # screen size
        self.screen_width = 800
        self.screen_height = 500

        # colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.dark_red = (150, 0, 0)
        self.dark_green = (0, 150, 0)
        self.dark_blue = (0, 0, 150)
        self.light_grey = (200, 200, 200)
        self.black_blueish = (50, 50, 100)

        # set clock and fps
        self.clock = pygame.time.Clock()
        self.fps = 60

        # calculate the seconds in every frame
        self.time = 1 / self.fps

        # bullet limit
        self.bullet_limit = 2


class DisplayText:
    def __init__(self, text, pos_x, pos_y, font_size, text_color):
        self.font = pygame.font.Font("freesansbold.ttf", font_size)
        self.text_surf = self.font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = (pos_x, pos_y)

        self.shadow_color = (0, 0, 0)

        self.text_surf_shadow = self.font.render(text, True, self.shadow_color)
        self.text_rect_shadow = self.text_surf.get_rect()
        self.text_rect_shadow.center = (pos_x + 10, pos_y + 5)

    def draw_me(self, screen):
        screen.blit(self.text_surf, self.text_rect)
        pygame.display.update()

    def draw_me_with_shadow(self, screen):
        screen.blit(self.text_surf_shadow, self.text_rect_shadow)
        screen.blit(self.text_surf, self.text_rect)

        pygame.display.update()


