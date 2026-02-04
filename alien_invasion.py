import sys

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game() -> None:
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.screen_dimensions)
    
    # Define o título da janela
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(screen)
    
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
    

if __name__ == "__main__":
    run_game()