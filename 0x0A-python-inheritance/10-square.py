#!/usr/bin/python3
class Square(Rectangle):
    def __init__(self, size):
        """
        Initializes the Square object with size.

        :param size: The size of the square.
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        :return: A string in the format [Rectangle] <size>/<size>
        """
        return "[Rectangle] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

