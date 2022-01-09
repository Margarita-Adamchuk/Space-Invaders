class Ststs():
    """ Отслеживание статистики """

    def __init__(self):
        """ Статистика """
        self.reset_stats()
        self.run_game = True
        with open('max_score', 'r') as fill:
            self.max_score = int(fill.readline()) #чтение рекорда

    def reset_stats(self):
        """ Изменение статистики во время игры """
        self.guns_left = 2
        self.score = 0
        self.game_over = "GAME OVER"
