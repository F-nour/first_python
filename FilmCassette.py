from Film import Film


class FilmCassette(Film):
    def __init__(self, name):
        super().__init__(name)
        self.magnetic = True

    def rewind(self):
        print("C'est long à rembobiner...")
        self.magnetic = True


    def watch(self, player):
        if player.type != "cassette":
            print("Le lecteur n'est pas un lecteur de cassette")
        else:
            print("Ca va commencer bientôt")
            super().watch(player)


