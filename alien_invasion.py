"""main module"""

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import functions as gf

def run_game():
    """ Initialize game and create a screen object."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Make a ship
    ship = Ship(ai_settings, screen)
    #Make a group to store bullets in
    bullets = Group()
    aliens = Group()
    #Make an alien
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        gf.update_bullets(bullets)
        print(len(bullets))
run_game()
