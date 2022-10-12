class Rectangle:

    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color

    def calculate_area(self):
        result = self.length * self.width
        return result
        