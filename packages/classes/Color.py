class Color:

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def get_rgb(self) -> str:
        return str(self.red) + " " + str(self.green) + " " + str(self.blue)
