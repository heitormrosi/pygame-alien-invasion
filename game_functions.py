import sys

import pygame
from settings import Settings
from ship import Ship

def check_events() -> None:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


def update_screen(
          ai_settings: Settings, screen: pygame.Surface, ship: Ship) -> None:
    screen.fill(ai_settings.bg_color)
        
    ship.blitme()
    
    # Atualiza a renderização da janela
    pygame.display.flip()