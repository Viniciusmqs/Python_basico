# stats.py
class Stats:
    """Classe para gerenciar as estatísticas do jogo."""

    def __init__(self):
        """Inicializa as estatísticas do jogo."""
        self.reset_stats()
        self.game_active = True  # Controla se o jogo está ativo ou pausado

    def reset_stats(self):
        """Inicializa as estatísticas que podem mudar durante o jogo."""
        self.ship_lives = 3  # Número de vidas da nave
        self.score = 0  # Pontuação do jogador
