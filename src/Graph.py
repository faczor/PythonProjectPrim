from src.Edge import Edge
from src.Vertex import Vertex


class Graph:

    def __init__(self, size):
        self.__vertex_size = 0
        self.__edge_size = 0
        self.__neighbours = self.prep_neighbours(size)
        self.__vertexes = []
        self.__edges = []

    def add_vertex(self, index):
        if not self.find_index(index.index):
            self.__vertexes.append(Vertex(index.index))
            self.vertex_size = self.vertex_size + 1

    def add_edge(self, v0, v1, value):
        self.edges.append(Edge(v0, v1, value))
        self.neighbours[v0][v1] = value
        self.edge_size = self.edge_size + 1
        self.edges.append(Edge(v1, v0, value))
        self.neighbours[v1][v0] = value
        self.edge_size = self.edge_size + 1

    def prep_neighbours(self, value):
        n = []
        for i in range(value):
            n.append([0] * value)
        return n

    def find_index(self, index):
        if self.vertex_size == 0:
            return False
        else:
            for v in self.vertexes:
                if v.index == index:
                    return True
            return False

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, value):
        self.__edges = value

    @property
    def vertexes(self):
        return self.__vertexes

    @property
    def vertex_size(self):
        return self.__vertex_size

    @vertex_size.setter
    def vertex_size(self, value):
        self.__vertex_size = value

    @property
    def edge_size(self):
        return self.__edge_size

    @edge_size.setter
    def edge_size(self, value):
        self.__edge_size = value

    @property
    def neighbours(self):
        return self.__neighbours

    @neighbours.setter
    def neighbours(self, value):
        self.__neighbours = value
