import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    """ Um alienígena """

    def __init__(
            self, 
            ai_settings: Settings, 
            screen: pygame.Surface
            ) -> None:
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    
    def blitme(self) -> None:
        self.screen.blit(self.image, self.rect)

    def update(self) -> None:
        """ Move o alien para a direita ou para a esquerda """

        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = int(self.x)

    def check_edges(self) -> bool:
        """ True se alien na borda da janela """
        screen_rect = self.screen.get_rect()

        return (self.rect.right >= screen_rect.right) \
            or (self.rect.left <= 0)