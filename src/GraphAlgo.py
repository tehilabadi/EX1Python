from abc import ABC
from typing import List
from src import GraphInterface as Gi
from src.DiGraph import DiGraph as gr
from src.GraphAlgoInterface import GraphAlgoInterface as GA
import json
from numpy import random as ra
import matplotlib.pyplot as plt

try:
    import Queue as Queue
except ImportError:
    import queue as Queue


class GraphAlgo(GA, ABC):
    """
        This class represents a Directed (positive) Weighted Graph Theory Algorithms.
        @authors Eliav Amar and Tehila Abadi
        """

    def __init__(self, gra: gr = None):
        if gra is None:
            self._graph = gr()
        else:
            self._graph = gra

    def get_graph(self) -> Gi:
        return self._graph

    """
    :return: the graph
    """

    def load_from_json(self, file_name: str) -> bool:
        """
        this method creates a new DiGraph and initializes it properties from the given jason file.
        :param file_name: jason file
        the method returns true iff the graph loaded succesfuly
        :returns true or false
        """
        try:
            with open(file_name, "r") as file:
                graph = gr()
                graph_dict = json.load(file)
                nodes_dict = graph_dict["Nodes"]
                edges_dict = graph_dict["Edges"]
                for node in nodes_dict:
                    pos = None
                    if node.get("pos") is not None:
                        pos_value = node.get("pos").split(",")
                        x = float(pos_value[0])
                        y = float(pos_value[1])
                        z = float(pos_value[2])
                        pos = x, y, z
                    graph.add_node(node_id=node["id"], pos=pos)
                for edge in edges_dict:
                    graph.add_edge(edge["src"], edge["dest"], edge["w"])
            self._graph = graph
            return True
        except Exception:
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
            this method save the graph to the given file.
            returns true iff succeeded
            :param self:
            :param file_name:
            :return:true or false
            """
        graph_j = self._graph.graph_dict()
        try:
            with open(file_name, "w") as file:
                json.dump(graph_j, default=lambda o: o.__dict__, indent=4, fp=file)
                return True
        except Exception as e:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
                this method calculate the shortest path between the two given
                nodes on a Directed (positive) Weighted Graph, and returns the value of the path,
                with a list of all the nodes in the way.
                if there is no path between them the method returns 'inf' and empty list.
                :param id1: src node's id
                :param id2: dest node's id
                :return: the value of the path with a list of all the nodes in the way
                """
        if self._graph.get_node(id1) is None or self._graph.get_node(id2) is None:
            return float('inf'), []

        for i in self._graph.get_all_v().keys():
            self._graph.get_node(i).set_tag(-1)
            self._graph.get_node(i).set_weight(0)

        node = self._graph.get_node(id1)
        node.set_tag(0)
        pq = Queue.PriorityQueue()
        pq.put((node.get_weight(), node))
        while not pq.empty():
            node = pq.get()[1]
            for k, v in self._graph.all_out_edges_of_node(node.get_key()).items():
                tNode = self._graph.get_node(k)
                if tNode.get_tag() == -1:
                    tNode.set_tag(0)
                    tNode.set_weight(node.get_weight() + v)
                    pq.put((tNode.get_weight(), tNode))

                elif tNode.get_weight() > node.get_weight() + v:
                    tNode.set_weight(node.get_weight() + v)

        node = self._graph.get_node(id2)
        if node.get_tag() == -1:
            return float('inf'), []
        lis = []
        value = 0
        while node.get_key() != id1:
            lis.insert(0, node.get_key())
            for k, v in self._graph.all_in_edges_of_node(node.get_key()).items():
                if node.get_weight() == self._graph.get_node(k).get_weight() + v:
                    node = self._graph.get_node(k)
                    value += v
                    break
        lis.insert(0, node.get_key())
        return value, lis

    def connected_component(self, id1: int) -> list:
        """
            this method returns a list of all the nodes in the connected component of the given node
            if the node is not in the graph the method returns an empty list
            :param id1:
            :return: a list of all the nodes in the connected component of the given node
            """
        if self._graph.get_node(id1) is None:
            return []
        lis2 = []
        lis1 = []
        templis = []
        for k in self._graph.get_all_v():
            self._graph.get_node(k).set_tag(-1)
        self._graph.get_node(id1).set_tag(0)
        lis1.append(self._graph.get_node(id1))
        templis.append(self._graph.get_node(id1))
        while len(templis) != 0:
            node = templis.pop(0)
            for k in self._graph.all_out_edges_of_node(node.get_key()):
                temp = self._graph.get_node(k)
                if temp.get_tag() == -1:
                    lis1.append(temp)
                    temp.set_tag(0)
                    templis.append(temp)

        for k in self._graph.get_all_v():
            self._graph.get_node(k).set_tag(-1)

        self._graph.get_node(id1).set_tag(0)
        lis2.append(self._graph.get_node(id1))
        templis.append(self._graph.get_node(id1))
        while len(templis) != 0:
            node = templis.pop(0)
            for k in self._graph.all_in_edges_of_node(node.get_key()):
                temp = self._graph.get_node(k)
                if temp.get_tag() == -1:
                    lis2.append(temp)
                    temp.set_tag(0)
                    templis.append(temp)

        list3 = []
        for node in lis1:
            for temp in lis2:
                if node.get_key() == temp.get_key():
                    list3.append(node.get_key())
                    break
        return list3

    def connected_components(self) -> List[list]:
        """
        this method returns a list of lists of all the connected components in the graph
        if the graph is empty the method returns an empty list
        :param self:
        :return: a list of lists
        """
        if len(self._graph.get_all_v()) == 0:
            return []
        lis = []
        keys = {}
        for k in self._graph.get_all_v():
            if keys.get(k) is None:
                temp_lis = self.connected_component(k)
                lis.append(temp_lis)
                for t_n in temp_lis:
                    keys[t_n] = t_n
        return lis

    def plot_graph(self) -> None:
        """
        this method uses mathplotlib library  to create a visual frame for the graph algo.

        :return:
        """
        Min_x = float('inf')
        Max_x = -float('inf')
        Min_y = float('inf')
        Max_y = -float('inf')
        node_lis = []
        counter = 0
        for k in self._graph.get_all_v():
            if self._graph.get_node(k).get_location() is None:
                node_lis.append(self._graph.get_node(k))
                counter += 1
            else:
                pos = self._graph.get_node(k).get_location()
                if pos.get_x() < Min_x:
                    Min_x = pos.get_x()
                if pos.get_x() > Max_x:
                    Max_x = pos.get_x()
                if pos.get_y() < Min_y:
                    Min_y = pos.get_y()
                if pos.get_y() > Max_y:
                    Max_y = pos.get_y()
        if counter == len(self._graph.get_all_v()):
            self.set_pos(node_lis, [2, 50], [2, 50])
        elif counter - 1 == len(self._graph.get_all_v()):
            Max_x = Min_x + 40
            Max_y = Min_y + 40
            self.set_pos(node_lis, [Min_x, Max_x], [Min_y, Max_y])
        elif counter > 0:
            self.set_pos(node_lis, [Min_x, Max_x], [Min_y, Max_y])
        x_lis = []
        y_lis = []
        for k in self._graph.get_all_v():
            x_pos = self._graph.get_node(k).get_location().get_x()
            y_pos = self._graph.get_node(k).get_location().get_y()
            x_lis.append(x_pos)
            y_lis.append(y_pos)
            plt.annotate(text=k, xy=(x_pos + 0.0001, y_pos + 0.0001), zorder=8)
        for i in range(len(x_lis)):
            plt.scatter(x_lis[i], y_lis[i], zorder=4)

        for src_k in self._graph.get_all_v():
            for dest_k in self._graph.all_out_edges_of_node(src_k):
                src_x = self._graph.get_node(src_k).get_location().get_x()
                f_src_x = self._graph.get_node(src_k).get_location().get_y()
                dest_x = self._graph.get_node(dest_k).get_location().get_x()
                f_dest_x = self._graph.get_node(dest_k).get_location().get_y()
                plt.plot([src_x, dest_x], [f_src_x, f_dest_x], zorder=0)

        plt.show()

    def set_pos(self, node_lis, x, y):
        """
        this method define a randome position to every node without any position in the graph.
        :param node_lis: nodes without position
        :param x: max x
        :param y: max y
        """

        range_x = x[1] - x[0]
        range_y = y[1] - y[0]
        epsilon_x = (x[1] - x[0]) * 0.0001
        epsilon_y = (y[1] - y[0]) * 0.0001
        for node in node_lis:
            rand_x = epsilon_x + x[0] + (ra.rand(1) * range_x)
            rand_y = epsilon_y + y[0] + (ra.rand(1) * range_y)
            node.set_location(x=rand_x[0], y=rand_y[0])

    def __eq__(self, other):
        """
             this method override eq method of python.
             the method check if the current graph and the given one are identical.
             the method returns true if the graphs are equals, and false otherwise.
             :param other:
             :return:
             """
        if isinstance(other, self.__class__):
            return self._graph == other._graph
        return False
