#!/usr/bin/python3
""" Square module
    Classes: square
"""


class square():
    """ Square class definition
        Class attributes: width, height
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Constructor method """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of the square"""
        return (self.width * 4)

    def __str__(self):
        """ String representation of the square """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = square(width=12, height=9)
    t = square(width=9, height=10)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
