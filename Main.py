import pygame
from Settings import *
from Entities import *
from Game_functions import *
from Menu import *

# make the modules available
setting = Settings()
menu = Menu(setting)


screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
pygame.display.set_caption("Alien Invasion, By Mark Olieman")

player = Player(screen, setting)
bullet = Bullet(screen, setting, player)

# initizialize pygame
pygame.init()
pygame.mixer.init()

# initizialize the screen and set a caption

bullets = pygame.sprite.Group()
menu.intro(screen)


# function to start gaming
def gaming():

    # Game Loop
    while True:
        print(player.player_speed_left)
        # check events and make actions happen
        events(bullets, player, screen, setting)

        # update everything and draw bullets
        update(player, setting, bullets, screen)

        # draw player on screen with x and y position
        player.draw_me()

        # update the position of the bullets
        bullets.update(bullets)
        # update screen at certain fps

        pygame.display.update()
        setting.clock.tick(setting.fps)

# Start the game
gaming()

# Stop the game
pygame.quit()
