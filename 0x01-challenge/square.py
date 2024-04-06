#!/usr/bin/python3

""" A module defining the class sqaure"""


class square():
    """The sqaure class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize an object"""
        for key, value in kwargs.items():
            setattr(self, key, value)
        if self.width < 0:
            self.width = 0
        if self.height < 0:
            self.height = 0

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Return the permiter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """A printable representation of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Test the creation of an object """

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
