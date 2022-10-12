class Cake:

    def __init__(self, flavor="chocolate"):
        self.flavor = flavor

    @classmethod
    def cut_parts(cls):
        print("Je coupe le gâteau en parts")

