class Person:

    def __init__(self, name):
        """Donne un nom."""
        self.name = name

    def walk(self):
        """Marche."""
        print(f"{self.name} marche.")