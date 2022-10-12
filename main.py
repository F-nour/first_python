from Cake import Cake
from Film import Film
from FilmCassette import FilmCassette
from Person import Person
from Player import Player
from Rectancle import Rectangle

cake = Cake("vanilla")
print(cake.flavor)
print(cake.cut_parts())

rectangle = Rectangle(150, 200, "blue")
print(rectangle.width)
print(rectangle.length)
rectangle.width = 300
area = rectangle.calculate_area()
print(area)

dvd = Player('dvd')
cassette = Player('cassette')
film = Film("L'odyssée de l'espace")
film_cassette = FilmCassette("Blade runner")
print(film_cassette.name)
film_cassette.watch(dvd)
film_cassette.watch(cassette)

volunteers = [Person("Alice"), Person("Bob"), Person("Carol")]
for volunteer in volunteers:
    volunteer.walk()