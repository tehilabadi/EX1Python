from unittest import TestCase

from src.TestDiGraph import TestDiGraph
from src.GraphAlgo import GraphAlgo as gAlgo


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        graph = TestDiGraph.graph_creator()
        ga = gAlgo(graph)
        self.assertEqual(graph.v_size(), 5)
        self.assertIsNotNone(ga)
        self.assertEqual(ga.get_graph().v_size(), graph.v_size())
        self.assertTrue(graph.remove_node(1))
        self.assertEqual(ga.get_graph().v_size(), graph.v_size())

    def test_save_to_json(self):
        graph = TestDiGraph.graph_creator()
        ga = gAlgo(graph)
        ga.save_to_json("file")
        graph2 = TestDiGraph.graph_creator()
        ga2 = gAlgo(graph2)
        ga2.load_from_json("file")
        self.assertEqual(ga,ga2)
        self.assertEqual(ga.get_graph().v_size(), ga2.get_graph().v_size())
        for key in ga.get_graph().get_all_v():
            self.assertTrue(ga2.get_graph().get_node(key) is not None)
        for key in ga2.get_graph().get_all_v():
            self.assertTrue(ga.get_graph().get_node(key) is not None)
        graph.remove_edge(1,2)
        self.assertNotEqual(ga,ga2)

    def test_shortest_path(self):
        graph = TestDiGraph.graph_creator()
        ga = gAlgo(graph)
        self.assertEqual(ga.shortest_path(1, 0), (float('inf'), []))
        self.assertTrue(graph.add_edge(4, 0, 1))
        self.assertTrue(graph.add_edge(0, 1, 1))
        self.assertEqual(ga.shortest_path(1, 0), (2, [1, 4, 0]))
        self.assertEqual(ga.shortest_path(8, 0), (float('inf'), []))
        self.assertEqual(ga.shortest_path(0, 8), (float('inf'), []))
        self.assertEqual(ga.shortest_path(0, 0), (0, [0]))

    def test_connected_component(self):
        graph = TestDiGraph.graph_creator()
        ga = gAlgo(graph)
        self.assertEqual(len(ga.connected_component(0)), 1)
        self.assertEqual(len(ga.connected_component(1)), 2)
        self.assertTrue(graph.add_edge(3, 1, 0.2))
        self.assertEqual(len(ga.connected_component(1)), 3)
        self.assertTrue(graph.add_edge(4, 3, 2))
        self.assertEqual(len(ga.connected_component(1)), 4)
        self.assertEqual(len(ga.connected_component(6)), 0)

    def test_connected_components(self):
        graph = TestDiGraph.graph_creator()
        ga = gAlgo(graph)
        self.assertEqual(len(ga.connected_components()), 4)
        self.assertTrue(graph.add_edge(3, 1, 0.2))
        self.assertEqual(len(ga.connected_components()), 3)
        self.assertTrue(graph.add_edge(4, 3, 2))
        self.assertEqual(len(ga.connected_components()), 2)
        self.assertTrue(graph.remove_node(1))
        self.assertTrue(graph.remove_node(2))
        self.assertTrue(graph.remove_node(3))
        self.assertEqual(len(ga.connected_components()), 2)
        for k in ga.connected_components():
            self.assertEqual(len(k), 1)