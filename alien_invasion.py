import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game() -> None:
    pygame.init()

    ai_settings = Settings()
    # Cria a janela com um certo tamanho e retorna sua superfície
    screen = pygame.display.set_mode(ai_settings.screen_dimensions)
    
    # Define o título da janela
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(screen, ai_settings)
    
    bullets = Group()
    
    aliens = Group()

    gf.create_fleet(
        ai_settings, screen, aliens
    )
    
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        
        # Atualiza o movimento da espaçonave
        ship.update()
        
        aliens.draw(screen)
         
        bullets.update()
        
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
    

if __name__ == "__main__":
    run_game()