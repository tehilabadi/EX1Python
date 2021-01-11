from unittest import TestCase

from src.node_data import NodeData as node_data
from src.DiGraph import DiGraph


class TestDiGraph(TestCase):
    def test_v_size(self):
        graph = self.graph_creator()
        self.assertEqual(graph.v_size(), 5)
        graph.remove_node(1)
        self.assertEqual(graph.v_size(), 4)
        graph.add_node(5)
        self.assertEqual(graph.v_size(), 5)
        graph.add_node(2)
        self.assertEqual(graph.v_size(), 5)

    def test_e_size(self):
        graph = self.graph_creator()
        self.assertEqual(graph.e_size(), 6)
        graph.remove_edge(1, 2)
        self.assertEqual(graph.e_size(), 5)
        graph.add_edge(1, 2, 2)
        self.assertEqual(graph.e_size(), 6)
        graph.add_edge(1, 2, 2)
        self.assertEqual(graph.e_size(), 6)

    def test_get_all_v(self):
        graph = self.graph_creator()
        self.assertEqual(len(graph.get_all_v()), 5)
        graph.remove_node(1)
        self.assertEqual(len(graph.get_all_v()), 4)
        graph.add_node(1)
        self.assertEqual(len(graph.get_all_v()), 5)

    def test_all_in_edges_of_node(self):
        graph = self.graph_creator()
        self.assertEqual(1, len(graph.all_in_edges_of_node(1)))
        self.assertEqual(2, len(graph.all_in_edges_of_node(3)))
        self.assertEqual(5, graph.all_in_edges_of_node(3).get(2))
        graph.remove_edge(2, 1)
        self.assertEqual(0, len(graph.all_in_edges_of_node(1)))

    def test_all_out_edges_of_node(self):
        graph = self.graph_creator()
        self.assertEqual(3, len(graph.all_out_edges_of_node(1)))
        self.assertEqual(1, len(graph.all_out_edges_of_node(3)))
        self.assertEqual(None, graph.all_out_edges_of_node(3).get(2))
        graph.remove_edge(1, 2)
        self.assertEqual(2, len(graph.all_out_edges_of_node(1)))

    def test_get_mc(self):
        graph = self.graph_creator()
        self.assertEqual(11,graph.get_mc())
        graph.remove_edge(2, 4)
        self.assertEqual(11, graph.get_mc())
        graph.remove_edge(2, 3)
        self.assertEqual(12, graph.get_mc())
        graph.remove_node(1)
        self.assertEqual(13, graph.get_mc())
        graph.add_edge(3,4,1)
        graph.add_edge(3, 4, 2)
        self.assertEqual(13, graph.get_mc())

    def test_add_edge(self):
        graph = self.graph_creator()
        self.assertEqual(6, graph.e_size())
        self.assertFalse(graph.add_edge(1, 2, 1))
        self.assertFalse(graph.add_edge(1, 5, 20))
        self.assertFalse(graph.add_edge(1, 0, -20))
        self.assertTrue(graph.add_edge(1, 0, 20))
        self.assertEqual(7, graph.e_size())
        self.assertEqual(graph.all_out_edges_of_node(1).get(0), 20)

    def test_add_node(self):
        graph = self.graph_creator()
        self.assertEqual(5, len(graph.get_all_v()))
        for key in graph.get_all_v():
            self.assertEqual(graph.get_all_v().get(key).get_key(), key)
        self.assertFalse(graph.add_node(1))
        self.assertTrue(graph.add_node(6))
        self.assertEqual(6, len(graph.get_all_v()))

    def test_remove_node(self):
        graph = self.graph_creator()
        self.assertEqual(5, len(graph.get_all_v()))
        self.assertIsNotNone(graph.get_all_v().get(1))
        self.assertTrue(graph.remove_node(1))
        self.assertIsNone(graph.get_all_v().get(1))
        self.assertFalse(graph.remove_node(8))
        self.assertEqual(4, len(graph.get_all_v()))
        for Key in graph.get_all_v():
            for key2 in graph.all_in_edges_of_node(Key):
                self.assertNotEqual(1, key2)
        for Key in graph.get_all_v():
            for key2 in graph.all_out_edges_of_node(Key):
                self.assertNotEqual(1, key2)

    def test_remove_edge(self):
        graph = self.graph_creator()
        self.assertEqual(graph.e_size(), 6)
        self.assertFalse(graph.remove_edge(1, 0))
        self.assertTrue(graph.remove_edge(1, 4))
        self.assertEqual(graph.e_size(), 5)
        self.assertIsNone(graph.all_in_edges_of_node(4).get(1))
        self.assertIsNone(graph.all_out_edges_of_node(1).get(4))
        self.assertEqual(graph.get_mc(), 12)

    @staticmethod
    def graph_creator():
        graph = DiGraph()
        for i in range (5):
            graph.add_node(i)
        graph.add_edge(1, 2, 1)
        graph.add_edge(1, 3, 1)
        graph.add_edge(1, 4,1)
        graph.add_edge(2, 1, 1)
        graph.add_edge(2, 3, 5)
        graph.add_edge(3, 4, 1)

        return graph




