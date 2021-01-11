from abc import ABC
from src.GraphInterface import GraphInterface as Gi
from node_data import NodeData as node_data
from Point3D import Point3D as P3D


class DiGraph(Gi, ABC):
    """
        this class represents a weighted directional graph.
        contains dictionary of the nodes, dictionary of all the edges from each node,
        and dictionary of all the edges to each node in the graph.
        @authors Eliav Amar and Tehila Abadi
        """

    def __init__(self):
        self._graph = {}
        self._edgesIn = {}
        self._edgesOut = {}
        self._mc = 0
        self._sizeOfEdge = 0

    def v_size(self) -> int:
        """
                  returns the number of nodes in the graph
                  :return: node size: int
                  """
        return len(self._graph.values())

    def e_size(self) -> int:

        """
                returns the number of edges in the graph
                :return: edge size: int
                """
        return self._sizeOfEdge

    def get_all_v(self) -> dict:

        """
                returns a dictionary of all the nodes in the graph {key, node_data)
                :return: all the nodes on the graph
                """
        return self._graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
                 returns a dictionary of all the edges coming to the given node
                 :param id1:
                 :return:in edges: dictionary
                 """

        if self._edgesIn.get(id1) is None:
            return {}
        return self._edgesIn.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
                    returns a dictionary of all the edges coming from the given node
                    :param id1:
                    :return:out edges: dictionary
                    """
        if self._edgesOut.get(id1) is None:
            return {}
        return self._edgesOut.get(id1)

    def get_mc(self) -> int:

        """
                counts the action preformed on the graph
                :return: mc: int
                """
        return self._mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
                    this method add an edge between the two given nodes, with the given weight
                    if there is already an edge between the two given nodes the function does nothing.
                    returns true iff the edge added to the graph successfully
                    :param id1: int
                    :param id2: int
                    :param weight: float
                    :return: true or false
                    """
        if weight <= 0 or self._graph.get(id1) is None or self._graph.get(id2) is None or self._edgesOut.get(id1).get(
                id2) is not None:
            return False
        self._edgesOut[id1][id2] = weight
        self._edgesIn[id2][id1] = weight
        self._mc += 1
        self._sizeOfEdge += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
                  this method add creates a new node_data with the given key and add it to the graph.
                  if there is already a node with the given key in the graph the method does nothing
                  returns true iff the node added to the graph successfully
                  :param node_id: int
                  :param pos:
                  :return:true or false
                  """
        if self._graph.get(node_id) is None:
            self._graph[node_id] = node_data(key=node_id, p=pos)
            self._edgesOut[node_id] = {}
            self._edgesIn[node_id] = {}
            self._mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
                this method removes from the graph the node with the given key
                returns true iff the node removed successfully
                :param node_id:int
                :return:true or false
                """
        if self._graph.get(node_id) is None:
            return False
        self._graph.pop(node_id)
        for Key in self.all_out_edges_of_node(node_id):
            self.all_in_edges_of_node(Key).pop(node_id)
            self._sizeOfEdge -= 1

        for Key in self.all_in_edges_of_node(node_id):
            self.all_out_edges_of_node(Key).pop(node_id)
            self._sizeOfEdge -= 1
        self._edgesIn[node_id] = self._edgesOut[node_id] = None
        self._mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
                    this method removes from the graph the edge between the two given nodes
                    returns true iff the edge removed successfully
                    :param node_id node_id2:int
                    :return:true or false
                    """
        if self._graph.get(node_id1) is None or self._graph.get(node_id2) is None:
            return False
        if self._edgesOut.get(node_id1).get(node_id2) is None:
            return False
        self._edgesOut.get(node_id1).pop(node_id2)
        self._edgesIn.get(node_id2).pop(node_id1)
        self._sizeOfEdge -= 1
        self._mc += 1
        return True

    def get_node(self, Key):
        """
                this method returns the node_data with the given key
                :param Key: int
                :return: node_data
                """
        return self._graph.get(Key)

    def graph_dict(self):
        """
                this method returns a dictionary represents the graph.
                Nodes key for a list of all the nodes,
                and dest key for a list of all the edges in the graph
                :return: a dictionary represents the graph
                """
        lis_node = []
        lis_edge = []
        for i in self._graph.keys():
            lis_node.append(self.get_node(i).node_dict())
            for k, v in self.all_out_edges_of_node(i).items():
                edge = {"src": i, "w": v, "dest": k}
                lis_edge.append(edge)

        return {"Edges": lis_edge, "Nodes": lis_node}

    def __eq__(self, other):
        """
        this method override eq method of python.
        the method check if the current graph and the given one are identical.
        the method returns true if the graphs are equals, and false otherwise.
        :param other:
        :return:
        """

        if isinstance(other, self.__class__):
            for k in other.get_all_v():
                if self.get_node(k) != other.get_node(k):
                    return False
                for tag, v in other.all_out_edges_of_node(k).items():
                    try:
                        if self._edgesOut[k][tag] != v:
                            return False
                    except Exception:
                        return False
            return True
        return False