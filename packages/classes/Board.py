from packages.classes.Position import Position


class Board:

    def __init__(self, elements: list):
        self.elements = elements

    def get_element_with_position(self, position: Position):
        return self.get_element(position.x, position.y)

    def get_element(self, x: int, y: int):
        try:
            return self.elements[y][x]
        except:
            print(self.elements)
            print(x)
            print(y)
