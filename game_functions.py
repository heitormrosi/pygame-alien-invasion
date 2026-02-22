import sys

import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien

def check_events(
        ai_settings: Settings, 
        screen: pygame.Surface, 
        ship: Ship, 
        bullets: Group
    ) -> None:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(
                    event, 
                    ai_settings,
                    screen,
                    ship,
                    bullets
                )
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)


def check_keydown_events(
        event: pygame.event.Event, 
        ai_settings: Settings, 
        screen: pygame.Surface, 
        ship: Ship, 
        bullets: Group
    ) -> None:
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(
            ai_settings,
            screen,
            ship,
            bullets
        )
    if event.key == pygame.K_q:
        pygame.quit()
        sys.exit()


def check_keyup_events(event: pygame.event.Event, ship: Ship) -> None:
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(
          ai_settings: Settings, 
          screen: pygame.Surface, 
          ship: Ship, 
          aliens: Group,
          bullets: Group
      ) -> None:
    screen.fill(ai_settings.bg_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Renderiza a espaçonave na tela
    ship.blitme()
    
    for alien in aliens.sprites():
        alien.blitme()
    
    # Atualiza a renderização da janela
    pygame.display.flip()

def update_bullets(bullets):
    """ Atualiza a posição dos projéteis e se livra dos projéteis antigos. """

    # Atualiza as posições dos projéteis 
    bullets.update()
    # Livra-se dos projéteis que desapareceram 
    for bullet in bullets.copy(): 
        if bullet.rect.bottom <= 0: 
            bullets.remove(bullet)


def fire_bullet(
        ai_settings: Settings,
        screen: pygame.Surface,
        ship: Ship,
        bullets: Group
    ) -> None:
    if len(bullets) < ai_settings.bullets_allowed:
        bullets.add(
            Bullet(
                ai_settings,
                screen,
                ship
            )
        )


def create_fleet(
    ai_settings: Settings,
    screen: pygame.Surface,
    aliens: Group       
) -> None:
    alien = Alien(ai_settings, screen)
    
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x

        aliens.add(alien)