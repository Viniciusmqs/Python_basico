import pygame
import random
from bullet import Bullet
from alien import Alien

def check_events(ship, bullets):
    """Verifica eventos de teclado e mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_SPACE:
                fire_bullet(bullets, ship)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def fire_bullet(bullets, ship):
    """Dispara uma bala."""
    new_bullet = Bullet(ship.screen, ship)
    bullets.add(new_bullet)

def update_bullets(bullets, aliens, score, ai_settings, screen, ship):
    """Atualiza as balas e remove as que saem da tela."""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(bullets, aliens, score, ai_settings, screen, ship)

def check_bullet_alien_collisions(bullets, aliens, score, ai_settings, screen, ship):
    """Verifica se uma bala atingiu um alien."""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            score += ai_settings.alien_speed * 10

def update_aliens(aliens, ai_settings, ship, score, bullets, stats):
    """Atualiza os aliens e verifica colisões."""
    aliens.update()

    for alien in aliens.copy():
        if alien.rect.bottom >= ship.screen_rect.bottom:
            aliens.remove(alien)
            stats.ships_left -= 1
            if stats.ships_left == 0:
                print("Game Over")
                pygame.quit()
                quit()

    # Criação de novos aliens
    if len(aliens) == 0:
        create_fleet(ai_settings, ship.screen, ship, aliens)

def create_fleet(ai_settings, screen, ship, aliens):
    """Cria a frota de aliens."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = int(ai_settings.screen_width / (alien_width * 2))

    # Preenchendo a tela com aliens
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.rect.x = alien_width * alien_number
        aliens.add(alien)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Atualiza a tela do jogo."""
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.blitme()

    for alien in aliens.sprites():
        alien.blitme()

    ship.blitme()
    pygame.display.flip()
