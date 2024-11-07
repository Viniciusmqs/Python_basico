class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configurações da nave
        self.ship_speed = 5

        # Configurações das balas
        self.bullet_speed = 5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)

        # Configurações dos aliens
        self.alien_speed = 1
        self.fleet_drop_speed = 10

        # Inicia contagem de aliens
        self.stats = Stats()

class Stats():
    def __init__(self):
        self.ships_left = 3
        self.score = 0
