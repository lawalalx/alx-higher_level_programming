#!/usr/bin/python3
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initializes the Rectangle object with width and height.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Computes the area of the rectangle.

        :return: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        :return: A string in the format [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
