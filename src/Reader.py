from src.Graph import Graph
from src.Vertex import Vertex


class Reader:

    def __init__(self, file_name):
        self.__file = self.open_file(file_name)
        self.__edge_size = self.read_edge_size()
        self.__graph = self.prep_graph()

    @property
    def file(self):
        return self.__file

    @property
    def edge_size(self):
        return self.__edge_size

    @edge_size.setter
    def edge_size(self, value):
        self.__edge_size = value

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        self.__graph = value

    def read_edge_size(self):
        line = self.file.readline()
        fields = line.split(" ")
        return int(fields[0])

    def open_file(self, file_name):
        file = "../" + file_name
        return open(file, "r")

    def prep_graph(self):
        g = Graph(self.edge_size)
        for line in self.file.readlines():
            fields = line.split(" ")
            g.add_vertex(Vertex(int(fields[0])))
            g.add_vertex(Vertex(int(fields[1])))
            g.add_edge(int(fields[0]), int(fields[1]), int(fields[2]))
        return g
