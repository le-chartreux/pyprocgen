class Color:

    def __init__(self, red: int, green: int, blue: int):
        if Color.is_part_of_color(red) and Color.is_part_of_color(green) and Color.is_part_of_color(blue):
            self.red = red
            self.green = green
            self.blue = blue
        else:
            raise Exception(
                "Error: impossible to set element for a Color, inputs are " +
                str(red) + str(green) + str(blue) +
                ", they must be between 0 and 255."
            )

    @staticmethod
    def is_part_of_color(number: int) -> bool:
        try:
            return 0 <= number <= 255
        except ValueError:
            raise Exception(
                "Error: impossible to set element for a Color, an input is a " +
                str(type(number)) +
                ", must be an int."
            )

    def get_rgb(self) -> str:
        return str(self.red) + " " + str(self.green) + " " + str(self.blue)
