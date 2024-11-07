import pygame
import sys
import random
from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()

    # Criação de aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Stats
    stats = ai_settings.stats
    score = 0

    while True:
        gf.check_events(ship, bullets)
        ship.update()
        gf.update_bullets(bullets, aliens, score, ai_settings, screen, ship)
        gf.update_aliens(aliens, ai_settings, ship, score, bullets, stats)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
      