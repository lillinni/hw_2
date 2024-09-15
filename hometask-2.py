class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass
    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length  

    def calculate_area(self):
        return self.__side_length ** 2  

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{Figure.unit}, area: {area}{Figure.unit}")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length  
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width  

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit}, area: {area}{Figure.unit}")


figures_list = [Square(5), Square(7), Rectangle(5, 8), Rectangle(4, 6), Rectangle(3, 9)]

for figure in figures_list:
    figure.info()
