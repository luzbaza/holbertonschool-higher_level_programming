#!/usr/bin/python3
""" square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ method so that it returns Rectangle """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ Update the class """
        if len(args) > 0:
            atri = ["id", "size", "x", "y"]
            for posi in range(len(args)):
                setattr(self, atri[posi], args[posi])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
