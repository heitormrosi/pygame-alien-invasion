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


def get_number_aliens_x(
    ai_settings: Settings,
    alien_width: int
) -> int:
    """Determina o número de aliens dentro de uma linha."""
    avaliable_space_x = ai_settings.screen_width - 2 * alien_width

    number_aliens_x = int(avaliable_space_x / (2 * alien_width))

    return number_aliens_x

def get_number_rows(
    ai_settings: Settings,
    ship_height: int,
    alien_height: int
) -> int:
    """Determina o número de linhas de aliens na tela do jogo"""
    available_space_y = (
        ai_settings.screen_height - (3 * alien_height) - ship_height
    )

    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows

def create_alien(
    ai_settings: Settings,
    screen: pygame.Surface,
    aliens: Group,
    alien_number: int,
    row_number: int
) -> None:
    """Cria um aligenígena"""
    alien = Alien(
        ai_settings,
        screen
    )

    alien_width = alien.rect.width
    alien.rect.x = alien_width + 2 * alien_width * alien_number

    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

    aliens.add(alien)
    

def create_fleet(
    ai_settings: Settings,
    screen: pygame.Surface,
    ship: Ship,
    aliens: Group       
) -> None:
    alien = Alien(ai_settings, screen)

    number_aliens_x = get_number_aliens_x(
        ai_settings,
        alien.rect.width
    )

    number_rows = get_number_rows(
        ai_settings,
        ship.rect.height,
        alien.rect.height
    )

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(
                ai_settings,
                screen,
                aliens,
                alien_number,
                row_number
            )