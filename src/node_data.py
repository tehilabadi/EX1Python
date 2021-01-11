from src.Point3D import Point3D

try:
    import Queue as Q
except ImportError:
    import queue as Q


class NodeData:
    """
        this class represents a node in a graph.
        contains a uniq key, tag for algorithms, p represents the location of the node and weight,
        also uses for algorithms
        @author Eliav Amar and Tehila Abadi
        """

    def __init__(self, key: int, tag: int = 0, p: tuple = None, weight: float = 0):
        p1 = None
        if p is not None:
            p1 = Point3D(p[0], p[1], p[2])
        self._key = key
        self._tag = tag
        self._p = p1
        self._weight = weight

    def get_key(self) -> int:
        """
        returns the key of the node
        :return: key: int
        """
        return self._key

    def set_tag(self, tag: int):
        """
        changes the tag of the node to the given tag
        :param tag: float
        """
        self._tag = tag

    def get_tag(self) -> int:
        """
        returns the tag of the node
        :return: tag: float
        """
        return self._tag

    def set_weight(self, weight: float):
        """
        changes the weight of the node to the given weight
        :param weight: float
        """

        self._weight = weight

    def get_weight(self) -> float:

        """
        returns the weight of the node
        :return: weight: float
        """
        return self._weight

    def get_location(self) -> Point3D:
        """
        returns the location of the node
        :return: p: Point3D
        """
        return self._p

    def set_location(self, x: float = 0, y: float = 0, z: float = 0):
        """
        changes the location of the node to the given Point3d
        :param x y z: float
        """
        point = Point3D(x, y, z)
        self._p = point

    def node_dict(self):
        """
        this method returns a dictionary represents the node.
        :return:
        """
        if self._p is None:
            return {"id": self._key}
        return {"pos": self._p.__str__(), "id": self._key}

    def __lt__(self, other):
        """
        this method check what  node is bigger
        """
        return self._weight - other.get_weight()

    def __eq__(self, other):
        """
        this method check if the nodes are equals
        """
        if other.get_key() == self._key:
            return True
        return False


