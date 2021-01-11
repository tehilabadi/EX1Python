import numpy as np


class Point3D:
    """
        this class represents a three dimensions point. contains x, y, z
        @authors Eliav Amar and Tehila Abadi
        """

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self._p = (x, y, z)

    def set_x(self, x):
        """
        changes x to the given x
        :param x:
        """
        pos = self._p
        self._p = (x, pos[1], pos[2])

    def set_y(self, y):
        """
        changes y to the given y
        :param y:
        """
        pos = self._p
        self._p = (pos[0], y, pos[2])

    def set_z(self, z):
        """
        changes z to the given z
        :param z:
        """
        pos = self._p
        self._p = (pos[0], pos[1], z)

    def get_x(self) -> float:
        """
        returns x
        :return: x
        """
        return self._p[0]

    def get_y(self) -> float:
        """
        returns y
        :return: y
        """
        return self._p[1]

    def get_z(self) -> float:
        """
        returns z
        :return: z
        """
        return self._p[2]

    def get_dist(self, p) -> float:
        """
        this method calculate the distance between the current and the given Point3D
        :param Point3D p:
        :return: the distance
        """
        sum1 = np.sqrt(pow(self._p[0] - p.get_x(), 2) + pow(self._p[1] - p.get_y(), 2) + pow(self._p[2] - p.get_z(), 2))
        return sum1

    def __str__(self):
        """
        :return: a string of Point3D
        """
        return "" + str(self._p[0]) + "," + str(self._p[1]) + "," + str(self._p[2])
