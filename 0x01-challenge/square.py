#!/usr/bin/python3

""" A module defining the class sqaure"""
class square():
    """The sqaure class"""
    width = 0

    def __init__(self, *args, **kwargs):
        """Initialize an object"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Return the permiter of the square"""
        return (self.width * 4)

    def __str__(self):
        """A printable representation of the square"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
