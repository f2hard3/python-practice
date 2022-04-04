class Rect:
    def __init__(self, width: int, height: int) -> None:
        if width <= 0 or height <= 0:
            raise Exception('width or height should not be less than or equal to zero.')
        self.__width = width
        self.__height = height
    def get_area(self) -> int:
        return self.__width * self.__height
    @property
    def width(self) -> int:
        return self.__width
    @width.setter
    def width(self, width: int) -> int:
        if width <= 0:
            raise Exception('width should not be less than or equal to zero.')
        self.__width = width
    @property
    def height(self) -> int:
        return self.__height
    @height.setter
    def height(self, height: int) -> int:
        if height <= 0:
            raise Exception('height should not be less than or equal to zero.')
        self.__width = height

rect = Rect(10, 10)
rect.width += 10
print(rect.get_area())