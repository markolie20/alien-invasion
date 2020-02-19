from Settings import *
import time


class Menu:
    def __init__(self, setting):
        self.setting = setting
        self.font_size = 100

        self.intro_text_1_pos_x = (setting.screen_width + 400)
        self.intro_text_1_pos_y = \
            (setting.screen_height / 2 - self.font_size)
        self.intro_text_1 = "A game by:"

        self.intro_text_2_pos_x = -400
        self.intro_text_2_pos_y = \
            (setting.screen_height / 2 + self.font_size)
        self.intro_text_2 = "Mark Olieman"

        self.intro_text_title_pos_x = (setting.screen_width / 2)
        self.intro_text_title_pos_y = (setting.screen_height + self.font_size)
        self.intro_text_title = "Alien Invasion!"

        self.speed = -100 * self.setting.time

        self.menu_1 = True
        self.menu_2 = True
        self.menu_title = True

    def intro(self, screen):
        screen.fill(self.setting.black_blueish)
        pygame.display.update()

        while self.menu_2:
            print(self.speed)
            print(self.setting.time * self.setting.fps)
            print(self.setting.time * -100)
            print(self.speed * 60)
            if self.intro_text_2_pos_x <= self.setting.screen_width + 400 and \
                    self.intro_text_1_pos_x >= -400:
                self.intro_text_1_pos_x += self.speed
                self.intro_text_2_pos_x -= self.speed

                display_intro_1 = DisplayText(self.intro_text_1,
                                              self.intro_text_1_pos_x,
                                              self.intro_text_1_pos_y,
                                              self.font_size,
                                              self.setting.light_grey)

                display_intro_2 = DisplayText(self.intro_text_2,
                                              self.intro_text_2_pos_x,
                                              self.intro_text_2_pos_y,
                                              self.font_size,
                                              self.setting.light_grey)

                screen.fill(self.setting.black_blueish)

                display_intro_1.draw_me_with_shadow(screen)
                display_intro_2.draw_me_with_shadow(screen)

                if (self.setting.screen_width / 2 + self.speed / 2) < \
                        self.intro_text_2_pos_x < \
                        (self.setting.screen_width / 2 - self.speed / 2) and\
                        (self.setting.screen_width / 2 + self.speed / 2) < \
                        self.intro_text_1_pos_x < \
                        (self.setting.screen_width / 2 - self.speed / 2):
                    time.sleep(5)
            else:
                self.menu_2 = False

        while self.menu_title:
            if self.intro_text_title_pos_y >= self.font_size:
                self.intro_text_title_pos_y += self.speed

                display_intro_title = DisplayText(self.intro_text_title,
                                                  self.intro_text_title_pos_x,
                                                  self.intro_text_title_pos_y,
                                                  self.font_size,
                                                  self.setting.light_grey)

                screen.fill(self.setting.black_blueish)
                display_intro_title.draw_me_with_shadow(screen)
            else:
                time.sleep(10)
                self.menu_title = False
