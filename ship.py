import pygame
from settings import Settings

class Ship:
    """ Uma nave espacial. """
    def __init__(self, screen: pygame.Surface, ai_settings: Settings) -> None:
        self.screen = screen
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.ai_settings = ai_settings
        
        # Alinha o retângulo da espaçonave com o retângulo da janela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.center = float(self.rect.centerx)
    
    def blitme(self) -> None:
        """Renderiza a espaçonave na janela."""
        self.screen.blit(self.image, self.rect)
    
    def update(self) -> None:
        """Atualiza o movimento da espaçonave."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        
        self.rect.centerx = int(self.center)