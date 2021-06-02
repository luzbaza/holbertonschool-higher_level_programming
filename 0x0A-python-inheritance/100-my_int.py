#!/usr/bin/python3
""" MyInt """


class MyInt(int):
    """  inherits  from int """

    def __eq__(self, value):
        """ equals """

        return super().__ne__(value)

    def __ne__(self, value):
        """ equals """
        return super().__eq__(value)
