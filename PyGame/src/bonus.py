import pygame
import random 
from pygame.sprite import Sprite

class Bonus(Sprite):
    """Classe para representar um bônus (raio) que dá tiro triplo."""
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('images/raio.png'), (20, 40))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = 2

    def update(self):
        """Move o raio para baixo."""
        self.rect.y += self.speed

    def blitme(self):
        """Desenha o raio na tela."""
        self.screen.blit(self.image, self.rect)
