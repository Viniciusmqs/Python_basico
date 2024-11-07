import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 15)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.color = (255, 0, 0)
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed

    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

