class Settings:
    """Define as configurações globais do jogo"""
    
    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_dimensions = (self.screen_width, self.screen_height)
        # RGB: cinza claro
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        