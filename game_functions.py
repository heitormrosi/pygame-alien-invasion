import sys

import pygame
from settings import Settings
from ship import Ship

def check_events(ship: Ship) -> None:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ship)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)


def check_keydown_events(event: pygame.event.Event, ship: Ship) -> None:
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event: pygame.event.Event, ship: Ship) -> None:
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(
          ai_settings: Settings, screen: pygame.Surface, ship: Ship) -> None:
    screen.fill(ai_settings.bg_color)
        
    # Renderiza a espaçonave na tela
    ship.blitme()
    
    # Atualiza a renderização da janela
    pygame.display.flip()