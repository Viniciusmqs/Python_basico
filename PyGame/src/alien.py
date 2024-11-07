import pygame
import random
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(random.choice(['images/alien.png', 'images/alien_fraco.png', 'images/alien_forte.png']))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Inicializa cada alien na parte superior da tela
        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = ai_settings.alien_speed

    def update(self):
        """Move o alien para baixo"""
        self.rect.y += self.speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)

