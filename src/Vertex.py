class Vertex:

    def __init__(self, index):
        self.__index = index

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        self.__index = value
