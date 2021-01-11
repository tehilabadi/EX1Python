ex3 <h1>  README</h1>
@auther Eliav Liav Amar and Tehila Abadi</p>

<br>
**File list** <br>
-----------------
node_data >>		represents node in graph (private class)<br>
Point3D >>                                 3D geo location <br>
DiGraph >>                                GraphInterface implementation<br>
GraphAlgo>>	  	GraphAlgoInterface implementation<br>
  
**tests:**<br>
--------------------
TestDiGraph>>		junit test file for DiGraph<br>
TestGraphAlgo>>		junit test file for GraphAlgo<br>

<h1>Introduction api</h1>

<h1>Point3D </h1>
Represents the  geo location of an object on directed weighted graph.<br>
<br>
<h1>node_data class</h1>
represents the node (vertex) and all its properties in adirected weighted undirected graph<br>
<br>
<h1>DiGraph</h1>
Implements the abstract class GraphInterface<br>
Represents directed wighted  graph and all its properties.<br>
<br>
<h1>GraphAlgo </h1>
Implements the abstract class GraphAlgoInterface<br>
Represents the algorithems on a directed weighted graph.<br>
<br>
<h1>Functions implemets api</h1><br>
<br>

<h1>node_data class</h1>
this class represents a three dimensions point. contains x, y, z<br>
<br>
__def get_dist(self, p) -> float:__<br>
this method returns the distance between two three dimentions point using distance equation<br>
<br>
<h1>node_data class</h1>
<br>
 __def __init__:__<br>
this method initilizes a new node_data weith the given properties.<br>
<br>
__def node_dict(self):__<br>
this method returns a dictionary represents the node.<br>
contains the location and the id key of the node<br>
<br>
<h1>DiGraph</h1>
this class represents a weighted directional graph.<br>
contains dictionary of the nodes, dictionary of all the edges from each node, and dictionary of all the edges to each node in the graph.<br>
<br>
__def __init __(self):__<br>
this method initilizes a new directed weighted graph.<br>
<br>
__def v_size(self) -> int:__<br>
this method returns the number of nodes in the graph.<br>
<br>
__def e_size(self) -> int:__<br>
this method returns the number of edges in the graph<br>
<br>
__def get_all_v(self) -> dict:__
this method returns a dict with all the nodes in the graph, with the ID of each node ass the key and the node_data itself as the value.<br>
<br>
__def all_in_edges_of_node(self, id1: int) -> dict:__
this method returns a dict contains all the edges that comming to the given node.<br>
the src node as the key and the weight of the edge between them as the value.<br>
<br>
__def all_out_edges_of_node(self, id1: int) -> dict:__<br>
this method returns a dict contains all the edges that comming from the given node.<br>
the dest node as the key and the weight of the edge between them as the value.<br>

__def add_edge(self, id1: int, id2: int, weight: float) -> bool:__<br>
this method connect between the two given nodes with the given weight.<br>
if the weight is not positive, or if there is already an edge between the two nodes, or if one of them does not exist in the graph, the method does nothing and simply returns false.<br>
else, the method add the ID of the src node to the outedges dictionary of the graph, and add the ID of the dest to the Inedges dictionary of the graph.<br>
returns true.<br>
<br>
__def add_node(self, node_id: int, pos: tuple = None) -> bool:__<br>
this nethod creates a new node with the given id, and add it to the graph.<br>
it creates a new inner dictionery for each of the edge list for the new node, and returns true.<br>
<br>
__def remove_node(self, node_id: int) -> bool:__<br>
this method removes the node woth the given ID from the graph, and delete all its edges, coming out andd comming in.<br>
first, the method delete the node from the nodes dictionary, and then runs on each of its neighbors and pop the node from the list of neighbors of its neighbors.<br>
if the node removed successfully, the method returns true.<br>
if there is no such node the method returns false and simply does nothing.<br>
<br>
__def remove_edge(self, node_id1: int, node_id2: int) -> bool:__<br>
this method removes the edge between the two given nodes from the graph.<br>
if there is no such edge, or one of the nodes does not exist, the method returns false and does nothing<br>
delede from the dictionery of the inner edges the src node,and delede from the dictionery of the out edges the dest node,<br>
returns true.<br>
<br>
<h1>GraphAlgo class</h1>
<br>
__def load_from_json(self, file_name: str) -> bool:__<br>
this method load a new graph from the given jason.<br>
<br>
__def save_to_json(self, file_name: str) -> bool:__<br>
this method save the current graph to the given file name as a json type.<br>
<br>
__def shortest_path(self, id1: int, id2: int) -> (float, list):__<br>
this method calculate the shortest path between the two given nodes on a Directed (positive) Weighted Graph,<br>
 and returns the value of the path, with a list of all the nodes in the way. <br>
if there is no path between them the method returns 'inf' and empty list.<br>
first, the method initilizes the tag of each node in the graph to -1, and the weight of every node in the graph to be 0.<br>
then, by using Dijkstra's algorythem' the method.<br>
 We started with the node src and from there moved on to all its neighbors so that the weight of each node is updated to the value of the previous node and the edge beteen them weight .<br>
Then for each node we chose the neighbor with the lowest value until we went through all the nodes of the graph. <br>
The weight value of the dest is the minimum distance between the two nodes.<br>
<br>
__def connected_component(self, id1: int) -> list:__<br>
this method returns a list of all the nodes in the connected component of the given node<br>
if the node is not in the graph the method returns an empty list.<br>
first,  we create three diffrent lists.<br>
first, we initilizes the tag of all the nodes in the graph to -1. than, we add the node to the first list.<br>
then, while the list is not empty, we add the current node to the seconed lise, changes its tag to 0, and add all the nodes thats share an edge with the node, while he is the src.<br>
the loop goes untill  all the nodes that associeated with the node gets into the seconed list.<br>
then, we initilizes the tags of all the nodes again and start the whole procces again for the nodes that shares an edge with the node while he the node is the dest node.<br>
then, we find all the common nodes between the list.<br>
<br>
__def connected_components(self) -> List[list]:__<br>
this method returns a list of lists of all the connected components in the graph<br>
first, we creat a list and a Dictionary.<br>
then, we iterate each node in the graph and check if the node already has a connected componned<br>
and if it does not, we add the connected componnet of the specific node to the list.<br>
<br>
__def plot_graph(self) -> None:__<br>
this nethod uses matplotlib librery to create a visual graph for a directed weighted graph.<br>
 



